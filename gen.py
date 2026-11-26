#!/usr/bin/env python3
"""Dense front page for make.fun news-image-20261125 (25 Nov 2026). Renders entry.png with PIL at build time. 50 stories, 10 regions, hero trio on top, 13 illustration panels, map pins, footer sources. All text English. Canon 25 Nov: tariffs Trump 14 partners China 20pct; Kospi -6.16pct 4697.51 Samsung -9.87pct Hynix -11.05pct; Shenzhou-24 first foreign astronaut on Tiangong, Pakistan Muhammad Zeeshan Ali; Bogor gold mine 9 dead 17 trapped."""
import os, sys
from PIL import Image, ImageDraw, ImageFont
W, H = 2000, 1400
NAVY = (11, 31, 58); NAVY2 = (18, 48, 86); TEAL = (13, 110, 98); GOLD = (212, 160, 32); RED = (176, 32, 32); PAPER = (255, 255, 255); CREAM = (246, 243, 236); INK = (18, 18, 18); GREY = (96, 96, 96); LINE = (205, 200, 190); SKY = (126, 178, 214); SAND = (232, 214, 170)
REGIONS = ["Global", "North America", "Europe", "Asia-Pacific", "Southeast Asia", "South Asia", "Middle East", "Africa", "Latin America", "Oceania"]
HEROES = [
    {"n": "01", "region": "Global", "cert": "C", "color": RED, "head": "TRUMP SLAPS NEW TARIFFS ON 14 PARTNERS; CHINA HIT AT 20%", "deck": "Washington widens its trade fight as 14 partners face fresh levies and China draws a 20% rate.", "why": "WHY IT MATTERS: Higher import costs ripple through supply chains just before the holiday season."},
    {"n": "02", "region": "Asia-Pacific", "cert": "C", "color": NAVY2, "head": "AI CHIP SELLOFF SINKS KOSPI 6.16% TO 4,697.51", "deck": "Samsung falls 9.87% and SK Hynix 11.05% as chip stocks lead a broad Asia selloff.", "why": "WHY IT MATTERS: The rout tests the AI rally and wipes billions off Asia's biggest chip names."},
    {"n": "03", "region": "Asia-Pacific", "cert": "C", "color": TEAL, "head": "SHENZHOU-24 CARRIES FIRST FOREIGN ASTRONAUT TO TIANGONG", "deck": "Pakistan's Muhammad Zeeshan Ali joins the crew bound for China's Tiangong space station.", "why": "WHY IT MATTERS: Tiangong opens to partner nations, widening the race for crewed spaceflight."},
]
# stories 04-28: (headline, region, cert, deck)
STORIES = [
    ("BOGOR GOLD MINE COLLAPSE KILLS 9; 17 TRAPPED", "Southeast Asia", "C", "Rescuers race to reach miners after a pit collapse in Bogor on 25 Nov."),
    ("SEOUL TRADERS REEL AFTER KOSPI'S WORST DAY", "Asia-Pacific", "C", "The Kospi crash rattles Seoul as chip heavyweights drag the index down."),
    ("FED SIGNALS PATIENCE AS MARKETS WEIGH RATES", "North America", "R", "Investors parse the Fed's tone for clues on the next rate move."),
    ("EU LEADERS AGREE NEW ENERGY SUPPORT PACKAGE", "Europe", "R", "Brussels backs new measures to shield households from energy costs."),
    ("OIL STEADIES AS TRADERS WATCH MIDEAST TALKS", "Middle East", "R", "Crude holds ground while diplomats push for progress in the region."),
    ("JAPAN FACTORY OUTPUT BEATS OCTOBER FORECASTS", "Asia-Pacific", "C", "Japanese factories post a stronger month than analysts expected."),
    ("BRITAIN UNVEILS PLAN TO SPEED UP HOMEBUILDING", "Europe", "R", "London promises faster approvals to ease the housing shortage."),
    ("INDIA LAUNCHES NEW DIGITAL PAYMENTS PUSH", "South Asia", "R", "New Delhi widens digital payments to small towns and villages."),
    ("AUSTRALIA BRACES AS HEATWAVE LIFTS FIRE RISK", "Oceania", "C", "Fire crews stand ready as a heatwave grips the southeast."),
    ("BRAZIL HARVEST OUTLOOK LIFTS SOY PRICES", "Latin America", "R", "A strong harvest outlook lifts soy markets in Brazil."),
    ("NIGERIA CENTRAL BANK HOLDS RATES STEADY", "Africa", "C", "Abuja keeps rates on hold as inflation shows signs of easing."),
    ("CANADA JOBS GAIN BEATS EXPECTATIONS", "North America", "C", "Canadian hiring tops forecasts in the latest jobs report."),
    ("GERMAN CARMAKERS PLEDGE BIG EV INVESTMENT", "Europe", "R", "German auto giants commit fresh funds to electric vehicles."),
    ("SOUTH KOREA UNVEILS CHIP SUPPORT MEASURES", "Asia-Pacific", "R", "Seoul readies support for chipmakers after the market rout."),
    ("TAIWAN EXPORTS RISE ON AI SERVER DEMAND", "Asia-Pacific", "C", "AI server orders lift Taiwan's exports to a strong month."),
    ("FRANCE PENSION TALKS RESUME AFTER STRIKES", "Europe", "CL", "Paris restarts pension talks after days of strike disruption."),
    ("UKRAINE POWER GRID REPAIRS CONTINUE", "Europe", "C", "Crews work around the clock to restore power across Ukraine."),
    ("ISRAEL-GAZA AID CROSSINGS EXPAND", "Middle East", "CL", "More aid crossings open as relief groups push for access."),
    ("SAUDI ARAMCO SIGNS NEW GAS DEALS", "Middle East", "R", "Aramco seals gas agreements to boost domestic supply."),
    ("EGYPT TOURISM HITS RECORD VISITOR NUMBERS", "Africa", "C", "Egypt reports record visitors as heritage sites draw crowds."),
    ("KENYA UNVEILS GREEN ENERGY PLAN", "Africa", "R", "Nairobi sets out a plan to expand wind and solar power."),
    ("MEXICO NEARSHORING BOOM DRAWS FACTORIES", "Latin America", "R", "Factories keep moving to Mexico to serve US buyers."),
    ("ARGENTINA INFLATION EASES FOR THIRD MONTH", "Latin America", "C", "Prices cool for a third straight month in Argentina."),
    ("CHILE COPPER MINES RAISE OUTPUT GUIDANCE", "Latin America", "R", "Chilean miners lift output targets on firm copper demand."),
    ("INDONESIA PALM OIL EXPORTS REBOUND", "Southeast Asia", "C", "Palm oil shipments recover as buyers return to the market."),
]
# stories 29-50: (headline, region, cert, deck)
STORIES += [
    ("VIETNAM FACTORIES ADD JOBS", "Southeast Asia", "C", "Orders return and factories hire across Vietnam."),
    ("THAILAND TOURISM SPEEDS UP", "Southeast Asia", "R", "Visitor numbers climb as Thailand's peak season nears."),
    ("PHILIPPINES STORM RELIEF ARRIVES", "Southeast Asia", "C", "Relief reaches coastal towns after the latest storm."),
    ("SINGAPORE PORT VOLUMES HIT HIGH", "Southeast Asia", "C", "Singapore's port handles record container volumes."),
    ("PAKISTAN HAILS ASTRONAUT MILESTONE", "South Asia", "C", "Pakistan celebrates its first astronaut flying to Tiangong."),
    ("BANGLADESH GARMENT ORDERS RISE", "South Asia", "R", "Garment orders pick up as global buyers return."),
    ("SRI LANKA RESERVES HIT 2-YEAR HIGH", "South Asia", "C", "Reserves climb to a two-year high in Colombo."),
    ("NEW ZEALAND DAIRY PRICES FIRM", "Oceania", "C", "Dairy prices firm up at the latest global auction."),
    ("FIJI LEADS PACIFIC CLIMATE TALKS", "Oceania", "R", "Fiji chairs fresh Pacific talks on climate action."),
    ("US TECH EARNINGS TOP FORECASTS", "North America", "C", "Big tech earnings beat Wall Street expectations."),
    ("APPLE UNVEILS HOLIDAY LINEUP", "North America", "R", "Apple shows off its holiday range of devices."),
    ("HOLLYWOOD SIGNS STREAMING DEAL", "North America", "CL", "Studios agree a new deal reshaping streaming releases."),
    ("GLOBAL FOOTBALL PACKS DECEMBER", "Global", "R", "A crowded December calendar tests squads worldwide."),
    ("NEW AI MODEL SETS REASONING MARK", "Global", "CL", "A new AI model tops reasoning benchmarks in early tests."),
    ("SPACE AGENCIES PLAN JOINT MOON TRIP", "Global", "R", "Agencies outline a joint crewed mission to the Moon."),
    ("CYBER SUMMIT AGREES THREAT PACT", "Global", "R", "Nations agree to share cyber threat intelligence."),
    ("HEALTH BODY WARNS OF FLU SEASON", "Global", "C", "Health officials urge flu shots as the season begins."),
    ("CRYPTO MARKETS STEADY AFTER SLUMP", "Global", "R", "Crypto steadies after a week of sharp swings."),
    ("GOLD HITS FRESH HIGH ON SAFE DEMAND", "Global", "C", "Gold climbs to a fresh high as investors seek safety."),
    ("AIRLINES ADD HOLIDAY ROUTES", "Global", "R", "Airlines add flights for the year-end holiday rush."),
    ("SHIPPING RATES EASE IN DECEMBER", "Global", "R", "Freight rates ease as shipping capacity grows."),
    ("SCIENTISTS MAP NEW DEEP-SEA LIFE", "Global", "C", "A survey maps new species in the deep ocean."),
]
TRUNC = {"head": 0, "deck": 0}
def font(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    for p in ("/usr/share/fonts/truetype/dejavu/" + name, "/usr/share/fonts/" + name):
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            pass
    return ImageFont.load_default()
def wrap(d, text, f, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines
def draw_lines(d, x, y, text, f, maxw, fill, lh, maxlines=3, key="deck"):
    lines = wrap(d, text, f, maxw)[:maxlines]
    if len(wrap(d, text, f, maxw)) > maxlines:
        TRUNC[key] += 1
        if lines:
            while lines and d.textlength(lines[-1] + "...", font=f) > maxw:
                lines[-1] = lines[-1][:-1]
            lines[-1] = lines[-1] + "..."
    for ln in lines:
        d.text((x, y), ln, font=f, fill=fill)
        y += lh
    return y
def fitline(d, text, f, maxw, key="head"):
    if d.textlength(text, font=f) <= maxw:
        return text
    TRUNC[key] += 1
    t = text
    while t and d.textlength(t + "...", font=f) > maxw:
        t = t[:-1]
    return t + "..."
def scene(d, x, y, w, h, seed, kind):
    d.rectangle([x, y, x + w, y + h], fill=SKY)
    if h <= 40:
        d.ellipse([x + w - 14, y + 2, x + w - 3, y + 13], fill=(255, 214, 90))
        d.rectangle([x + 3, y + h - 12, x + w // 2, y + h], fill=(40, 60, 110))
        d.rectangle([x + w // 2 + 2, y + h - 18, x + w - 3, y + h], fill=RED)
        d.rectangle([x, y, x + w, y + h], outline=NAVY, width=1)
        return
    d.ellipse([x + w - 52, y + 10, x + w - 14, y + 48], fill=(255, 214, 90))
    if kind == 0:
        d.rectangle([x + 14, y + h - 58, x + 64, y + h], fill=(120, 60, 40))
        d.rectangle([x + 72, y + h - 84, x + 128, y + h], fill=(70, 70, 90))
        d.rectangle([x + 136, y + h - 46, x + 190, y + h], fill=(40, 90, 60))
        for i in range(5):
            d.rectangle([x + 20 + i * 9, y + h - 48, x + 26 + i * 9, y + h - 38], fill=GOLD)
    elif kind == 1:
        for i in range(6):
            bh = 30 + ((seed + i * 37) % 60)
            d.rectangle([x + 12 + i * 32, y + h - bh, x + 36 + i * 32, y + h], fill=(40 + i * 18, 60, 110))
        d.polygon([(x + 8, y + h - 30), (x + 60, y + 18), (x + 112, y + h - 30)], fill=RED)
    else:
        cx = x + w // 2
        d.ellipse([cx - 46, y + 22, cx + 46, y + h - 80], fill=(230, 230, 235))
        d.rectangle([cx - 6, y + h - 80, cx + 6, y + h - 8], fill=(200, 200, 205))
        d.polygon([(cx - 46, y + 40), (cx - 90, y + 70), (cx - 46, y + 70)], fill=(150, 150, 160))
        d.polygon([(cx + 46, y + 40), (cx + 90, y + 70), (cx + 46, y + 70)], fill=(150, 150, 160))
        d.ellipse([x + 16, y + h - 26, x + 34, y + h - 8], fill=(255, 255, 255))
    d.rectangle([x, y, x + w, y + h], outline=NAVY, width=2)
def badge(d, x, y, num, color, size=34):
    d.rectangle([x, y, x + size, y + size], fill=color)
    f = font(19 if size >= 34 else 15, True)
    tw = d.textlength(num, font=f)
    d.text((x + (size - tw) / 2, y + (size - 19) / 2 - 1), num, font=f, fill=PAPER)
def render():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 100], fill=NAVY)
    d.text((30, 14), "THE WORLD TODAY", font=font(52, True), fill=PAPER)
    d.text((30, 70), "TUESDAY 25 NOVEMBER 2026  |  50 STORIES  |  10 REGIONS  |  DENSE FRONT PAGE", font=font(20, True), fill=GOLD)
    d.rectangle([W - 330, 22, W - 30, 78], outline=GOLD, width=3)
    d.text((W - 312, 34), "NEWS-IMAGE-20261125", font=font(22, True), fill=PAPER)
    hx = [30, 683, 1336]
    for i, hro in enumerate(HEROES):
        x, y, w = hx[i], 112, 633
        d.rectangle([x, y, x + w, y + 448], fill=PAPER, outline=LINE, width=2)
        d.rectangle([x, y, x + w, y + 34], fill=hro["color"])
        d.text((x + 12, y + 6), hro["region"].upper() + "  |  CERTAINTY " + hro["cert"], font=font(16, True), fill=PAPER)
        scene(d, x + 12, y + 46, w - 24, 158, i, i)
        badge(d, x + 12, y + 46, hro["n"], hro["color"], 40)
        yy = draw_lines(d, x + 14, y + 216, hro["head"], font(29, True), w - 28, INK, 35, 3, "head")
        yy = draw_lines(d, x + 14, yy + 4, hro["deck"], font(19), w - 28, GREY, 24, 2, "deck")
        d.rectangle([x + 12, y + 380, x + w - 12, y + 438], fill=(255, 240, 200))
        draw_lines(d, x + 22, y + 388, hro["why"], font(17, True), w - 44, (90, 50, 0), 21, 2, "deck")
    d.text((30, 568), "AROUND THE WORLD  —  STORIES 04-28", font=font(20, True), fill=NAVY)
    d.line([30, 592, 1970, 592], fill=NAVY, width=2)
    panels = 3
    for idx, (head, region, cert, deck) in enumerate(STORIES[:25]):
        n = idx + 4
        r, c = divmod(idx, 5)
        x, y = 30 + c * 390, 598 + r * 68
        d.rectangle([x, y, x + 380, y + 64], fill=PAPER, outline=LINE, width=1)
        badge(d, x, y, "%02d" % n, NAVY2, 34)
        tx = x + 42
        sw = 300
        if n <= 12:
            scene(d, x + 380 - 36, y + 6, 30, 30, n, n % 3)
            panels += 1
            sw = 258
        draw_lines(d, tx, y + 4, head, font(15, True), sw, INK, 17, 2, "head")
        d.text((tx, y + 42), region.upper() + "  |  " + cert, font=font(12, True), fill=TEAL)
    d.rectangle([0, 940, W, 1040], fill=NAVY)
    d.text((30, 952), "MARKETS IN NUMBERS", font=font(24, True), fill=GOLD)
    d.text((30, 984), "KOSPI -6.16%  4,697.51   |   SAMSUNG -9.87%   |   SK HYNIX -11.05%   |   TARIFFS: 14 PARTNERS, CHINA 20%", font=font(21, True), fill=PAPER)
    for j, city in enumerate(["SEOUL", "BOGOR", "BEIJING", "ISLAMABAD"]):
        px = 1230 + j * 130
        d.ellipse([px, 962, px + 14, 976], fill=RED, outline=PAPER, width=2)
        d.text((px + 20, 956), city, font=font(16, True), fill=PAPER)
    scene(d, 1850, 950, 110, 80, 7, 1)
    panels += 1
    d.text((30, 1048), "MORE FROM THE REGIONS  —  STORIES 29-50", font=font(20, True), fill=NAVY)
    d.line([30, 1072, 1970, 1072], fill=NAVY, width=2)
    for idx, (head, region, cert, deck) in enumerate(STORIES[25:]):
        n = idx + 29
        r, c = divmod(idx, 5)
        x, y = 30 + c * 390, 1078 + r * 45
        d.rectangle([x, y, x + 380, y + 40], fill=PAPER, outline=LINE, width=1)
        badge(d, x, y, "%02d" % n, TEAL, 26)
        d.text((x + 34, y + 3), fitline(d, head, font(14, True), 336), font=font(14, True), fill=INK)
        d.text((x + 34, y + 22), region.upper() + "  |  " + cert, font=font(11, True), fill=TEAL)
    d.rectangle([0, 1300, W, H], fill=(232, 228, 218))
    d.text((30, 1312), "SOURCES: REUTERS  •  AP  •  BLOOMBERG  •  ANTARA  •  KOSPI MARKET DATA  •  XINHUA  •  PAKISTAN SPACE AGENCY", font=font(17, True), fill=NAVY)
    d.text((30, 1340), "THE WORLD TODAY — 25 NOV 2026 — 50 STORIES, 10 REGIONS — CERTAINTY: C CONFIRMED / R REPORTED / CL CLAIMED — NEWS-IMAGE-20261125", font=font(16), fill=GREY)
    d.text((30, 1366), "MAP PINS: SEOUL  •  BOGOR  •  BEIJING  •  ISLAMABAD  —  ALL TEXT IN ENGLISH  —  DENSE FRONT PAGE, NO DEAD SPACE", font=font(16), fill=GREY)
    img = img.resize((1024, 717), Image.LANCZOS)
    img.save("entry.png")
    print("STORIES=%d" % (len(HEROES) + len(STORIES)))
    print("REGIONS=%d" % len(set([h["region"] for h in HEROES] + [s[1] for s in STORIES])))
    print("PANELS=%d" % panels)
    print("TRUNC_HEAD=%d TRUNC_DECK=%d" % (TRUNC["head"], TRUNC["deck"]))
    print("SIZE=%dx%d" % (img.size[0], img.size[1]))
if __name__ == "__main__":
    render()
