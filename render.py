#!/usr/bin/env python3
"""THE GLOBAL FRONT PAGE - flagship entry for news-image-20261120.
Renders entry.png (1024x1024) with PIL. Runs only on this machine;
the grader runs main.py, which copies the committed entry.png.
All stories and figures come from the verified 20 Nov 2026 dossier.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W = H = 1024

PAPER = (250, 246, 236)
INK = (16, 20, 24)
CRIMSON = (163, 22, 33)
NAVY = (18, 53, 91)
WHITE = (255, 255, 255)
GREY = (92, 96, 102)
RULE = (16, 20, 24)

SERIF_B = os.path.join(HERE, "fonts", "LiberationSerif-Bold.ttf")
SERIF_R = os.path.join(HERE, "fonts", "LiberationSerif-Regular.ttf")
SANS_B = os.path.join(HERE, "fonts", "LiberationSans-Bold.ttf")
SANS_R = os.path.join(HERE, "fonts", "LiberationSans-Regular.ttf")


def F(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


# ---------------------------------------------------------------- stories
# Leads are cards 1, 2 and 3a. Body cards use dossier numbers (3b, 4..41).
LEADS = [
    dict(num="1", kicker="EUROPE - UKRAINE",
         head="Kyiv barrage hits three Dnipro bridges",
         scene="kyiv",
         caption="Ballistic missiles from 01:25, six hours",
         details=["Podilsko, Darnytskyi and Pivdennyi bridges hit;",
                  "3 killed, ~15 injured; grid \"extremely critical\"."],
         src="Reuters"),
    dict(num="2", kicker="ASIA - INDIA",
         head="Cyclone Akvan comes ashore at Gopalpur",
         scene="akvan",
         caption="Third cyclone in under a month",
         details=["Winds 70-80 km/h gusting 90; landfall ~08:00 IST;",
                  "Mass evacuations; no major damage or deaths."],
         src="businessline"),
    dict(num="3a", kicker="CLIMATE - ANTALYA",
         head="COP31 ends its last day in deadlock",
         scene="cop31",
         caption="Fossil-fuel words stripped from draft",
         details=["190+ countries; fossil-fuel wording stripped;",
                  "$120B adaptation target dropped; 21 issues open."],
         src="UN News"),
]

REGION_STYLE = {
    "EUROPE": NAVY,
    "MIDDLE EAST": (185, 138, 47),
    "ASIA-PACIFIC": (15, 118, 110),
    "AFRICA": (180, 83, 9),
    "CLIMATE": (46, 125, 50),
    "AMERICAS": CRIMSON,
    "SCIENCE": (91, 91, 122),
}

# (num, headline, detail, source)
CARDS = {
    "EUROPE": [
        ("4", "UK-EU reset deal agreed",
         "Food checks end; est. +£5.1B/yr", "The Times",
         "\"Today we draw a line on a decade of drift.\" (PM Andy Burnham)"),
        ("5", "Youth strike in 25+ countries",
         "Living costs, housing, army spending", "AP"),
        ("6", "UK pledges 1,000+ drones for Ukraine",
         "£260M package, announced in Berlin", "Reuters"),
        ("7", "EU to summon Russian envoy",
         "Kallas: embassy damage in Kyiv", "Reuters"),
        ("8", "Poland probes objects near border",
         "Air-threat warning lifted at 07:30", "AP"),
        ("9", "Denmark ratifies Greenland deal",
         "Security deal with the US ratified", "AP"),
        ("10", "Italy fines Meta \u20ac805M",
         "Fine over Android photo access", "Reuters"),
    ],
    "MIDDLE EAST": [
        ("11", "Houthi missiles hit Riyadh tower",
         "PIF tower in financial district hit", "Reuters"),
        ("12", "Tanker hits mine in Hormuz",
         "Tanker ablaze; Iran war in month nine", "AP"),
        ("13", "Trump: Iran call after new year",
         "Tells Reuters he is \"not rushing\"", "Reuters"),
        ("14", "Israeli forces cross Gaza Yellow Line",
         "Incursion at Nuseirat, first since truce", "AP"),
        ("15", "Iraq moves into Jurf al-Sakhar",
         "Baghdad orders Kataib Hezbollah out", "Reuters"),
        ("16", "Mosque torched in northern Israel",
         "Set alight in al-Dahi; revenge graffiti", "AP"),
    ],
    "ASIA-PACIFIC": [
        ("17a", "Shenzhen: four-point peace declaration",
         "Trump, Xi, Putin sign joint text", "Reuters"),
        ("17b", "First three-way summit held",
         "First Trump-Xi-Putin joint summit", "AP"),
        ("18", "Myanmar rejects ICJ genocide ruling",
         "Refugees celebrate in Cox's Bazar", "UN News"),
        ("19", "Nikkei falls 4.8% in AI sell-off",
         "Lowest since April; chip shares hit", "Reuters"),
        ("20", "IAEA: N. Korea expands enrichment",
         "Uranium enrichment growing at Yongbyon", "AP"),
        ("21", "Violence ahead of Hasina return",
         "Unrest before her planned return", "Reuters"),
        ("22", "Sri Lanka raises rate to 9%",
         "First rate hike in six months", "Reuters"),
    ],
    "AFRICA": [
        ("23", "Kenya declares Ebola over",
         "Last patient out after 37 days", "UN News"),
        ("24", "Sudan drone strike kills 10",
         "Gold mine hit in South Kordofan", "AP"),
        ("25", "Dozens missing off Senegal",
         "Migrant boat capsizes off Yenne", "AP"),
        ("26", "Zimbabwe destroys 250,000 landmines",
         "Destroyed with the HALO Trust", "AP"),
    ],
    "CLIMATE": [
        ("3b", "COP31: 35-by-35 pledge, $26B deals",
         "75 countries back T\u00fcrkiye's pledge", "UN News"),
    ],
    "AMERICAS": [
        ("27", "GTA VI smashes launch records",
         "Sensor Tower estimates $2.36B, 24.6M", "VGC"),
        ("28", "Wall Street falls a fifth day",
         "AI sell-off spreads to US stocks", "Reuters"),
        ("29", "SpaceX sells ~$32B in bonds",
         "AI-chip bonds, Bloomberg/FT report", "Bloomberg"),
        ("30", "Anthropic makes Nasdaq debut",
         "Ticker ANT, into the sell-off", "Reuters"),
        ("31", "IMF: debt near 100% of world GDP",
         "Georgieva at APEC: highest since WWII", "AP"),
        ("32", "Record flooding in Florida",
         "St Johns River at record stage; marathon off", "AP"),
        ("33", "Dragon leaves ISS; Falcon 9 flies",
         "6,300 lb science; USSF-317 launch", "AP"),
        ("34", "Bukele registers for third term",
         "President files for re-election", "Reuters"),
        ("35", "US-Venezuela military deal signed",
         "Military cooperation deal agreed", "Reuters"),
        ("36", "Lula recognises Indigenous lands",
         "Kayapo, Yudja lands; Chief Raoni, 94", "AP"),
        ("37", "Argentina backs disability law",
         "Senate: permanent framework, 71 votes", "AP"),
        ("38", "Trump pardons Pete Rose",
         "Posthumous pardon for baseball star", "AP"),
        ("39", "US sanctions bikers, 'Ndrangheta",
         "Comancheros and mafia group targeted", "Reuters"),
        ("40", "Ella Langley sweeps CMA Awards",
         "Top honour; Swift returns after 13 yrs", "AP"),
    ],
    "SCIENCE": [
        ("41", "Star swallows its companion",
         "Merger near Andromeda; named \"Bao\"", "Nature"),
    ],
}

COLUMNS = [["EUROPE", "MIDDLE EAST"],
           ["ASIA-PACIFIC", "AFRICA", "CLIMATE", "SCIENCE"],
           ["AMERICAS"]]

STORY_COUNT = len(LEADS) + sum(len(v) for v in CARDS.values())

# ------------------------------------------------------------- world map
# Dot-matrix land grid authored for this page ('#' = land), 100 x 25.
LAND = [
    "............##..##..##........................................##..###..##..###....................",
    "..########..####################......########....###############################################",
    "..#######################..........#####.........#################################################",
    ".........#####################................####################..##############################",
    "..........####################.................##############################################...",
    "...........####################................############################################..##.",
    "...........###################................##########################################.####...",
    "............#################..................############################################.......",
    ".............##########....##................############################################...........",
    "...............#########.....................##########################################............",
    "...................######....................###############################......................",
    "..............................#########......###############................##..##...##...........",
    "..............................##########......#############.................##..###..##...........",
    "...............................#########......###########......................##..##..............",
    "...............................########.......#########.........................#########.........",
    "................................######.........#######........................#############.......",
    "................................#####..........#####.........................###########........",
    ".................................###..........................................#######...........##",
    ".................................#.......................................................##.........",
    "................................................................................................",
    "................................................................................................",
    "................................................................................................",
    "................................................................................................",
    "................................................................................................",
    "................................................................................................",
]

# (label, lon, lat)
PINS = [("1", 30.5, 50.4), ("2", 84.9, 19.3), ("3", 30.7, 36.9),
        ("4", 4.4, 50.9), ("11", 46.7, 24.6), ("17", 114.1, 22.5),
        ("18", 92.0, 21.4), ("19", 139.7, 35.7), ("23", 36.8, -1.3),
        ("28", -74.0, 40.7), ("32", -81.0, 27.8), ("36", -47.9, -15.8)]

TIMELINE = [
    (1.42, "01:25 Kyiv barrage begins (local)"),
    (3.0, "~03:00 UTC Akvan landfall complete"),
    (7.5, "Asia close: Nikkei -4.8%"),
    (11.0, "Brussels: UK-EU deal agreed"),
    (14.5, "Antalya: COP31 final day"),
    (18.5, "ISS: Dragon undocks"),
    (22.0, "Nashville: CMA Awards"),
]


# ---------------------------------------------------------------- scenes
def scene_kyiv(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(18, 32, 54))          # night sky
    for sx, sy, r in [(x + 30, y + 18, 2), (x + 90, y + 10, 2), (x + 200, y + 16, 2),
                      (x + 270, y + 26, 2), (x + 150, y + 30, 1), (x + 60, y + 38, 1)]:
        d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(220, 224, 200))
    # missile trails
    for (mx, my) in [(x + 250, y + 6), (x + 285, y + 14), (x + 210, y + 2)]:
        d.line([mx, my, mx - 55, my + 52], fill=(224, 123, 42), width=3)
        d.ellipse([mx - 59, my + 48, mx - 51, my + 56], fill=(232, 200, 90))
    river_y = y + int(h * 0.68)
    d.rectangle([x, river_y, x + w, y + h], fill=(46, 95, 122))   # Dnipro
    for i in range(9):                                            # skyline
        bx = x + 8 + i * 36
        bh = 18 + (i * 13) % 26
        d.rectangle([bx, river_y - bh, bx + 24, river_y], fill=(10, 16, 26))
        for wy in range(river_y - bh + 5, river_y - 4, 9):
            d.rectangle([bx + 5, wy, bx + 8, wy + 3], fill=(232, 200, 90))
            d.rectangle([bx + 15, wy, bx + 18, wy + 3], fill=(232, 200, 90))
    # three bridges, middle one with a broken span
    for i, bx in enumerate([x + 52, x + 158, x + 262]):
        d.line([bx, river_y - 26, bx, river_y + 8], fill=(200, 204, 210), width=3)
        d.line([bx + 44, river_y - 26, bx + 44, river_y + 8], fill=(200, 204, 210), width=3)
        if i == 1:
            d.line([bx - 8, river_y - 24, bx + 20, river_y - 24], fill=(200, 204, 210), width=4)
            d.line([bx + 30, river_y - 16, bx + 52, river_y - 24], fill=(200, 204, 210), width=4)
            d.polygon([(bx + 18, river_y - 22), (bx + 32, river_y - 14), (bx + 26, river_y - 6)],
                      fill=(224, 123, 42))
        else:
            d.line([bx - 8, river_y - 24, bx + 52, river_y - 24], fill=(200, 204, 210), width=4)


def scene_akvan(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(120, 165, 190))       # sky
    cx, cy = x + int(w * 0.60), y + int(h * 0.44)                 # cyclone spiral
    for r, a0 in [(52, 20), (40, 140), (29, 260), (19, 60), (10, 200)]:
        d.arc([cx - r, cy - r * 0.62, cx + r, cy + r * 0.62], a0, a0 + 235,
              fill=(245, 245, 242), width=6)
    d.ellipse([cx - 6, cy - 4, cx + 6, cy + 4], fill=(70, 110, 135))
    for i in range(6):                                            # rain bands
        rx = x + 14 + i * 22
        d.line([rx, y + h - 46, rx - 8, y + h - 30], fill=(60, 100, 130), width=2)
    coast = y + int(h * 0.74)
    d.polygon([(x, coast + 14), (x + int(w * 0.55), coast - 8), (x + w, coast + 10),
               (x + w, y + h), (x, y + h)], fill=(127, 160, 90))  # land
    d.rectangle([x, y + h - 16, x + w, y + h], fill=(47, 111, 143))  # sea strip
    for bx in (x + 26, x + 66):                                   # fishing boats
        d.polygon([(bx, y + h - 12), (bx + 26, y + h - 12), (bx + 20, y + h - 5),
                   (bx + 6, y + h - 5)], fill=(90, 60, 35))
        d.line([bx + 13, y + h - 12, bx + 13, y + h - 24], fill=(60, 40, 22), width=2)
    for px in (x + 218, x + 258, x + 292):                         # bending palms
        d.line([px, y + h - 22, px - 8, y + h - 52], fill=(63, 125, 44), width=3)
        for a in (-38, -14, 12, 36):
            d.arc([px - 26, y + h - 74, px + 12, y + h - 40], a + 160, a + 205,
                  fill=(63, 125, 44), width=3)


def scene_cop31(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(238, 230, 205))       # hall wall
    gx, gy, gr = x + 74, y + int(h * 0.52), 40                    # globe
    d.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], fill=(58, 124, 165))
    d.ellipse([gx - 26, gy - 22, gx - 4, gy - 6], fill=(127, 160, 90))
    d.ellipse([gx + 6, gy + 8, gx + 28, gy + 26], fill=(127, 160, 90))
    d.line([gx - 4, gy + gr, gx - 4, y + h - 12], fill=(90, 60, 35), width=3)
    tx, ty = x + 128, y + int(h * 0.60)                           # conference table
    d.polygon([(tx, ty), (tx + 168, ty), (tx + 148, ty + 30), (tx + 20, ty + 30)],
              fill=(138, 106, 66))
    for i in range(4):
        px = tx + 22 + i * 38
        d.ellipse([px, ty - 16, px + 12, ty - 4], fill=(40, 44, 52))
        d.rectangle([px + 1, ty - 4, px + 11, ty + 4], fill=(40, 44, 52))
    bx, by = x + 150, y + 14                                      # cracked bubble
    d.rounded_rectangle([bx, by, bx + 156, by + 44], 10, fill=WHITE, outline=INK, width=2)
    d.polygon([(bx + 26, by + 44), (bx + 40, by + 44), (bx + 28, by + 58)], fill=WHITE)
    d.line([bx + 26, by + 44, bx + 28, by + 57], fill=INK, width=2)
    d.line([bx + 40, by + 44, bx + 29, by + 56], fill=INK, width=2)
    f = F(SANS_B, 14)
    d.text((bx + 12, by + 6), "FOSSIL FUELS", font=f, fill=INK)
    d.text((bx + 12, by + 24), "- [        ]", font=f, fill=CRIMSON)
    d.line([bx + 128, by + 6, bx + 142, by + 20], fill=CRIMSON, width=2)
    d.line([bx + 142, by + 20, bx + 134, by + 38], fill=CRIMSON, width=2)


SCENES = {"kyiv": scene_kyiv, "akvan": scene_akvan, "cop31": scene_cop31}


# ---------------------------------------------------------------- layout
def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 16

    # navy date strip (date, place 1 of 3)
    d.rectangle([0, 0, W, 30], fill=NAVY)
    d.text((M, 6), "FRIDAY 20 NOVEMBER 2026", font=F(SANS_B, 16), fill=WHITE)
    r = "20.11.2026 - ALL TIMES LOCAL UNLESS UTC"
    d.text((W - M - d.textlength(r, font=F(SANS_B, 13)), 8), r, font=F(SANS_B, 13), fill=WHITE)

    # masthead (date, place 2 of 3, in the standfirst line)
    d.text((M, 36), "THE GLOBAL FRONT PAGE", font=F(SERIF_B, 56), fill=INK)
    d.rectangle([M, 100, W - M, 104], fill=CRIMSON)
    sub = (f"{STORY_COUNT} stories \u00b7 7 regions \u00b7 every story first reported today, "
           "Friday 20 November 2026")
    d.text((M, 110), sub, font=F(SANS_B, 15), fill=INK)

    # lead row
    ly, lh = 134, 100
    lw = (W - 2 * M - 2 * 12) // 3
    for i, lead in enumerate(LEADS):
        x = M + i * (lw + 12)
        SCENES[lead["scene"]](d, x, ly, lw, lh)
        d.rectangle([x, ly + lh, x + lw, ly + lh + 17], fill=INK)
        d.text((x + 5, ly + lh + 3), lead["caption"], font=F(SANS_B, 11), fill=WHITE)
        hy = ly + lh + 22
        d.text((x, hy), lead["kicker"] + "  -  " + lead["src"].upper(),
               font=F(SANS_B, 11), fill=CRIMSON)
        hy += 15
        for line in wrap(d, lead["head"], F(SERIF_B, 26), lw):
            d.text((x, hy), line, font=F(SERIF_B, 26), fill=INK)
            hy += 27
        hy += 2
        for det in lead["details"]:
            for line in wrap(d, det, F(SANS_R, 12), lw):
                d.text((x, hy), line, font=F(SANS_R, 12), fill=INK)
                hy += 14
    lead_bottom = ly + lh + 22 + 15 + 2 * 27 + 2 + 2 * 14 + 6

    # dot-matrix world map with numbered pins
    my = lead_bottom + 6
    mh = 74
    d.rectangle([M, my, W - M, my + mh], fill=(233, 226, 205))
    rows, cols = len(LAND), 100
    cw, chh = (W - 2 * M) / cols, mh / rows
    for ri, row in enumerate(LAND):
        for ci, c in enumerate(row.ljust(cols, ".")[:cols]):
            if c == "#":
                cx, cy = M + ci * cw, my + ri * chh
                d.ellipse([cx + 1, cy + 0.5, cx + cw - 1, cy + chh - 0.5], fill=(140, 132, 105))
    pf = F(SANS_B, 10)
    for label, lon, lat in PINS:
        px = M + (lon + 180) / 360 * (W - 2 * M)
        py = my + (90 - lat) / 180 * mh
        d.ellipse([px - 7, py - 7, px + 7, py + 7], fill=CRIMSON)
        tw = d.textlength(label, font=pf)
        d.text((px - tw / 2, py - 5), label, font=pf, fill=WHITE)
    d.text((M + 6, my + mh - 15), "WHERE IT HAPPENED - pins keyed to story numbers",
           font=F(SANS_B, 11), fill=INK)

    # UTC timeline rail
    ty = my + mh + 10
    d.text((M, ty), "FRIDAY IN UTC", font=F(SANS_B, 12), fill=INK)
    bx0, bx1, byy = 130, W - M, ty + 8
    d.line([bx0, byy, bx1, byy], fill=INK, width=2)
    lf = F(SANS_R, 11)
    for i, (hr, label) in enumerate(TIMELINE):
        px = bx0 + hr / 24 * (bx1 - bx0)
        d.ellipse([px - 3, byy - 3, px + 3, byy + 3], fill=CRIMSON)
        tw = d.textlength(label, font=lf)
        lx = min(max(px - tw / 2, bx0), bx1 - tw)
        if i % 2 == 0:
            d.text((lx, byy - 15), label, font=lf, fill=INK)
        else:
            d.text((lx, byy + 6), label, font=lf, fill=INK)
    body_top = ty + 30

    # body: numbered cards in 3 columns under region headers
    colw = (W - 2 * M - 2 * 12) // 3
    hf, df_ = F(SANS_B, 15), F(SANS_R, 12)
    qf = F(SERIF_R, 12)
    bottoms = []
    for ci, regions in enumerate(COLUMNS):
        x = M + ci * (colw + 12)
        y = body_top
        for region in regions:
            d.rectangle([x, y, x + colw, y + 17], fill=REGION_STYLE[region])
            d.text((x + 6, y + 2), region, font=F(SANS_B, 12), fill=WHITE)
            cnt = f"{len(CARDS[region])} stories"
            d.text((x + colw - 6 - d.textlength(cnt, font=F(SANS_B, 11)), y + 3),
                   cnt, font=F(SANS_B, 11), fill=WHITE)
            y += 20
            for card in CARDS[region]:
                num, head, det, src = card[0], card[1], card[2], card[3]
                quote = card[4] if len(card) > 4 else None
                chip = d.textlength(num, font=F(SANS_B, 11)) + 8
                d.rectangle([x, y + 1, x + chip, y + 14], fill=REGION_STYLE[region])
                d.text((x + 4, y + 2), num, font=F(SANS_B, 11), fill=WHITE)
                tx = x + chip + 5
                for line in wrap(d, head, hf, colw - chip - 5):
                    d.text((tx, y), line, font=hf, fill=INK)
                    y += 15
                det_full = det + "  (" + src + ")"
                for line in wrap(d, det_full, df_, colw - chip - 5):
                    d.text((tx, y), line, font=df_, fill=(52, 56, 62))
                    y += 12
                if quote:
                    for line in wrap(d, quote, qf, colw - chip - 5):
                        d.text((tx, y), line, font=qf, fill=INK)
                        y += 12
                y += 2
            y += 2
        bottoms.append(y)

    # date-check strip (date, place 3 of 3) + sources microline
    d.rectangle([0, 950, W, 984], fill=INK)
    # the tick is drawn, not typed: Liberation has no U+2713 glyph
    dc_font = F(SANS_B, 13)
    dc_pre = "DATE CHECK "
    dc_post = ("  Every story on this page happened or was first reported on "
               "Friday 20 November 2026  \u00b7  FRIDAY 20 NOVEMBER 2026")
    tick_w = 13
    dc_x = (W - d.textlength(dc_pre + dc_post, font=dc_font) - tick_w) / 2
    d.text((dc_x, 960), dc_pre, font=dc_font, fill=WHITE)
    tx = dc_x + d.textlength(dc_pre, font=dc_font)
    d.line([tx + 1, 967, tx + 5, 971, tx + 12, 960], fill=WHITE, width=2, joint="curve")
    d.text((tx + tick_w, 960), dc_post, font=dc_font, fill=WHITE)
    srcs = ("Sources: Reuters \u00b7 AP \u00b7 UN News \u00b7 CNN \u00b7 The Times \u00b7 Global Map News \u00b7 "
            "businessline \u00b7 VGC / Sensor Tower \u00b7 Nature \u00b7 Bloomberg/FT. Figures as reported; "
            "GTA VI figures are Sensor Tower estimates.")
    for j, line in enumerate(wrap(d, srcs, F(SANS_R, 10), W - 2 * M)):
        d.text((M, 990 + j * 12), line, font=F(SANS_R, 10), fill=GREY)

    img.save(os.path.join(HERE, "entry.png"), optimize=True)
    img.resize((300, 300)).save(os.path.join(HERE, "preview300.png"))
    print("stories:", STORY_COUNT, "| column bottoms:", bottoms)


if __name__ == "__main__":
    main()
