# Public benchmark viewer

This folder contains a public, read-only visualization of the benchmark.
There are no API keys, judge settings, evaluation controls, delete buttons or localStorage administration tools.

## Files

- `index.html` — public site
- `benchmark-data.js` — generated public data
- `build_public_data.py` — rebuilds the data from `README.md` and optional `scores.json`

## Publish at the repository root

1. Keep the private/evaluation page under another name such as `admin.html`.
2. Copy these files to the repository root:
   - `index.html`
   - `benchmark-data.js`
   - `build_public_data.py`
3. Keep the benchmark result folders beside `index.html`, for example:

```text
index.html
benchmark-data.js
README.md
scores.json
02 - Excel clone/
12 - 3D castle scene/
15 - Space battle simulation/
32 - SVG pagoda with dragon/
33 - SVG infographic/
36 - Voxel world/
```

The viewer looks for PNG/JPG/WebP screenshots inside those test folders.

## Refresh data

Run from the repository root:

```bash
python build_public_data.py
```

The script reads `README.md`. If `scores.json` exists, it also includes public AI judge scores without including API keys or judge configuration.

## Local preview

```bash
python -m http.server 8000
```

Open `http://localhost:8000`.

## GitHub Pages

Set GitHub Pages to deploy from the repository root on the main branch, or use your existing Pages workflow.
Update the repository URL in the header link inside `index.html`.
