# Putting this on GitHub — 20 minutes

Everything below is done in a browser except step 3.

## 1. Make the organisation first
The repository belongs to the ministry, not to a person. An organisation means it
stays with SYDACM if whoever maintains it moves parishes.

- github.com → profile menu → **Your organizations** → **New organization**
- Choose the **Free** plan
- Organisation name: **`sydacm`**
- Contact email: your own

## 2. Make the repository inside the organisation
- On the organisation page → **New repository**
- Owner: **sydacm** (check this — it defaults to your personal account)
- Name: `sydacm-churches`
- **Public**
- Do **not** add a README, .gitignore or licence — this folder already has them

## 3. Push this folder — GitHub Desktop
- **File → Add Local Repository…** → choose the `sydacm-churches` folder
- It will say it is not a Git repository → click **create a repository**
- Leave **Git Ignore** and **License** as *None* (the folder already has them)
- **Create Repository**, then **Publish repository**
- Set the owner to **sydacm**, and **untick "Keep this code private"**

Keep the folder somewhere local such as `~/Documents`. Do not keep a git
repository inside iCloud Drive — iCloud evicts files and syncs the hidden
`.git` folder, which corrupts repositories.

## 4. Turn on GitHub Pages
- Repository → **Settings** → **Pages**
- Source: **GitHub Actions**

Within a minute the site is live at `https://sydacm.github.io/sydacm-churches/`

## 5. Allow Actions to commit
- **Settings** → **Actions** → **General** → Workflow permissions
- Choose **Read and write permissions**

## 5b. Add a second owner
- Organisation → **People** → invite one other person → make them an **Owner**

One person holding the only key is how this kind of thing gets lost.

This lets the workflow rebuild the map files when you edit the CSV.

## 6. Check it worked
- Open https://sydacm.github.io/sydacm-churches/
- **Three maps should load with 39 points.** This is the one thing that was not
  testable before publishing — if the maps are blank, say so.
- Open **Actions**. The run should be green.
- Open `church-update-links.csv`, click any link — the form should open with that church already chosen.

## 7. Link it from sydacm.com.au
Add a link from `/localchurch` to the new site. The Wix page stays the front door; this is the checkable data behind it.

---

## Editing the data later
Edit `data/churches.csv` in the browser (GitHub lets you edit files directly), commit, and the maps rebuild themselves. If you make a mistake the build fails and tells you which row.
