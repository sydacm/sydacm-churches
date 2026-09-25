# How this repository is set up

Everything is done on github.com. You don't need GitHub Desktop for this repository.

## Layout

All files sit at the top level, so updates are always a simple **Add file → Upload files** into one place. The only folder is `.github`, which holds the publishing workflow and the church update form. It's created on github.com (below), never by dragging.

## One-time settings (already done once; here for reference)

1. **Settings → Pages → Source: GitHub Actions.** The maps are built from `churches.csv` on every change.
2. The organisation has at least **two Owners**, so the ministry never depends on one person.

## Creating a file in `.github` (only if it's ever missing)

- **Add file → Create new file**
- Type the full name, including the folder, e.g. `.github/workflows/publish.yml`. GitHub creates the folders as you type the `/`.
- Paste the contents, then **Commit changes**.

## Checking it works

- **Actions** tab: the latest "Check and publish church maps" run is green.
- https://sydacm.github.io/sydacm-churches/ shows three maps with 39 points.
- The Find a Church page on https://sydacm.github.io/ shows the same churches.
