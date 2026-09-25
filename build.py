#!/usr/bin/env python3
"""Build docs/churches.geojson and docs/churches.json from data/churches.csv.

Run after editing the CSV:  python3 scripts/build.py
GitHub Actions runs this automatically on every push to main.
"""
import csv, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC  = ROOT / "data" / "churches.csv"
CATS = {"congregation", "translation", "groups", "unknown"}

rows, errors = [], []
with SRC.open(encoding="utf-8") as f:
    for n, r in enumerate(csv.DictReader(f), start=2):
        try:
            r["lat"] = float(r["lat"]); r["lng"] = float(r["lng"])
        except ValueError:
            errors.append(f"row {n} ({r.get('name','?')}): lat/lng is not a number")
            continue
        if not (-35 < r["lat"] < -33 and 150 < r["lng"] < 152):
            errors.append(f"row {n} ({r['name']}): coordinates are outside Sydney")
        if r["category"] not in CATS:
            errors.append(f"row {n} ({r['name']}): category '{r['category']}' is not one of {sorted(CATS)}")
        if not r["name"]:
            errors.append(f"row {n}: name is empty")
        r["languages"] = [x.strip() for x in r["languages"].split(";") if x.strip()]
        r["sunflower"] = r["sunflower"].strip().lower() in ("yes", "true", "1")
        rows.append(r)

if errors:
    print("Build failed:", file=sys.stderr)
    for e in errors:
        print("  -", e, file=sys.stderr)
    sys.exit(1)

geo = {
    "type": "FeatureCollection",
    "name": "Sydney Anglican Chinese congregations",
    "metadata": {
        "source": "Sydney Anglican Chinese Ministry — sydacm.com.au",
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

(ROOT / "docs" / "churches.geojson").write_text(
    json.dumps(geo, ensure_ascii=False, indent=1), encoding="utf-8")
(ROOT / "docs" / "churches.json").write_text(
    json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")

churches = {r["name"] for r in rows}
print(f"OK — {len(churches)} churches, {len(rows)} sites")
for c in sorted(CATS):
    n = len({r['name'] for r in rows if r['category'] == c})
    print(f"   {c:13} {n}")
