# 19 November 2026: the world in one front page

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/kai0x3/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/kai0x3/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

Entry for "Sum up 19 November's world news in one image" ($250, 50 places paid).
Free entry, no fee. Ends Sat 21 Nov 2026 00:00 UTC (07:00 WIB).

A single 1024x1024 newspaper front page summing up the world news of
Thursday 19 November 2026, drawn with PIL (see `build_image.py`).

## Format (dense wire edition)

This version follows the format that won the sibling 17 November
edition (1st place: "50 sourced stories, a UTC timeline and a date
check"; 2nd: "50 Verified Stories, UTC Wire & Date Audit") — density
of real, verifiable content over a sparse poster:

- **Date line + date check:** the masthead carries the explicit date
  (Thursday 19 November 2026) and a "DATE CHECKED" banner states that
  every story on the page is from that day.
- **UTC timeline:** a strip of the day's events in UTC order
  (overnight Iran attacks in the Gulf → tankers hit mines in Hormuz →
  APEC opens in Shenzhen → the first Trump–Xi–Putin summit → the ICJ's
  Myanmar genocide ruling → Anthropic's Nasdaq debut in the evening).
- **49 sourced stories:** 1 lead + 3 secondary stories + a numbered
  wire of 45 short items in four dense broadsheet columns. Every item
  names its source inline, in parentheses.

## Headlines

- **Lead — Trump, Xi and Putin meet in Shenzhen:** the three leaders
  hold the first-ever US–China–Russia summit at Kylin Villa, about 70
  minutes of talks ending in a "Declaration toward Peace" — but no
  arms-control deal and no mention of Ukraine or Iran.
- **World Court: Myanmar genocide:** the ICJ rules 9–6 that Myanmar
  committed genocide against the Rohingya in 2017 — about 10,000
  killed, 700,000+ fled to Bangladesh — and orders probes,
  compensation and returns.
- **Anthropic's record IPO:** Anthropic starts Nasdaq trading as ANT
  at $83, raising about $81.3bn in the largest IPO on record; shares
  open at $111.50 and briefly value the firm near $2tn.
- **Houthi missile hits Riyadh tower:** a suspected Houthi missile
  damages Riyadh's PIF Tower, the city's tallest skyscraper, blowing
  out windows across seven to eight floors; no injuries reported.
- **On the wire (45 items):** Israel's Gaza operation past the Yellow
  Line, Ukraine's third Kerch Bridge strike in a week, Russian strikes
  on Odesa, drones hitting a Tatarstan oil station, the Hormuz tanker
  fires, the EU's €45bn Ukraine loan, North Korea's expanding uranium
  enrichment, Denmark's Greenland security deal, the Jeffries speaker
  nomination, Musk's "not MAGA" turn, the GTA 6 launch, Bitcoin
  dipping below $63,000, South Florida floods, Cyclone Akvan
  evacuations, and more — each with its source printed next to it on
  the page.

## Sources

Every story was checked against the 19 November 2026 daily briefs of:

- **Level Headlines** — Daily Brief: Thursday, Nov. 19, 2026
  (levelheadlines.com/briefs/2026-11-19/)
- **Zark News** — Zark News Daily Briefing: November 19, 2026
  (zarknews.com)
- **Open Chronicle** — Global News Brief: Key Developments Around the
  World, November 19, 2026 (openchronicle.org)
- **EGazette** — Daily Brief — November 19, 2026
  (egazette.ai/daily/2026-11-19)
- **Just Security** — Early Edition: November 19, 2026
  (justsecurity.org)

Those briefs in turn cite the underlying reporting of Reuters, the
Associated Press, AFP, BBC News, CNBC, the New York Times, UN News,
the IAEA, Yonhap, The Atlantic, CoinDesk, Axios, CBS Colorado, the
Washington Times, Dawn, the Seattle Times and the Associated Press —
the specific source is printed on the page next to each story.

## Files

- `build_image.py` — PIL generator that draws `entry.png`
  (1024x1024: masthead with date line, date-checked banner, lead
  story, UTC timeline strip, three secondary stories, and the
  four-column numbered wire; the story count printed on the page is
  computed from what is actually rendered).
- `entry.png` — the rendered front page.
- `main.py` — deterministic entry point: copies `entry.png` to
  `/output/entry.png`. No network access, same output on every run.
- `README.md` — this file.
- `LICENSE` — MIT license.

## License

MIT — see `LICENSE`.
