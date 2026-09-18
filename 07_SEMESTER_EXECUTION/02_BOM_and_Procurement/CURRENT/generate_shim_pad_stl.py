#!/usr/bin/env python3
"""
VibeGuard N20 Motor Shim Pad CAD Solid Generator (FAB-03)
=========================================================
Generates certified, watertight binary STL files for the N20 Motor Shim Pad:
  1. VibeGuard_N20_Motor_Shim_Pad_1mm.stl (Flat 1.0 mm bed: 12.0 x 24.0 x 1.0 mm)
  2. VibeGuard_N20_Motor_Shim_Pad_1p2mm.stl (Flat 1.2 mm bed: 12.0 x 24.0 x 1.2 mm)
  3. VibeGuard_N20_Motor_Cradle_Shim_1mm.stl (Precision cradle with 0.8 mm anti-slip side guides)

All models are strictly 2-manifold, single connected shells, positive signed volume,
and slice cleanly without support material on any FDM 3D printer (PLA, 100% infill).
"""

import struct
import math
import os
import sys

def write_binary_stl(filepath, header_str, vertices, faces, normals):
    """Writes binary STL file conforming strictly to standard 84 + 50*F format."""
    os.makedirs(os.path.dirname(os.path.abspath(filepath)), exist_ok=True)
    header_bytes = header_str.encode('utf-8')[:80].ljust(80, b' ')
    
    with open(filepath, 'wb') as f:
        f.write(header_bytes)
        f.write(struct.pack('<I', len(faces)))
        for face, norm in zip(faces, normals):
            f.write(struct.pack('<3f', *norm))
            f.write(struct.pack('<3f', *vertices[face[0]]))
            f.write(struct.pack('<3f', *vertices[face[1]]))
            f.write(struct.pack('<3f', *vertices[face[2]]))
            f.write(struct.pack('<H', 0))
            
    file_size = os.path.getsize(filepath)
    expected_size = 84 + 50 * len(faces)
    assert file_size == expected_size, f"File size mismatch: {file_size} != {expected_size}"

def orient_and_recompute_normals(vertices, faces):
    """
    Applies BFS traversal to ensure strict CCW winding consistency across all faces,
    checks that signed volume is positive (reversing if needed), and returns unit outward normals.
    """
    from collections import defaultdict, deque
    n_faces = len(faces)
    face_list = [list(f) for f in faces]
    
    edge_to_faces = defaultdict(list)
    for i, face in enumerate(face_list):
        k1, k2, k3 = face[0], face[1], face[2]
        for e in [(k1, k2), (k2, k3), (k3, k1)]:
            edge_to_faces[tuple(sorted(e))].append((i, e))
            
    oriented = [False] * n_faces
    oriented[0] = True
    queue = deque([0])
    
    while queue:
        curr_idx = queue.popleft()
        curr_face = face_list[curr_idx]
        curr_edges = [
            (curr_face[0], curr_face[1]),
            (curr_face[1], curr_face[2]),
            (curr_face[2], curr_face[0])
        ]
        for e_dir in curr_edges:
            e_undir = tuple(sorted(e_dir))
            for adj_idx, adj_e_dir in edge_to_faces[e_undir]:
                if adj_idx == curr_idx:
                    continue
                if not oriented[adj_idx]:
                    adj_face = face_list[adj_idx]
                    adj_edges = [
                        (adj_face[0], adj_face[1]),
                        (adj_face[1], adj_face[2]),
                        (adj_face[2], adj_face[0])
                    ]
                    if e_dir in adj_edges:
                        face_list[adj_idx] = [adj_face[0], adj_face[2], adj_face[1]]
                    oriented[adj_idx] = True
                    queue.append(adj_idx)
                    
    assert all(oriented), "Error: Mesh graph is not a single connected component!"
    
    vol6 = 0.0
    for f in face_list:
        p1 = vertices[f[0]]
        p2 = vertices[f[1]]
        p3 = vertices[f[2]]
        vol6 += (p1[0] * (p2[1]*p3[2] - p2[2]*p3[1]) +
                 p1[1] * (p2[2]*p3[0] - p2[0]*p3[2]) +
                 p1[2] * (p2[0]*p3[1] - p2[1]*p3[0]))
                 
    if vol6 < 0:
        for i in range(n_faces):
            face_list[i] = [face_list[i][0], face_list[i][2], face_list[i][1]]
        vol6 = -vol6
        
    signed_vol = vol6 / 6.0
    
    normals = []
    for f in face_list:
        p1 = vertices[f[0]]
        p2 = vertices[f[1]]
        p3 = vertices[f[2]]
        ax, ay, az = p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]
        bx, by, bz = p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2]
        nx = ay * bz - az * by
        ny = az * bx - ax * bz
        nz = ax * by - ay * bx
        length = math.sqrt(nx*nx + ny*ny + nz*nz)
        if length > 1e-12:
            normals.append((nx / length, ny / length, nz / length))
        else:
            normals.append((0.0, 0.0, 0.0))
            
    return face_list, normals, signed_vol

