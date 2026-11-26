# The World Today — 25 November 2026

[![The World Today](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![Dense Front Page](https://make.fun/badge/news-image-20261125/akbare12/news-25-b13-dense/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![50 Stories, 10 Regions](https://make.fun/badge/news-image-20261125/akbare12/news-25-b13-dense/reward.svg)](https://make.fun/bounty/news-image-20261125)

Dense front page for the make.fun news-image bounty **news-image-20261125** ($100, top 50, closes 27 Nov 2026 07:00 WIB).

## Headlines

- **Trump tariffs:** new levies on 14 partners, China at 20%.
- **AI chip selloff:** Kospi -6.16% to 4,697.51; Samsung -9.87%, SK Hynix -11.05%.
- **Shenzhou-24:** first foreign astronaut on Tiangong — Pakistan's Muhammad Zeeshan Ali.
- **Bogor gold mine:** 9 dead, 17 trapped (25 Nov).

## Inside

50 stories across 10 regions, hero trio across the top, 13 illustration panels, story numbering on every card, map pins (Seoul, Bogor, Beijing, Islamabad), WHY IT MATTERS on every hero, certainty letters (C confirmed / R reported / CL claimed) on every card, and a sources footer.

## How it runs

- `gen.py` renders `entry.png` at build time (PIL).
- `main.py` is stdlib-only: it copies `entry.png` into `$MAKEFUN_OUTPUT_DIR/entry.png`.
- Verified with a stdlib-only venv simulation: clean venv without Pillow, different working directory, read-only repo copy, empty output dir.

## Bounty

[news-image-20261125 on make.fun](https://make.fun/bounty/news-image-20261125)
