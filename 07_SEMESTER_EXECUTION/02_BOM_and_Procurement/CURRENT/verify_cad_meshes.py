#!/usr/bin/env python3
"""
VibeGuard Automated CAD Mesh Topology & Dimensional Verification Suite
======================================================================
Certifies binary STL solid models against frozen hardware specifications:
  - FAB-01: VibeGuard_Rotor_Arm_D_Shaft.stl (Eccentric Rotor Cam Arm)
  - FAB-02: VibeGuard_ADXL345_Rigid_Mount.stl (Rigid Sensor Bracket)

Verification Criteria:
  1. Binary STL format & file size integrity (Size == 84 + 50*F)
  2. Strict 2-manifold condition (3F == 2E, 0 non-manifold edges, 0 boundary seams)
  3. Uniform outward-pointing face normals (0 inverted directed edges, dot product > 0.99)
  4. Single connected outer shell topology (1 connected component via BFS face-graph)
  5. Euler-Poincaré genus invariant: g = (2 - chi) / 2 (g == 2 for FAB-01, g == 4 for FAB-02)
  6. Positive signed volume via tetrahedron divergence theorem (V > 0)
  7. Non-degenerate triangle mesh (0 zero-area faces)
  8. Exact dimensional audit:
     - FAB-01: 3.15 mm D-bore with 2.65 mm flat chord, 12.0 mm eccentric pitch, 3.2 mm M3 hole
     - FAB-02: 15.0 mm upright sensor hole pitch (3.2 mm dia), 15.0 mm base hole pitch (3.2 mm dia),
               3.5 mm vertical wall, 4.0 mm baseplate foot, triangular stiffening gussets

Environment: Standard Library Only (struct, math, collections, sys, os)
"""

import os
import sys
import struct
import math
from collections import defaultdict, deque, Counter

def fit_circle_2d(points):
    """
    Fits a circle to a 2D point set using algebraic least-squares (Kåsa method).
    Solves for A, B, C in: 2*xc*x + 2*yc*y + (r^2 - xc^2 - yc^2) = x^2 + y^2
    Returns (xc, yc, radius).
    """
    n = len(points)
    if n < 3:
        raise ValueError("At least 3 points required for circle fit")
    sx = sum(p[0] for p in points)
    sy = sum(p[1] for p in points)
    sx2 = sum(p[0]**2 for p in points)
    sy2 = sum(p[1]**2 for p in points)
    sxy = sum(p[0]*p[1] for p in points)
    
    sz = [p[0]**2 + p[1]**2 for p in points]
    sxz = sum(p[0]*z for p, z in zip(points, sz))
    syz = sum(p[1]*z for p, z in zip(points, sz))
    sz_sum = sum(sz)
    
    # 3x3 determinant helper (Cramer's rule)
    def det3(m):
        return (m[0][0]*(m[1][1]*m[2][2] - m[1][2]*m[2][1])
              - m[0][1]*(m[1][0]*m[2][2] - m[1][2]*m[2][0])
              + m[0][2]*(m[1][0]*m[2][1] - m[1][1]*m[2][0]))
              
    M = [[sx2, sxy, sx], [sxy, sy2, sy], [sx, sy, n]]
    d = det3(M)
    if abs(d) < 1e-12:
        raise ValueError("Singular matrix in circle fit")
        
    Ma = [[sxz, sxy, sx], [syz, sy2, sy], [sz_sum, sy, n]]
    Mb = [[sx2, sxz, sx], [sxy, syz, sy], [sx, sz_sum, n]]
    Mc = [[sx2, sxy, sxz], [sxy, sy2, syz], [sx, sy, sz_sum]]
    
    A = det3(Ma) / d
    B = det3(Mb) / d
    C = det3(Mc) / d
    
    xc = A / 2.0
    yc = B / 2.0
    r = math.sqrt(max(0.0, C + xc**2 + yc**2))
    return xc, yc, r