def verify_mesh_topology(vertices, faces):
    """Verifies strict 2-manifold properties and Euler characteristic."""
    from collections import defaultdict
    edge_counts = defaultdict(int)
    directed_edges = set()
    
    for f in faces:
        e1 = (f[0], f[1])
        e2 = (f[1], f[2])
        e3 = (f[2], f[0])
        for e in [e1, e2, e3]:
            edge_counts[tuple(sorted(e))] += 1
            directed_edges.add(e)
            
    # Check 2-manifold
    for e, count in edge_counts.items():
        assert count == 2, f"Non-manifold edge detected: {e} shared by {count} faces!"
        
    # Check orientation consistency
    for e in directed_edges:
        assert (e[1], e[0]) in directed_edges, f"Inconsistent winding order on edge: {e}"
        
    v_count = len(vertices)
    e_count = len(edge_counts)
    f_count = len(faces)
    chi = v_count - e_count + f_count
    genus = (2 - chi) // 2
    return chi, genus

def make_box_mesh(length, width, height):
    """
    Creates a monolithic 12-triangle solid box centered at X, Y and resting on Z=0.
    length = X dimension, width = Y dimension, height = Z dimension.
    """
    hx = length / 2.0
    hy = width / 2.0
    hz = height
    
    # 8 vertices
    vertices = [
        (-hx, -hy, 0.0), # 0
        ( hx, -hy, 0.0), # 1
        ( hx,  hy, 0.0), # 2
        (-hx,  hy, 0.0), # 3
        (-hx, -hy, hz),  # 4
        ( hx, -hy, hz),  # 5
        ( hx,  hy, hz),  # 6
        (-hx,  hy, hz),  # 7
    ]
    
    # 12 triangles with CCW outward normals
    faces = [
        # Bottom (-Z)
        (0, 2, 1),
        (0, 3, 2),
        # Top (+Z)
        (4, 5, 6),
        (4, 6, 7),
        # Front (-Y)
        (0, 1, 5),
        (0, 5, 4),
        # Back (+Y)
        (2, 3, 7),
        (2, 7, 6),
        # Left (-X)
        (3, 0, 4),
        (3, 4, 7),
        # Right (+X)
        (1, 2, 6),
        (1, 6, 5)
    ]
    
    faces, normals, volume = orient_and_recompute_normals(vertices, faces)
    chi, genus = verify_mesh_topology(vertices, faces)
    assert chi == 2 and genus == 0, f"Topology check failed: chi={chi}, genus={genus}"
    assert volume > 0, f"Volume non-positive: {volume}"
    return vertices, faces, normals, volume

