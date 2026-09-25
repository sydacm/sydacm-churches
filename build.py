#!/usr/bin/env python3
"""Check churches.csv and build the map site into _site/.

    python3 build.py                  # check churches.csv, build _site/
    python3 -m http.server -d _site   # preview at http://localhost:8000

GitHub Actions runs this on every change. If churches.csv has a mistake, the
build stops and names the row, and the live maps stay as they were.
No extra Python packages are needed.
"""
import csv, json, pathlib, shutil, sys

ROOT = pathlib.Path(__file__).resolve().parent
SRC  = ROOT / "churches.csv"
OUT  = ROOT / "_site"
CATS = {"congregation", "translation", "groups", "unknown"}
REGIONS = {"City", "East", "Inner West", "North", "North-West", "South", "South-West", "West"}
PAGE = ["index.html", "site.webmanifest", "icon.svg", "favicon-32.png",
        "apple-touch-icon.png", "icon-192.png", "icon-512.png", "LICENSE"]

rows, errors = [], []
with SRC.open(encoding="utf-8-sig", newline="") as f:
    for n, r in enumerate(csv.DictReader(f), start=2):
        if None in r:
            errors.append(f"row {n} ({r.get('name','?')}): too many columns. If a value contains a comma, wrap it in \"double quotes\"")
            continue
        if not (r.get("name") or "").strip():
            errors.append(f"row {n}: name is empty")
            continue
        try:
            r["lat"] = float(r["lat"]); r["lng"] = float(r["lng"])
        except (TypeError, ValueError):
            errors.append(f"row {n} ({r['name']}): lat/lng is not a number")
            continue
        if not (-35 < r["lat"] < -33 and 150 < r["lng"] < 152):
            errors.append(f"row {n} ({r['name']}): coordinates are outside Sydney")
        if r["category"] not in CATS:
            errors.append(f"row {n} ({r['name']}): category '{r['category']}' must be one of {sorted(CATS)}")
        if r["region"] not in REGIONS:
            errors.append(f"row {n} ({r['name']}): region '{r['region']}' must be one of {sorted(REGIONS)}")
        r["languages"] = [x.strip() for x in (r["languages"] or "").split(";") if x.strip()]
        r["sunflower"] = (r["sunflower"] or "").strip().lower() in ("yes", "true", "1")
        rows.append(r)

if errors:
    print("Build failed. Nothing was published. Please fix:", file=sys.stderr)
    for e in errors:
        print("  -", e, file=sys.stderr)
    sys.exit(1)

geo = {
    "type": "FeatureCollection",
    "name": "Sydney Anglican Chinese congregations",
    "metadata": {
        "source": "Sydney Anglican Chinese Ministry — sydacm.github.io",
        "licence": "CC BY 4.0",
        "note": "Public contacts only. Ministers' personal numbers are not published here.",
        "categories": {
            "congregation": "Holds a service in Chinese, including bilingual services",
            "translation": "English service with live or AI translation",
            "groups": "Chinese Bible study or fellowship, no Chinese service",
            "unknown": "Listed historically, not yet confirmed by the church",
        },
        "coordinates": "Derived from street addresses (about 100 m accuracy) except St Paul's Carlingford, supplied by the church.",
    },
    "features": [{
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [r["lng"], r["lat"]]},
        "properties": {k: v for k, v in r.items() if k not in ("lat", "lng")},
    } for r in rows],
}

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()
for name in PAGE:
    if (ROOT / name).is_file():
        shutil.copy2(ROOT / name, OUT / name)
shutil.copy2(SRC, OUT / "churches.csv")
(OUT / "churches.geojson").write_text(json.dumps(geo, ensure_ascii=False, indent=1), encoding="utf-8")
(OUT / "churches.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
(OUT / ".nojekyll").write_text("")

churches = {r["name"] for r in rows}
print(f"OK — {len(churches)} churches, {len(rows)} sites")
for c in sorted(CATS):
    print(f"   {c:13} {len({r['name'] for r in rows if r['category'] == c})}")
