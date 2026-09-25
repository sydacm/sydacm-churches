# Chinese Congregations of the Diocese of Sydney
# 悉尼圣公会华文教会一览

Every Anglican church in the Diocese of Sydney with Chinese-language ministry — as an open, checkable dataset.

本仓库以公开、可查核的数据形式，收录悉尼教区所有设有华文事工的圣公会教会。

**Map and list → https://sydacm.github.io/sydacm-churches/**

Maintained by the [Sydney Anglican Chinese Ministry](https://www.sydacm.com.au) (SYDACM).

---

## Why this exists

In September 2026 the SYDACM listing was checked church by church for the first time in years. Of 29 entries, **24 needed amending**. Two congregations had moved. Two had closed their Chinese services. Five churches with Chinese ministry were missing from the list altogether.

None of that was anyone's fault. The list lived as typed text on a web page, so correcting it meant editing prose by hand, and nobody did. This repository exists so that never happens again: the data is a file, the file is public, anyone can see what changed and when, and any church can correct its own entry.

2026 年 9 月，我们首次逐间教会核对了 SYDACM 名单。29 项资料中有 **24 项需要更正**：两间教会已迁址，两间已停办华语崇拜，另有五间设有华文事工的教会完全未被收录。本仓库的目的，是让这种情况不再发生。

---

## What's here

| Path | What it is |
|---|---|
| `data/churches.csv` | **The source of truth.** Edit this file; everything else is generated. |
| `data/churches.json` | The same data as JSON. |
| `docs/index.html` | The public site — three maps and the full list. |
| `docs/churches.geojson` | Generated. Drop into any mapping tool. |
| `scripts/build.py` | Checks the CSV and rebuilds the map files. |
| `.github/ISSUE_TEMPLATE/` | The form a church uses to send changes. |

### The three maps

1. **By ministry type** — whether a church holds a service *in Chinese*, or an English service *with translation*. These are different things and the list had never distinguished them.
2. **By language** — Mandarin, Cantonese, or both in one service.
3. **Coverage** — roughly a 5 km reach around each church. The gaps are the point.

---

## Categories 分类

| Category | Meaning |
|---|---|
| `congregation` | Holds a service in Chinese, including bilingual services. 设有华语崇拜。 |
| `translation` | English service with live or AI translation. 英语崇拜，设有即时翻译。 |
| `groups` | Chinese Bible study or fellowship, no Chinese service. 设有华语小组，但无华语崇拜。 |
| `unknown` | Listed historically, not yet confirmed by the church. 历史记录，教会尚未确认。 |

The `congregation` / `translation` split is the most useful thing in this dataset. Eleven parishes now run **Sunflower AI translation** during an English service — several of them advertise it nowhere on their own websites. A visitor who cannot tell the two apart arrives expecting one and finds the other.

---

## How a church updates its entry

**No GitHub account is needed to email us; an account is needed to use the form.**

1. Open the [update form](../../issues/new?template=update-listing.yml).
2. Choose your church from the list.
3. Tell us only what has **changed** — or tick the box to say everything is still correct.
4. We check it and update the file. You will see the change in this repository.

Each church has its own pre-filled link in `church-update-links.csv`. Those links are **identifiers, not passwords** — see below.

如需更新资料，请使用上方表格，或直接联络 SYDACM。

---

## About the links, and why there are no secret tokens

An earlier design gave each church a secret token in a private link. That works when a change goes live immediately, because the secret is the only thing standing between a stranger and your listing.

It does not belong in a public repository. **Anything committed here is public forever**, including its history — a secret token in a public repo is not a secret.

GitHub replaces it with something better. Every change is a **public proposal that a maintainer approves**. The per-church links simply pre-fill the form with the right church; anyone can open one, and that is fine, because nothing reaches the data until a person accepts it. The review step *is* the security.

Changes about **people** — a minister's name, a congregation closing — are confirmed with that church directly before they are merged.

---

## Privacy 私隐

**Ministers' personal mobile numbers and personal email addresses are not published here.** They were given for the SYDACM listing, not for a public dataset that can be cloned and scraped, and git history cannot be cleanly erased on request. Only parish offices and church websites appear.

The full contact list is held privately by SYDACM. To reach a minister, contact the parish office or [sydacm.com.au](https://www.sydacm.com.au).

本仓库不刊登牧者私人手机号码及私人电邮。如需联络，请透过堂区办公室或 sydacm.com.au。

---

## Coordinates

Derived from street addresses — accurate to roughly 100 m. Good enough to plot the diocese; **not** good enough for navigation. One exception: St Paul's Carlingford supplied surveyed coordinates. Other churches are welcome to do the same.

---

## Editing the data

```bash
# edit data/churches.csv, then:
python3 scripts/build.py
```

The script refuses to build if a row has a bad category, a missing name, or coordinates outside Sydney. GitHub Actions runs the same check on every push and rebuilds the published maps.

---

## Licence

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — use it, please credit the Sydney Anglican Chinese Ministry.
Code: MIT.

---

*Verified 14–24 September 2026 with each church. Details change. If something here is wrong, that is worth ten minutes of your time to tell us.*