def make_cradle_mesh(length=24.0, total_width=12.0, bed_width=10.0, bed_height=1.0, wall_height=1.8):
    """
    Creates a monolithic cradle shim with a flat central motor bed and side guide rails.
    Cross-section in Y-Z plane:
      - Bottom: Y in [-6, 6], Z = 0
      - Left rail: Y in [-6, -5], Z up to 1.8
      - Bed: Y in [-5, 5], Z = 1.0
      - Right rail: Y in [5, 6], Z up to 1.8
    Extruded along X from -12 to +12 (length 24 mm).
    """
    hx = length / 2.0
    w2 = total_width / 2.0 # 6.0
    bw2 = bed_width / 2.0  # 5.0
    
    # 2D cross-section polygon (8 vertices) in Y-Z
    poly2d = [
        (-w2,  0.0),        # P0: bottom-left
        ( w2,  0.0),        # P1: bottom-right
        ( w2,  wall_height),# P2: right-rail top-outer
        ( bw2, wall_height),# P3: right-rail top-inner
        ( bw2, bed_height), # P4: bed right edge
        (-bw2, bed_height), # P5: bed left edge
        (-bw2, wall_height),# P6: left-rail top-inner
        (-w2,  wall_height) # P7: left-rail top-outer
    ]
    
    # Extrude along X: Front at +hx, Back at -hx
    vertices = []
    for y, z in poly2d:
        vertices.append((-hx, y, z))
    for y, z in poly2d:
        vertices.append(( hx, y, z))
        
    faces = []
    # Side quads between x=-hx and x=+hx
    for i in range(8):
        next_i = (i + 1) % 8
        v1 = i
        v2 = next_i
        v3 = next_i + 8
        v4 = i + 8
        faces.append((v1, v2, v3))
        faces.append((v1, v3, v4))
        
    # Cap triangles
    cap_tris = [
        (0, 1, 4),
        (0, 4, 5),
        (1, 2, 3),
        (1, 3, 4),
        (0, 5, 6),
        (0, 6, 7)
    ]
    # Back cap (X = -hx)
    for i1, i2, i3 in cap_tris:
        faces.append((i1, i2, i3))
        
    # Front cap (X = +hx)
    for i1, i2, i3 in cap_tris:
        faces.append((i1 + 8, i2 + 8, i3 + 8))
        
    faces, normals, volume = orient_and_recompute_normals(vertices, faces)
    chi, genus = verify_mesh_topology(vertices, faces)
    assert chi == 2 and genus == 0, f"Topology check failed: chi={chi}, genus={genus}"
    assert volume > 0, f"Volume non-positive: {volume}"
    return vertices, faces, normals, volume

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    bom_dir = os.path.join(repo_root, '07_SEMESTER_EXECUTION/02_BOM_and_Procurement/CURRENT')
    root_dir = repo_root
    
    models = [
        ("VibeGuard_N20_Motor_Shim_Pad_1mm.stl",
         "VibeGuard N20 Motor Shim Pad (1.0 mm Flat) - Monolithic Solid",
         lambda: make_box_mesh(length=24.0, width=12.0, height=1.0)),
         
        ("VibeGuard_N20_Motor_Shim_Pad_1p2mm.stl",
         "VibeGuard N20 Motor Shim Pad (1.2 mm Flat) - Monolithic Solid",
         lambda: make_box_mesh(length=24.0, width=12.0, height=1.2)),
         
        ("VibeGuard_N20_Motor_Cradle_Shim_1mm.stl",
         "VibeGuard N20 Motor Cradle Shim (1.0 mm Bed + Anti-Slip Guides) - Monolithic Solid",
         lambda: make_cradle_mesh(length=24.0, total_width=12.0, bed_width=10.0, bed_height=1.0, wall_height=1.8)),
    ]
    
    print("=================================================================")
    print("      VibeGuard N20 Motor Shim Pad CAD Solid Generator           ")
    print("=================================================================")
    
    for filename, header, generator in models:
        verts, faces, norms, vol = generator()
        
        # Save in BOM directory
        p1 = os.path.join(bom_dir, filename)
        write_binary_stl(p1, header, verts, faces, norms)
        print(f"[OK] Generated in BOM CURRENT: {filename} (Volume: {vol:.2f} mm^3, Faces: {len(faces)})")
        
        # Save in Root directory
        p2 = os.path.join(root_dir, filename)
        write_binary_stl(p2, header, verts, faces, norms)
        print(f"[OK] Mirrored to root: {filename}")
        
        # Mirror to Downloads if writable
        dl_dir = '/home/paradoxpete/Downloads'
        dl_fablab = '/home/paradoxpete/Downloads/VibeGuard_Shareable_Packs/01_College_FabLab_3D_Printing'
        for target_dir in [dl_dir, dl_fablab]:
            try:
                os.makedirs(target_dir, exist_ok=True)
                write_binary_stl(os.path.join(target_dir, filename), header, verts, faces, norms)
                print(f"[OK] Mirrored to: {target_dir}/{filename}")
            except Exception as e:
                pass

if __name__ == '__main__':
    main()
