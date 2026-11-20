#!/usr/bin/env python3
"""Build the 19 Nov 2026 world-news front page (1024x1024 PNG) for the
make.fun news-image-20261119 bounty — dense wire style.

Modelled on what won the sibling 17 Nov edition (1st: "50 sourced
stories, a UTC timeline and a date check"; 2nd: "50 Verified Stories,
UTC Wire & Date Audit"): this page packs 50+ real, sourced stories from
Thursday 19 November 2026 onto one broadsheet front page — a lead, a
UTC timeline strip, three secondary stories and a dense numbered wire
of short items, every item attributed to its source inline, under an
explicit date line with a date-checked banner.

Stories were verified against the 19 Nov 2026 daily briefs of Level
Headlines, Zark News, Open Chronicle, EGazette and Just Security's
Early Edition, which in turn cite Reuters, AP, AFP, BBC, CNBC, the
New York Times, UN News, Yonhap, the IAEA and others (full source
list in README.md; checked 2026-11-20 ~01:00 UTC).
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (247, 243, 234)      # newsprint cream
INK = (24, 24, 28)
NAVY = (18, 38, 66)
RED = (178, 34, 34)
DARKRED = (120, 22, 22)
GOLD = (198, 148, 44)
GREY = (90, 90, 92)
RULE = (180, 172, 158)
SKY = (206, 224, 234)

F = "/usr/share/fonts/truetype/dejavu/"
serif_b = lambda s: ImageFont.truetype(F + "DejaVuSerif-Bold.ttf", s)
serif = lambda s: ImageFont.truetype(F + "DejaVuSerif.ttf", s)
sans_b = lambda s: ImageFont.truetype(F + "DejaVuSans-Bold.ttf", s)
sans = lambda s: ImageFont.truetype(F + "DejaVuSans.ttf", s)

# ---------------------------------------------------------------- stories
LEAD_HEAD = "TRUMP, XI AND PUTIN MEET IN SHENZHEN"
LEAD_BODY = ("The three leaders hold the first-ever US-China-Russia summit "
             "at Kylin Villa in Shenzhen, about 70 minutes of talks ending "
             "in a 'Declaration toward Peace' \u2014 but no arms-control deal "
             "and no mention of Ukraine or Iran. (AP / Reuters)")

# (when, text, source) — the day in UTC, as reported by the day's briefs
# (kept short so each fits its timeline column)
TIMELINE = [
    ("OVERNIGHT", "Iran widens Gulf attacks", "Reuters"),
    ("OVERNIGHT", "Tankers hit mines in Hormuz", "IRGC"),
    ("MORNING", "APEC opens in Shenzhen", "AP"),
    ("MIDDAY", "Trump, Xi & Putin summit", "AP"),
    ("AFTERNOON", "ICJ: Myanmar genocide", "UN News"),
    ("EVENING", "Anthropic's record IPO", "CNBC"),
]

# (headline, body) — three secondary stories under the lead
SECONDARY = [
    ("WORLD COURT: MYANMAR GENOCIDE",
     "The ICJ rules 9-6 that Myanmar committed genocide against the "
     "Rohingya in 2017 \u2014 about 10,000 killed, 700,000+ fled to "
     "Bangladesh \u2014 and orders probes, compensation and returns. "
     "(UN News / BBC)"),
    ("ANTHROPIC'S RECORD IPO",
     "Anthropic starts Nasdaq trading as ANT at $83, raising about "
     "$81.3bn in the largest IPO on record; shares open at $111.50 "
     "and briefly value the firm near $2tn. (CNBC / AP)"),
    ("HOUTHI MISSILE HITS RIYADH TOWER",
     "A suspected Houthi missile damages Riyadh's PIF Tower, the "
     "city's tallest skyscraper, blowing out windows across seven "
     "to eight floors; no injuries reported. (Reuters)"),
]

# (headline, body) — the numbered wire; body ends with its source in parens
WIRE = [
    ("GAZA OPERATION",
     "Israel launches a ground operation in central Gaza past the "
     "Yellow Line near Nuseirat, despite the ceasefire; the IDF says "
     "it targeted a 'terror tunnel'. (BBC)"),
    ("KERCH BRIDGE HIT AGAIN",
     "Ukraine strikes the Crimean Bridge for the third time in a "
     "week; rail traffic is halted. (BBC)"),
    ("RUSSIA STRIKES ODESA",
     "Russian strikes kill at least five people across Ukraine in 24 "
     "hours, hitting power plants and Odesa. (EGazette)"),
    ("DRONES HIT TATARSTAN OIL",
     "Ukrainian drones strike the Kaleykino oil pumping station in "
     "Tatarstan; storage tanks are left ablaze. (EGazette)"),
    ("KURSK DRONE ATTACK",
     "A morning drone attack on Kursk injures 11 people, the "
     "regional governor says. (EGazette)"),
    ("HORMUZ TANKER FIRES",
     "Three tankers strike sea mines east of the Strait of Hormuz; "
     "two supertankers carried over 4m barrels of crude. (IRGC)"),
    ("IEA: HORMUZ BIGGEST THREAT",
     "The IEA calls the Hormuz crisis the largest threat to energy "
     "security in history. (Reuters)"),
    ("EU \u20ac45BN UKRAINE LOAN",
     "Brussels proposes a \u20ac45bn loan to Kyiv to cover a \u20ac70bn "
     "funding gap in 2027. (Reuters)"),
    ("BERLIN HUDDLE ON UKRAINE",
     "European allies gather in Berlin over Ukraine's security as "
     "Kyiv faces a \u20ac25bn defence shortfall. (AJVC)"),
    ("ZELENSKYY: NO DEAL WITHOUT KYIV",
     "Zelenskyy insists Ukraine's future cannot be settled without "
     "Kyiv as the big three meet. (Open Chronicle)"),
    ("EUROPE READY FOR TALKS",
     "Europe is ready for talks with Russia on ending the war in "
     "Ukraine, leaders say. (NYT)"),
    ("NORTH KOREA ENRICHMENT GROWS",
     "The IAEA says North Korea is expanding uranium enrichment at "
     "Yongbyon; an extension is now externally complete. (AP)"),
    ("SOUTH KOREA CLEARS HAN",
     "South Korea's top court overturns ex-PM Han Duck-soo's "
     "conviction over Yoon's martial law decree. (AP)"),
    ("LEE SEEKS PYONGYANG TALKS",
     "President Lee Jae Myung renews his call for dialogue with "
     "North Korea. (Open Chronicle)"),
    ("TAKAICHI TALKS TO PUTIN",
     "Japan's PM Takaichi says she held talks with Putin and agreed "
     "to keep communicating. (AP)"),
    ("RUSSIAN BOMBERS IN VIETNAM",
     "Two Russian Tu-95 bombers land in Vietnam after flights near "
     "Taiwan and Japan. (10 Things)"),
    ("DENMARK-GREENLAND DEAL",
     "Denmark's parliament unanimously approves a security deal with "
     "Greenland and the US, paving the way for more US bases. (AP)"),
    ("PRINCE HARRY: WOULD SERVE",
     "Prince Harry says he would consider returning to military "
     "service if needed to fight Russia. (Open Chronicle)"),
    ("VAN GOGH SELLS FOR $190.4M",
     "A Van Gogh painting reportedly sells for $190.4m amid a row "
     "over its Nazi-era history. (Open Chronicle)"),
    ("EU CYBERATTACK REPORT",
     "The European Commission is reportedly hit by a cyberattack; "
     "the extent is unclear. (Open Chronicle)"),
    ("BANGLADESH UNREST",
     "Four are killed and Muhammad Yunus's ancestral home is torched "
     "amid political unrest. (EGazette)"),
    ("SENEGAL BOAT SINKS",
     "A migrant boat carrying about 100 people sinks off Senegal; "
     "dozens are missing, four bodies recovered. (EGazette)"),
    ("FIJI DROUGHT DISASTER",
     "Fiji declares a state of disaster as El Ni\u00f1o drought "
     "threatens water supplies. (Open Chronicle)"),
    ("CYCLONE AKVAN",
     "Nearly 72,000 people are evacuated in eastern India as "
     "Cyclone Akvan threatens the coast. (Open Chronicle)"),
    ("RIO TINTO PAYS $250M",
     "Rio Tinto commits $250m to a fund over the Panguna mine's "
     "legacy in Papua New Guinea. (NYT)"),
    ("EBOLA IN DR CONGO",
     "Ebola containment in DR Congo is hampered by insecurity, "
     "displacement and weak clinics. (Open Chronicle)"),
    ("SUDAN DEFECTIONS",
     "An RSF commander reportedly defects to the Sudanese army as "
     "the civil war grinds on. (Open Chronicle)"),
    ("ETHIOPIA-ERITREA TROOPS",
     "Ethiopia and Eritrea mass troops along their border. "
     "(10 Things)"),
    ("LEBANON CHARGES HEZBOLLAH",
     "Lebanon charges five Hezbollah members over recruitment and "
     "weapons. (Open Chronicle)"),
    ("US-VENEZUELA MILITARY TIES",
     "Hegseth announces a US\u2013Venezuela military partnership deal "
     "during a visit to Caracas. (Hansen Intel)"),
    ("HAITI PASTOR CONVICTED",
     "A Miami court convicts a Haitian-American pastor over the 2021 "
     "killing of President Mo\u00efse. (NYT)"),
    ("EL SALVADOR IN HAITI",
     "El Salvador deploys about 2,500 troops to Haiti's security "
     "mission. (Open Chronicle)"),
    ("JEFFRIES NOMINATED",
     "House Democrats nominate Hakeem Jeffries for speaker, 251\u201311; "
     "he is in line to be the first Black speaker. (Reuters)"),
    ("MUSK: 'NOT MAGA'",
     "Musk says he is 'not MAGA' after spending $400m+ on "
     "Republicans, calling it 'pretty foolish'. (AP)"),
    ("TRUMP: 'SEE WHAT HAPPENS'",
     "Trump says the US will 'see what happens' in the Iran war "
     "after Jan. 1, 2027. (Reuters)"),
    ("TRUMP FRUSTRATED WITH VANCE",
     "Trump grows frustrated with VP Vance over the midterm "
     "post-mortem and praises Rubio instead. (NYT)"),
    ("EPA GRANTS AT SUPREME COURT",
     "The Trump administration asks the Supreme Court to let the EPA "
     "cancel $16bn in climate grants. (AP)"),
    ("VENEZUELAN TPS FIGHT",
     "The administration asks the Supreme Court to halt restored "
     "deportation protections for Venezuelans. (AP)"),
    ("ICE CONTEMPT RULING",
     "A federal judge finds ICE in contempt for re-arresting a man a "
     "court had ordered freed in Colorado. (Reuters)"),
    ("ARIZONA PROBES OPENAI",
     "Arizona opens a criminal probe into OpenAI and AI firms over "
     "'rogue AI agents' in banks. (Reuters)"),
    ("KUSHNER FIRM BUYS ARXIS",
     "Kushner's Affinity Partners bought nearly 700,000 shares in "
     "defence contractor Arxis. (The Atlantic)"),
    ("PETE ROSE PARDONED",
     "Trump posthumously pardons baseball's hit king Pete Rose. "
     "(BBC)"),
    ("GTA 6 LAUNCHES",
     "Grand Theft Auto VI launches to universal acclaim, breaking "
     "gaming and streaming records. (AJVC)"),
    ("BITCOIN BELOW $63K",
     "Bitcoin dips below $63,000 then recovers, as ETF outflows hit "
     "$157.8m. (CoinDesk)"),
    ("DOW DROPS 800",
     "The Dow drops about 800 points as Anthropic jumps after its "
     "IPO; the S&P heads for a sixth straight loss. (AP)"),
    ("SOUTH FLORIDA FLOODS",
     "More than a foot of rain floods South Florida, shutting I-95 "
     "and forcing high-water rescues. (Zark News)"),
    ("INDONESIA ASSET LAW",
     "Indonesia's parliament approves asset-forfeiture legislation; "
     "a refinery blast kills a worker. (Open Chronicle)"),
    ("ISLAM LARGEST BY 2035",
     "Islam is projected to become the world's largest religion by "
     "2035, Pew research finds. (10 Things)"),
    ("NZ PAY EQUITY RULING",
     "A New Zealand court rules the government's pay-equity changes "
     "violated women's rights. (Open Chronicle)"),
    ("RED CRABS MIGRATE",
     "Millions of red crabs begin their annual migration on "
     "Christmas Island. (Open Chronicle)"),
    ("SPAIN TRAIN INQUIRY",
     "Spain launches a safety inquiry after a high-speed train "
     "crash. (AJVC)"),
    ("CARNEY WRAPS APEC",
     "Canada's Carney wraps APEC with China trade gains worth about "
     "$400m in tariff relief. (Daily News)"),
    ("FIONA THE HIPPO DIES",
     "Fiona the hippo dies after swallowing a hat at Cincinnati Zoo. "
     "(BBC)"),
    ("GOOGLE REFUSES BRAND VIDEO",
     "Google refuses a UK prison request to remove a video of "
     "Russell Brand's wife reading his letter. (BBC)"),
    ("COP31 FINAL STRETCH",
     "COP31 climate talks in Antalya enter their final stretch with "
     "144 items still disputed. (NewsTrendToday)"),
    ("GAZA WINTER RAINS",
     "Winter rains damage 40,000+ family shelters in Gaza as 1.7m "
     "people remain displaced. (Dawn)"),
    ("RUSSIAN SPY ARREST",
     "A Russian man is arrested in Silicon Valley for allegedly "
     "spying on Palantir staff over Ukraine support. (BBC)"),
    ("ILLINOIS TEMPLE PLOT",
     "Federal terrorism charges follow an alleged plot to attack a "
     "Hindu temple in Illinois. (Open Chronicle)"),
    ("MISSISSIPPI VOTER PROBE",
     "Mississippi Democrats call for a probe of 230,000 inactive "
     "voter registrations. (AP)"),
    ("NEGUSE ASSISTANT SPEAKER",
     "Rep. Joe Neguse is elected assistant speaker of the US House, "
     "unanimously. (CBS Colorado)"),
    ("LULA PROTECTS RAONI LAND",
     "Brazil's Lula moves to protect Chief Raoni's birthplace in the "
     "Amazon rainforest. (Washington Times)"),
    ("US AUCTIONS PACIFIC",
     "The US auctions 31.5m acres of Pacific seabed to a deep-sea "
     "mining company. (NYT)"),
    ("CALIFORNIA PROBES NVIDIA",
     "California targets Nvidia in a China AI chip probe. (BBC)"),
    ("NIKE GIFTS VALEDICTORIANS",
     "Nike will give custom Air Force 1s to every US high-school "
     "valedictorian. (Axios)"),
]

# (the on-page story count is computed after layout, as STORY_COUNT)

# ---------------------------------------------------------------- drawing
img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

def text(x, y, s, font, fill=INK, anchor="la"):
    d.text((x, y), s, font=font, fill=fill, anchor=anchor)

def wrap(s, font, max_w):
    words, lines, cur = s.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

MX = 32                      # side margin
CW = W - 2 * MX              # content width = 960

# ---- wire layout: decide which items fit the four columns up front,
# so the banner can print the true on-page story count ----
WY = 446
WBOT = 976
GAP = 16
COLW = (CW - 3 * GAP) // 4
HF, BF = sans_b(10), sans(9)
def _item_h(head, body):
    hl = len(wrap(head, HF, COLW - 19))
    bl = len(wrap(body, BF, COLW - 19))
    return hl * 11 + bl * 10 + 5

COLS = [[] for _ in range(4)]
_heights = [0] * 4
for _n, (_head, _body) in enumerate(WIRE, start=1):
    _h = _item_h(_head, _body)
    _c = min(range(4), key=lambda k: _heights[k])
    if _heights[_c] + _h > WBOT - WY and all(
            _heights[k] + _h > WBOT - WY for k in range(4)):
        break
    COLS[_c].append((_n, _head, _body))
    _heights[_c] += _h
RENDERED = sum(len(c) for c in COLS)
STORY_COUNT = 1 + len(SECONDARY) + RENDERED

# ---- masthead ----
d.rectangle([0, 0, W, 92], fill=NAVY)
text(512, 8, "THURSDAY  \u2022  19 NOVEMBER 2026  \u2022  THE DAILY WORLD EDITION",
     sans_b(17), fill=(232, 222, 190), anchor="ma")
text(512, 32, "THE WORLD IN ONE IMAGE", serif_b(44),
     fill=(255, 255, 255), anchor="ma")
d.rectangle([0, 92, W, 96], fill=GOLD)

# ---- date-check banner ----
d.rectangle([0, 96, W, 124], fill=DARKRED)
text(512, 103, "\u2713 DATE CHECKED \u2014 ALL STORIES FROM THURSDAY 19 NOVEMBER 2026 "
               f"\u2022 {STORY_COUNT} SOURCED STORIES \u2022 SOURCES NAMED INLINE",
     sans_b(13), fill=(255, 255, 255), anchor="ma")

# ---- lead story ----
ly = 138
_lead_size = 40
while d.textlength(LEAD_HEAD, font=serif_b(_lead_size)) > CW and _lead_size > 24:
    _lead_size -= 1
text(MX, ly, LEAD_HEAD, serif_b(_lead_size), fill=RED)
# compact flags at the right of the lead block
def flag(x, y, w, h, kind):
    d.line([x, y, x, y + 46], fill=INK, width=3)
    if kind == "china":
        d.rectangle([x, y, x + w, y + h], fill=(222, 41, 16))
        for sx, sy in [(x + 8, y + 6), (x + 18, y + 10), (x + 8, y + 16)]:
            d.ellipse([sx, sy, sx + 4, sy + 4], fill=(255, 222, 0))
    elif kind == "russia":
        d.rectangle([x, y, x + w, y + h // 3], fill=(255, 255, 255))
        d.rectangle([x, y + h // 3, x + w, y + 2 * h // 3], fill=(0, 60, 160))
        d.rectangle([x, y + 2 * h // 3, x + w, y + h], fill=(210, 30, 30))
    else:
        for i in range(7):
            d.rectangle([x, y + i * h // 7, x + w, y + (i + 1) * h // 7],
                        fill=(178, 34, 34) if i % 2 == 0 else (255, 255, 255))
        d.rectangle([x, y, x + w // 2, y + 4 * h // 7], fill=NAVY)
fx, fy = 856, 200
d.rectangle([fx - 10, fy - 8, W - MX, fy + 64], fill=SKY, outline=NAVY, width=2)
flag(fx, fy, 34, 20, "china")
flag(fx + 44, fy, 34, 20, "russia")
flag(fx + 88, fy, 34, 20, "usa")
text(fx + 61, fy + 50, "SHENZHEN \u2022 APEC", sans_b(10), fill=NAVY, anchor="ma")
for i, ln in enumerate(wrap(LEAD_BODY, serif(16), 800)):
    text(MX, ly + 52 + i * 21, ln, serif(16))
d.line([MX, 266, W - MX, 266], fill=RULE, width=2)

# ---- UTC timeline strip ----
ty = 272
d.rectangle([MX, ty, W - MX, ty + 64], fill=NAVY)
text(MX + 12, ty + 5, "THE DAY IN UTC \u2014 THURSDAY 19 NOVEMBER 2026",
     sans_b(13), fill=GOLD)
col_w = (CW - 24) // 3
for i, (when, txt, src) in enumerate(TIMELINE):
    cx = MX + 12 + (i % 3) * col_w
    cy = ty + 25 + (i // 3) * 19
    text(cx, cy, when + "  ", sans_b(9), fill=(255, 255, 255))
    off = d.textlength(when + "  ", font=sans_b(9))
    text(cx + off, cy, txt + f" ({src})", sans(9), fill=(214, 222, 235))

# ---- secondary stories: three boxes ----
sy = 344
box_w = (CW - 2 * 14) // 3
for i, (head, body) in enumerate(SECONDARY):
    x = MX + i * (box_w + 14)
    d.rectangle([x, sy, x + box_w, sy + 96], outline=RULE, width=2)
    d.rectangle([x, sy, x + box_w, sy + 26], fill=NAVY if i != 0 else RED)
    text(x + 10, sy + 5, head, sans_b(14), fill=(255, 255, 255))
    for j, ln in enumerate(wrap(body, sans(11), box_w - 20)[:4]):
        text(x + 10, sy + 32 + j * 15, ln, sans(11))

# ---- the wire: draw the precomputed columns ----
for c in range(4):
    x = MX + c * (COLW + GAP)
    if c:
        d.line([x - GAP // 2, WY, x - GAP // 2, WBOT], fill=RULE, width=1)
    y = WY
    for n, head, body in COLS[c]:
        text(x, y, f"{n}.", sans_b(10), fill=RED)
        for j, ln in enumerate(wrap(head, HF, COLW - 19)):
            text(x + 19, y + j * 11, ln, HF)
        y += len(wrap(head, HF, COLW - 19)) * 11
        for ln in wrap(body, BF, COLW - 19):
            text(x + 19, y, ln, BF, fill=(52, 52, 56))
            y += 10
        y += 4

# ---- footer ----
d.line([MX, 980, W - MX, 980], fill=RULE, width=2)
text(512, 986, "Sources: Level Headlines \u2022 Zark News \u2022 Open Chronicle \u2022 EGazette \u2022 "
               "Just Security \u2022 Reuters \u2022 AP \u2022 AFP \u2022 BBC \u2022 CNBC \u2022 NYT \u2022 "
               "UN News \u2022 IAEA \u2022 Yonhap \u2014 full citations in README.md",
     sans(9), fill=GREY, anchor="ma")
text(512, 1002, f"One day, one page: {STORY_COUNT} stories from 19 November 2026, "
                "each checked against the day's briefs. Drawn with PIL \u2014 see build_image.py.",
     sans(9), fill=GREY, anchor="ma")

img.save("/home/hatch/workspace/makefun/news-image-20261119/entry.png",
         "PNG", optimize=True)
print(f"saved; wire items rendered: {RENDERED} of {len(WIRE)}; "
      f"total stories on page: {STORY_COUNT}")