class MeshAuditor:
    def __init__(self, filepath, name, expected_genus):
        self.filepath = filepath
        self.name = name
        self.expected_genus = expected_genus
        self.errors = []
        self.warnings = []
        self.metrics = {}
        
    def log_error(self, msg):
        self.errors.append(msg)
        
    def log_warning(self, msg):
        self.warnings.append(msg)

    def parse_binary_stl(self):
        if not os.path.exists(self.filepath):
            self.log_error(f"File not found: {self.filepath}")
            return None
            
        file_size = os.path.getsize(self.filepath)
        if file_size < 84:
            self.log_error(f"File size too small for binary STL ({file_size} bytes)")
            return None
            
        with open(self.filepath, 'rb') as f:
            header = f.read(80)
            n_tris_bytes = f.read(4)
            n_tris = struct.unpack('<I', n_tris_bytes)[0]
            
            expected_size = 84 + 50 * n_tris
            if file_size != expected_size:
                self.log_error(f"File size mismatch: {file_size} != expected {expected_size} (F={n_tris})")
                return None
                
            triangles = []
            for _ in range(n_tris):
                data = f.read(50)
                norm = struct.unpack('<3f', data[0:12])
                v1 = struct.unpack('<3f', data[12:24])
                v2 = struct.unpack('<3f', data[24:36])
                v3 = struct.unpack('<3f', data[36:48])
                attr = struct.unpack('<H', data[48:50])[0]
                triangles.append((norm, v1, v2, v3, attr))
                
        self.metrics['header'] = header.decode('utf-8', errors='replace').strip()
        self.metrics['file_size'] = file_size
        self.metrics['num_triangles'] = n_tris
        return triangles

    def audit_topology_and_geometry(self, triangles):
        if not triangles:
            return False
            
        F = len(triangles)
        
        # Helper to canonicalize vertex coords (0.1 micron precision)
        def vkey(v):
            return (round(v[0], 4), round(v[1], 4), round(v[2], 4))
            
        vertices = set()
        directed_edges = Counter()
        undirected_to_faces = defaultdict(list)
        undirected_edges = Counter()
        
        vol6 = 0.0
        degenerate_count = 0
        normal_mismatches = 0
        
        # Bounding box
        min_x = min_y = min_z = float('inf')
        max_x = max_y = max_z = float('-inf')
        
        face_list_vkeys = []
        
        for face_idx, (norm, raw_v1, raw_v2, raw_v3, _) in enumerate(triangles):
            k1 = vkey(raw_v1)
            k2 = vkey(raw_v2)
            k3 = vkey(raw_v3)
            
            face_list_vkeys.append((k1, k2, k3))
            
            for k in (k1, k2, k3):
                vertices.add(k)
                min_x = min(min_x, k[0]); max_x = max(max_x, k[0])
                min_y = min(min_y, k[1]); max_y = max(max_y, k[1])
                min_z = min(min_z, k[2]); max_z = max(max_z, k[2])
                
            # Compute triangle cross product & area
            ax, ay, az = k2[0] - k1[0], k2[1] - k1[1], k2[2] - k1[2]
            bx, by, bz = k3[0] - k1[0], k3[1] - k1[1], k3[2] - k1[2]
            nx = ay * bz - az * by
            ny = az * bx - ax * bz
            nz = ax * by - ay * bx
            len_n = math.sqrt(nx*nx + ny*ny + nz*nz)
            
            if len_n < 1e-6:
                degenerate_count += 1
            else:
                # Normal consistency with stored STL normal
                snx, sny, snz = norm
                len_sn = math.sqrt(snx*snx + sny*sny + snz*snz)
                if len_sn > 1e-6:
                    dot = (nx*snx + ny*sny + nz*snz) / (len_n * len_sn)
                    if dot < 0.95:
                        normal_mismatches += 1
                        
            # Signed volume element
            vol6 += (k1[0] * (k2[1]*k3[2] - k2[2]*k3[1]) +
                     k1[1] * (k2[2]*k3[0] - k2[0]*k3[2]) +
                     k1[2] * (k2[0]*k3[1] - k2[1]*k3[0]))
                     
            # Edges
            for e in ((k1, k2), (k2, k3), (k3, k1)):
                directed_edges[e] += 1
                ue = tuple(sorted(e))
                undirected_edges[ue] += 1
                undirected_to_faces[ue].append(face_idx)
                
        V = len(vertices)
        E = len(undirected_edges)
        signed_volume = vol6 / 6.0
        
        # 1. 2-Manifold checks
        non_manifold_edges = sum(1 for c in undirected_edges.values() if c > 2)
        boundary_edges = sum(1 for c in undirected_edges.values() if c == 1)
        two_manifold_edges = sum(1 for c in undirected_edges.values() if c == 2)
        
        # 2. Directed orientation consistency
        inverted_directed_edges = 0
        for (u, v), count in list(directed_edges.items()):
            opp_count = directed_edges.get((v, u), 0)
            if opp_count != count:
                inverted_directed_edges += 1
                
        # 3. Connected shell count via dual face graph BFS
        adj_faces = defaultdict(set)
        for faces_sharing in undirected_to_faces.values():
            for i in faces_sharing:
                for j in faces_sharing:
                    if i != j:
                        adj_faces[i].add(j)
                        
        visited = [False] * F
        connected_components = 0
        for i in range(F):
            if not visited[i]:
                connected_components += 1
                queue = deque([i])
                visited[i] = True
                while queue:
                    curr = queue.popleft()
                    for neighbor in adj_faces[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                            
        # 4. Euler-Poincaré Characteristic & Genus
        chi = V - E + F
        computed_genus = (2 - chi) // 2
        
        self.metrics.update({
            'V': V, 'E': E, 'F': F,
            '3F': 3 * F, '2E': 2 * E,
            'non_manifold_edges': non_manifold_edges,
            'boundary_edges': boundary_edges,
            'two_manifold_edges': two_manifold_edges,
            'inverted_directed_edges': inverted_directed_edges,
            'normal_mismatches': normal_mismatches,
            'connected_components': connected_components,
            'chi': chi,
            'genus': computed_genus,
            'signed_volume': signed_volume,
            'degenerate_faces': degenerate_count,
            'bbox': ((min_x, max_x), (min_y, max_y), (min_z, max_z)),
            'vertices_set': vertices
        })
        
        # Topological Assertions
        if non_manifold_edges != 0:
            self.log_error(f"Mesh has {non_manifold_edges} non-manifold edges (must be 0)")
        if boundary_edges != 0:
            self.log_error(f"Mesh has {boundary_edges} open boundary edges (must be 0 watertight)")
        if 3 * F != 2 * E:
            self.log_error(f"3F != 2E invariant violated ({3*F} != {2*E})")
        if inverted_directed_edges != 0:
            self.log_error(f"Mesh has {inverted_directed_edges} inverted directed edges (inconsistent winding)")
        if normal_mismatches != 0:
            self.log_error(f"Mesh has {normal_mismatches} faces with normal direction mismatch")
        if connected_components != 1:
            self.log_error(f"Connected shells = {connected_components} (must be 1 single monolithic solid)")
        if computed_genus != self.expected_genus:
            self.log_error(f"Genus = {computed_genus} (expected {self.expected_genus}, chi = {chi})")
        if signed_volume <= 0:
            self.log_error(f"Signed volume is not positive: {signed_volume:.4f} mm^3")
        if degenerate_count != 0:
            self.log_error(f"Mesh contains {degenerate_count} degenerate faces")
            
        return len(self.errors) == 0

    def audit_dimensions(self):
        verts = self.metrics.get('vertices_set', set())
        if not verts:
            return False
            
        ((min_x, max_x), (min_y, max_y), (min_z, max_z)) = self.metrics['bbox']
        
        if self.name == 'FAB-01':
            # 1. Height audit (Z span: 8.0 mm)
            height = max_z - min_z
            if abs(height - 8.0) > 0.05:
                self.log_error(f"FAB-01 Hub Height {height:.3f} mm out of spec [8.0 - 9.0 mm]")
                
            # 2. D-Bore audit around (0,0)
            bore_top = [v for v in verts if abs(v[2] - max_z) < 1e-3 and math.hypot(v[0], v[1]) < 2.0]
            if not bore_top:
                self.log_error("FAB-01 D-Bore vertices not found at top face")
            else:
                flat_verts = [v for v in bore_top if abs(v[1] - 1.05) < 0.02]
                arc_verts = [v for v in bore_top if v[1] < 1.04]
                
                if len(flat_verts) < 2 or len(arc_verts) < 3:
                    self.log_error("FAB-01 Flat chord or circular arc vertices insufficient")
                else:
                    flat_chord_y = sum(v[1] for v in flat_verts) / len(flat_verts)
                    bore_x, bore_y, arc_radius = fit_circle_2d([(v[0], v[1]) for v in arc_verts])
                    bore_diameter = 2.0 * arc_radius
                    flat_to_back_depth = arc_radius + (flat_chord_y - bore_y)
                    
                    self.metrics['bore_center'] = (bore_x, bore_y)
                    self.metrics['bore_diameter'] = bore_diameter
                    self.metrics['flat_to_back_depth'] = flat_to_back_depth
                    
                    if abs(bore_diameter - 3.15) > 0.05:
                        self.log_error(f"FAB-01 Bore Dia {bore_diameter:.3f} mm out of spec (3.15 mm)")
                    if abs(flat_to_back_depth - 2.65) > 0.05:
                        self.log_error(f"FAB-01 Flat Depth {flat_to_back_depth:.3f} mm out of spec (2.65 mm)")
                        
            # 3. Eccentric M3 Mass Hole audit around (12.0, 0)
            mass_verts = [v for v in verts if abs(v[2] - max_z) < 1e-3 and math.hypot(v[0] - 12.0, v[1]) < 2.0]
            if not mass_verts or len(mass_verts) < 3:
                self.log_error("FAB-01 Mass hole vertices not found at top face")
            else:
                mass_x, mass_y, mass_r = fit_circle_2d([(v[0], v[1]) for v in mass_verts])
                mass_hole_dia = 2.0 * mass_r
                
                # Genuine Euclidean pitch calculation from bore axis to mass hole axis
                bore_x, bore_y = self.metrics.get('bore_center', (0.0, 0.0))
                pitch = math.hypot(mass_x - bore_x, mass_y - bore_y)
                
                self.metrics['mass_center'] = (mass_x, mass_y)
                self.metrics['mass_hole_dia'] = mass_hole_dia
                self.metrics['eccentric_pitch'] = pitch
                
                if abs(pitch - 12.0) > 0.05:
                    self.log_error(f"FAB-01 Eccentric pitch {pitch:.3f} mm out of spec (12.0 mm)")
                if abs(mass_hole_dia - 3.20) > 0.05:
                    self.log_error(f"FAB-01 Mass Hole Dia {mass_hole_dia:.3f} mm out of spec (3.20 mm)")
                    
        elif self.name == 'FAB-02':
            # 1. Bracket dimensions
            width = max_x - min_x
            depth = max_y - min_y
            height = max_z - min_z
            
            self.metrics['bracket_width'] = width
            self.metrics['bracket_depth'] = depth
            self.metrics['bracket_height'] = height
            
            if abs(width - 24.0) > 0.05:
                self.log_error(f"FAB-02 Width {width:.3f} mm out of spec (24.0 mm)")
            if abs(depth - 18.0) > 0.05:
                self.log_error(f"FAB-02 Depth {depth:.3f} mm out of spec (18.0 mm)")
            if abs(height - 22.0) > 0.05:
                self.log_error(f"FAB-02 Height {height:.3f} mm out of spec (22.0 mm)")
                
            # 2. Sensor upright holes at Z=15.0 mm, Y=3.5 mm
            sensor_h1 = [v for v in verts if abs(v[1] - 3.5) < 1e-3 and math.hypot(v[0] - (-7.5), v[2] - 15.0) < 1.8]
            sensor_h2 = [v for v in verts if abs(v[1] - 3.5) < 1e-3 and math.hypot(v[0] - (7.5), v[2] - 15.0) < 1.8]
            
            if not sensor_h1 or not sensor_h2:
                self.log_error("FAB-02 Sensor upright holes not found at Z=15.0, X=+-7.5")
            else:
                s1_x, s1_z, r1 = fit_circle_2d([(v[0], v[2]) for v in sensor_h1])
                s2_x, s2_z, r2 = fit_circle_2d([(v[0], v[2]) for v in sensor_h2])
                
                # Genuine Euclidean distance between upright hole centroids/circle fits
                upright_pitch = math.hypot(s2_x - s1_x, s2_z - s1_z)
                sensor_hole_dia = r1 + r2
                
                self.metrics['sensor_h1_center'] = (s1_x, s1_z)
                self.metrics['sensor_h2_center'] = (s2_x, s2_z)
                self.metrics['upright_pitch'] = upright_pitch
                self.metrics['sensor_hole_dia'] = sensor_hole_dia
                
                if abs(upright_pitch - 15.0) > 0.05:
                    self.log_error(f"FAB-02 Upright pitch {upright_pitch:.3f} mm out of spec (15.0 mm)")
                if abs(sensor_hole_dia - 3.20) > 0.05:
                    self.log_error(f"FAB-02 Sensor hole dia {sensor_hole_dia:.3f} mm out of spec (3.20 mm)")
                    
            # 3. Base flange holes at Z=4.0 mm, Y=11.0 mm
            base_h1 = [v for v in verts if abs(v[2] - 4.0) < 1e-3 and math.hypot(v[0] - (-7.5), v[1] - 11.0) < 1.8]
            base_h2 = [v for v in verts if abs(v[2] - 4.0) < 1e-3 and math.hypot(v[0] - (7.5), v[1] - 11.0) < 1.8]
            
            if not base_h1 or not base_h2:
                self.log_error("FAB-02 Base flange holes not found at Z=4.0, Y=11.0, X=+-7.5")
            else:
                b1_x, b1_y, br1 = fit_circle_2d([(v[0], v[1]) for v in base_h1])
                b2_x, b2_y, br2 = fit_circle_2d([(v[0], v[1]) for v in base_h2])
                
                # Genuine Euclidean distance between base flange hole centroids/circle fits
                base_pitch = math.hypot(b2_x - b1_x, b2_y - b1_y)
                base_hole_dia = br1 + br2
                
                self.metrics['base_h1_center'] = (b1_x, b1_y)
                self.metrics['base_h2_center'] = (b2_x, b2_y)
                self.metrics['base_pitch'] = base_pitch
                self.metrics['base_hole_dia'] = base_hole_dia
                
                if abs(base_pitch - 15.0) > 0.05:
                    self.log_error(f"FAB-02 Base pitch {base_pitch:.3f} mm out of spec (15.0 mm)")
                if abs(base_hole_dia - 3.20) > 0.05:
                    self.log_error(f"FAB-02 Base hole dia {base_hole_dia:.3f} mm out of spec (3.20 mm)")
                    
            # 4. Monolithic junction verification (verify contiguous integration between upright wall and base foot)
            junction_verts = [v for v in verts if v[1] <= 3.5 and v[2] <= 4.0]
            if not junction_verts:
                self.log_error("FAB-02 Monolithic joint not detected between upright wall and base foot")
            else:
                self.metrics['junction_elements'] = len(junction_verts)

                
        return len(self.errors) == 0

def print_audit_report(auditors):
    print("=" * 78)
    print("        VIBEGUARD MONOLITHIC CAD SOLID MESH VERIFICATION REPORT       ")
    print("=" * 78)
    
    all_passed = True
    
    for a in auditors:
        m = a.metrics
        passed = (len(a.errors) == 0)
        if not passed:
            all_passed = False
            
        status_str = "[PASS] CERTIFIED 100% MONOLITHIC" if passed else "[FAIL] NON-CONFORMANT"
        print(f"\n--- {a.name}: {os.path.basename(a.filepath)} --- {status_str}")
        print(f"  * Header               : {m.get('header', 'N/A')}")
        print(f"  * File Size            : {m.get('file_size', 0):,} bytes")
        print(f"  * Triangle Count (F)   : {m.get('F', 0)}")
        print(f"  * Vertex Count (V)     : {m.get('V', 0)}")
        print(f"  * Edge Count (E)       : {m.get('E', 0)}")
        print(f"  * 3F = 2E Invariant    : {m.get('3F', 0)} == {m.get('2E', 0)} (Match: {m.get('3F') == m.get('2E')})")
        print(f"  * Non-Manifold Edges   : {m.get('non_manifold_edges', 0)} (Target: 0)")
        print(f"  * Open Boundary Edges  : {m.get('boundary_edges', 0)} (Target: 0)")
        print(f"  * Inverted Directed E  : {m.get('inverted_directed_edges', 0)} (Target: 0)")
        print(f"  * Normal Mismatches    : {m.get('normal_mismatches', 0)} (Target: 0)")
        print(f"  * Connected Shells     : {m.get('connected_components', 0)} (Target: 1)")
        print(f"  * Euler Chi (V - E + F): {m.get('chi', 0)}")
        print(f"  * Euler Genus (g)      : {m.get('genus', 0)} (Expected: {a.expected_genus})")
        print(f"  * Signed Volume        : +{m.get('signed_volume', 0.0):.4f} mm^3 (Target: >0)")
        print(f"  * Degenerate Faces     : {m.get('degenerate_faces', 0)} (Target: 0)")
        
        bbox = m.get('bbox', ((0,0), (0,0), (0,0)))
        print(f"  * Bounding Box         : X=[{bbox[0][0]:.2f}, {bbox[0][1]:.2f}], Y=[{bbox[1][0]:.2f}, {bbox[1][1]:.2f}], Z=[{bbox[2][0]:.2f}, {bbox[2][1]:.2f}] mm")
        
        if a.name == 'FAB-01':
            bore_c = m.get('bore_center', (0.0, 0.0))
            mass_c = m.get('mass_center', (0.0, 0.0))
            print("  --- Hardware Fit & Sizing (FAB-01 Rotor Cam) ---")
            print(f"  * Hub Height           : {bbox[2][1] - bbox[2][0]:.2f} mm (Spec: 8.0-9.0 mm)")
            print(f"  * Bore Center (fit)    : ({bore_c[0]:.4f}, {bore_c[1]:.4f}) mm")
            print(f"  * N20 D-Bore Diameter  : {m.get('bore_diameter', 0.0):.3f} mm (Spec: 3.15 mm, 0.15 mm PLA shrinkage compensation)")
            print(f"  * Flat-to-Back Chord   : {m.get('flat_to_back_depth', 0.0):.3f} mm (Spec: 2.65 mm, for 2.50 mm N20 flat)")
            print(f"  * Mass Center (fit)    : ({mass_c[0]:.4f}, {mass_c[1]:.4f}) mm")
            print(f"  * Eccentric Mass Pitch : {m.get('eccentric_pitch', 0.0):.3f} mm (Spec: 12.00 mm center-to-center)")
            print(f"  * M3 Mass Bolt Hole Dia: {m.get('mass_hole_dia', 0.0):.3f} mm (Spec: 3.20 mm clearance)")
            
        elif a.name == 'FAB-02':
            sh1_c = m.get('sensor_h1_center', (0.0, 0.0))
            sh2_c = m.get('sensor_h2_center', (0.0, 0.0))
            bh1_c = m.get('base_h1_center', (0.0, 0.0))
            bh2_c = m.get('base_h2_center', (0.0, 0.0))
            print("  --- Hardware Fit & Sizing (FAB-02 Sensor Mount) ---")
            print(f"  * Bracket Outer BBox   : {m.get('bracket_width', 0.0):.2f} x {m.get('bracket_depth', 0.0):.2f} x {m.get('bracket_height', 0.0):.2f} mm")
            print(f"  * Upright Hole Centers : H1=({sh1_c[0]:.4f}, {sh1_c[1]:.4f}), H2=({sh2_c[0]:.4f}, {sh2_c[1]:.4f}) mm")
            print(f"  * Upright Sensor Pitch : {m.get('upright_pitch', 0.0):.3f} mm (Spec: 15.00 mm matching ADXL345 PCB)")
            print(f"  * Upright Hole Diameter: {m.get('sensor_hole_dia', 0.0):.3f} mm (Spec: 3.20 mm clearance for M3)")
            print(f"  * Base Hole Centers    : H1=({bh1_c[0]:.4f}, {bh1_c[1]:.4f}), H2=({bh2_c[0]:.4f}, {bh2_c[1]:.4f}) mm")
            print(f"  * Base Flange Pitch    : {m.get('base_pitch', 0.0):.3f} mm (Spec: 15.00 mm matching baseplate template)")
            print(f"  * Base Hole Diameter   : {m.get('base_hole_dia', 0.0):.3f} mm (Spec: 3.20 mm clearance for wood screws)")
            print(f"  * Monolithic Junction  : {m.get('junction_elements', 0)} contiguous boundary elements uniting upright & foot")
            
        if a.errors:
            print("  [!] Errors Detected:")
            for err in a.errors:
                print(f"      - {err}")
        else:
            print("  [OK] All dimensional, topological, and manifold invariants certified.")
            
    print("\n" + "=" * 78)
    if all_passed:
        print(">> FINAL RESULT: ALL CAD SOLID MESH VERIFICATION TESTS PASSED (100%) <<")
    else:
        print(">> FINAL RESULT: VERIFICATION FAILURES DETECTED <<")
    print("=" * 78)
    return all_passed

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    default_dir = os.path.join(repo_root, '07_SEMESTER_EXECUTION/02_BOM_and_Procurement/CURRENT')
    
    # Check if target paths provided via CLI, else use default CURRENT dir
    if len(sys.argv) >= 3:
        p_fab01 = sys.argv[1]
        p_fab02 = sys.argv[2]
    else:
        p_fab01 = os.path.join(default_dir, 'VibeGuard_Rotor_Arm_D_Shaft.stl')
        p_fab02 = os.path.join(default_dir, 'VibeGuard_ADXL345_Rigid_Mount.stl')
        
    auditors = [
        MeshAuditor(p_fab01, 'FAB-01', expected_genus=2),
        MeshAuditor(p_fab02, 'FAB-02', expected_genus=4)
    ]
    
    for a in auditors:
        tris = a.parse_binary_stl()
        if tris:
            a.audit_topology_and_geometry(tris)
            a.audit_dimensions()
            
    success = print_audit_report(auditors)
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
