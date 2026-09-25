# Updating church details 更新教会资料

There's one list, `churches.csv` (at the top of the sydacm-churches repository), and it feeds both the maps here and the **Find a Church** page on sydacm.github.io. Change it once, and both update within a couple of minutes.

教会名单只有一份：`churches.csv`。修改一次，两个网站都会自动更新。

---

## Who does what

| | |
|---|---|
| **Churches** keep their own details current | They click **Update this listing** under their church on sydacm.github.io. That opens an email to SYDACM with their current details filled in; they change what's different and send. No account needed. (If they have a GitHub account, they can use the update form instead.) |
| **SYDACM** checks and publishes | You read the request and change the CSV (below). Nothing goes live until you do, and that review step is what keeps the list trustworthy. |
| **Once a year** | Send each church its current listing and ask them to confirm or correct it. Claude can draft these emails for you (see the end of this page). |

---

## Path 1 — ask Claude (easiest)

Forward the church's email, or just describe the change, e.g. *"St Paul's Kogarah's Chinese service has moved to 9:30am"*. Attach the current `churches.csv` from GitHub (open it, then use the **download** button ↓).

Claude returns the corrected `churches.csv`, lists exactly what changed, and drafts a short bilingual reply to the church. Then:

1. On github.com, open the **sydacm-churches** repository, then **Add file → Upload files**.
2. Drag in the new `churches.csv`, write a short note (e.g. "Kogarah service time"), then **Commit changes**. It replaces the old one.

## Path 2 — edit it yourself on github.com

1. Open **churches.csv** in the sydacm-churches repository, then click the **pencil ✏️** icon.
2. Find the church's line, change it, then **Commit changes**.
3. Wait a minute. If the **Actions** tab turns red, it tells you which row to fix, and the live list stays as it was until then.

### The rules for each column

| Column | What goes in it |
|---|---|
| `name` | English name, exactly as it appears elsewhere in the file. A church with several sites has one row per site, **all with the same name**. |
| `name_zh` | Chinese name (optional). |
| `site` | Only for multi-site churches: the site's name, e.g. `Rockdale`. Otherwise blank. |
| `address` | Full street address. |
| `suburb`, `region` | Region is one of: City, East, Inner West, North, North-West, South, South-West, West. |
| `lat`, `lng` | Map position. In Google Maps, right-click the building; the first line of the menu is `-33.96, 151.13`. Paste those two numbers here. **Only change these if the address changes.** |
| `category` | Exactly one of: `congregation` (holds a Chinese or bilingual service) · `translation` (English service with live or AI translation) · `groups` (Chinese Bible study only) · `unknown` (not yet confirmed). |
| `languages` | Any of `Mandarin`, `Cantonese`, `Bilingual`, `Chinese`, separated by `;` |
| `sunflower` | `yes` if the church uses Sunflower AI translation, otherwise blank. |
| `services` | Each service separated by `;`, e.g. `Sun 9:00am English; Sun 11:00am Mandarin` |
| `translation` | Internal note for SYDACM. It isn't shown on the website. |
| `phone`, `email`, `website` | **Parish office only.** Never a minister's personal mobile or personal email. Website without `https://`. |

**Commas:** if a value contains a comma (most addresses do), the whole value must be wrapped in "double quotes", as the existing rows are. The GitHub editor is unforgiving here, so Path 1 is safer for anything beyond a small change.

---

## Before publishing a change

- **Changes about people**, like a new minister or a congregation closing, need confirming with the church by phone or email first.
- **Don't publish personal contacts**, even if a church sends them. Use the parish office.
- **A church that has stopped Chinese ministry:** delete its row, or set `category` to `unknown` while you check.

## The yearly check

Early each year, ask Claude to *"draft the annual listing check emails"*. Attach `churches.csv` and `church-update-links.csv`. You'll get one bilingual email per church, showing its current details and how to update them. Churches with no office email in the list are marked for a phone call instead.
