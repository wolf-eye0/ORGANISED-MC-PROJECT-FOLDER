# VibeGuard Local Dashboard

Presentation-ready local condition-monitoring dashboard for an ESP32 + ADXL345 motor rig. The first launch uses deterministic **PREVIEW DATA**. Live mode uses the included Node WebSocket/serial bridge.

## Start

```bash
npm install
npm start
```

Open `http://127.0.0.1:8765/vibeguard-dashboard.html`.

## Preview and live modes

- Preview: default URL, or `?source=preview`.
- Live: `http://127.0.0.1:8765/vibeguard-dashboard.html?source=live`.
- Configure a serial port: macOS/Linux `SERIAL_PORT=/dev/ttyUSB0 npm start`; Windows PowerShell `$env:SERIAL_PORT='COM5'; npm start`.
- Optional port auto-detection: `AUTO_SERIAL=true npm start`.

The frontend consumes one canonical sample model. `public/js/telemetry-adapter.js` is the only file intended for final firmware packet mapping.

## Supported bridge input

The bridge accepts newline-delimited JSON from the ESP32. It also exposes deliberately conservative best-effort parsing for labelled key/value lines and a documented CSV order. Unrecognized lines are forwarded as raw packets and rejected safely by the frontend adapter.

## Keyboard and presentation

- `P`: presentation mode, unless typing in a field.
- `Escape`: close an open drawer.
- All interactive controls are keyboard reachable.
- Reduced-motion preferences are respected.

## Safety and claims

Preview values are deterministic UI fixtures, not hardware measurements. The dashboard does not claim RPM, machine health percentage, ISO compliance, FFT results, or diagnosed fault classes.
