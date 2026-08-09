#!/usr/bin/env python3
"""Generate four candidate header/footer SVGs for the profile README.

Motion is expressed as CSS animations inside the SVG's own <style> block rather
than SMIL, so a `prefers-reduced-motion` media query can switch it all off.
Every loop returns to its exact starting state, so there is no snap on repeat.
"""
import math
import os

W, H = 1200, 180
NAME = "Oluwatobi Wilfred Ojulari"
DESC = "Bioinformatics Data Engineer  ·  Full-Stack Developer"

DEEP, CYAN, GREEN = "#0B4F6C", "#01BAEF", "#20BF55"
AMBER = "#F4A259"

THEMES = {
    "dark": dict(bg="#0d1117", ink="#ffffff", sub="#c9d7e4", veil=0.0),
    "light": dict(bg="#ffffff", ink="#0B4F6C", sub="#33566b", veil=0.10),
}

FONT = ("-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,"
        "sans-serif")

REDUCED = """
    @media (prefers-reduced-motion: reduce) {
      * { animation: none !important; }
    }"""


def titles(t, y1=88, y2=118, align=600):
    """Shared name + tagline block."""
    return f"""
  <text class="nm" x="{align}" y="{y1}" text-anchor="middle">{NAME}</text>
  <text class="ds" x="{align}" y="{y2}" text-anchor="middle">{DESC}</text>"""


def base_style(t, extra=""):
    # No entrance animation on the title block — the name and tagline are
    # painted at full opacity on first frame. Only the background trace moves.
    return f"""
    .nm {{ font: 700 40px {FONT}; fill: {t['ink']}; letter-spacing: .2px; }}
    .ds {{ font: 500 17px {FONT}; fill: {t['sub']}; }}
    {extra}
    {REDUCED}"""


# ───────────────────────────── 1. aurora ─────────────────────────────
def aurora(t, footer=False):
    h = 120 if footer else H
    blobs = [
        # cx,  cy,   rx,  ry, color, dur, dx, dy, opacity
        (250, 60, 520, 200, CYAN, 46, 90, 18, .55),
        (820, 130, 620, 230, GREEN, 61, -110, -22, .40),
        (560, 30, 480, 170, DEEP, 38, 60, 26, .65),
    ]
    defs, layers, keys = [], [], []
    for i, (cx, cy, rx, ry, col, dur, dx, dy, op) in enumerate(blobs):
        defs.append(f"""
    <radialGradient id="g{i}{'f' if footer else ''}">
      <stop offset="0%"   stop-color="{col}" stop-opacity="{op}"/>
      <stop offset="55%"  stop-color="{col}" stop-opacity="{op*0.45:.2f}"/>
      <stop offset="100%" stop-color="{col}" stop-opacity="0"/>
    </radialGradient>""")
        layers.append(f"""
    <ellipse class="b{i}" cx="{cx}" cy="{cy*h/H:.0f}" rx="{rx}" ry="{ry}"
             fill="url(#g{i}{'f' if footer else ''})"/>""")
        # drift out and back -> identical start/end, no snap
        keys.append(f"""
    .b{i} {{ animation: d{i} {dur}s ease-in-out infinite; }}
    @keyframes d{i} {{
      0%   {{ transform: translate(0,0)        scale(1);    }}
      50%  {{ transform: translate({dx}px,{dy}px) scale(1.12); }}
      100% {{ transform: translate(0,0)        scale(1);    }}
    }}""")

    veil = (f'<rect width="{W}" height="{h}" fill="{t["bg"]}" '
            f'opacity="{t["veil"]}"/>' if t["veil"] else "")
    txt = "" if footer else titles(t)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}"
     viewBox="0 0 {W} {h}" role="img" aria-label="{NAME}">
  <defs>{''.join(defs)}
    <filter id="soft{'f' if footer else ''}" x="-30%" y="-60%"
            width="160%" height="220%">
      <feGaussianBlur stdDeviation="42"/>
    </filter>
    <clipPath id="cp{'f' if footer else ''}">
      <rect width="{W}" height="{h}" rx="0"/>
    </clipPath>
  </defs>
  <style>{base_style(t, ''.join(keys))}</style>
  <rect width="{W}" height="{h}" fill="{t['bg']}"/>
  <g clip-path="url(#cp{'f' if footer else ''})"
     filter="url(#soft{'f' if footer else ''})">{''.join(layers)}
  </g>
  {veil}{txt}
</svg>
"""


# ─────────────────────────── 2. dna helix ───────────────────────────
def helix(t, footer=False):
    h = 120 if footer else H
    period, amp = 240, 30
    mid = 46 if not footer else h - 46
    span = W + period * 2
    step = 4

    def strand(phase):
        pts = []
        for x in range(0, span + step, step):
            y = mid + amp * math.sin(2 * math.pi * (x / period) + phase)
            pts.append(f"{x},{y:.1f}")
        return "M" + " L".join(pts)

    rungs = []
    n = span // 24
    for i in range(n + 1):
        x = i * 24
        p = 2 * math.pi * (x / period)
        y1 = mid + amp * math.sin(p)
        y2 = mid + amp * math.sin(p + math.pi)
        depth = abs(math.cos(p))            # 1 at widest, 0 at crossover
        op = 0.18 + 0.62 * depth
        wid = 1.0 + 1.6 * depth
        col = GREEN if i % 2 else CYAN
        rungs.append(
            f'<line x1="{x}" y1="{y1:.1f}" x2="{x}" y2="{y2:.1f}" '
            f'stroke="{col}" stroke-opacity="{op:.2f}" '
            f'stroke-width="{wid:.2f}" stroke-linecap="round"/>')

    css = f"""
    .helix {{ animation: scroll 40s linear infinite; }}
    @keyframes scroll {{
      from {{ transform: translateX(0); }}
      to   {{ transform: translateX(-{period}px); }}
    }}
    .s1 {{ stroke: {CYAN};  }}
    .s2 {{ stroke: {GREEN}; }}"""
    txt = "" if footer else titles(t)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}"
     viewBox="0 0 {W} {h}" role="img" aria-label="{NAME}">
  <defs>
    <linearGradient id="fade{'f' if footer else ''}" x1="0" x2="1">
      <stop offset="0"    stop-color="#fff" stop-opacity="0"/>
      <stop offset=".14"  stop-color="#fff" stop-opacity="1"/>
      <stop offset=".86"  stop-color="#fff" stop-opacity="1"/>
      <stop offset="1"    stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <mask id="m{'f' if footer else ''}">
      <rect width="{W}" height="{h}"
            fill="url(#fade{'f' if footer else ''})"/>
    </mask>
  </defs>
  <style>{base_style(t, css)}</style>
  <rect width="{W}" height="{h}" fill="{t['bg']}"/>
  <g mask="url(#m{'f' if footer else ''})" opacity=".9">
    <g class="helix">
      <g>{''.join(rungs)}</g>
      <path class="s1" d="{strand(0)}" fill="none" stroke-width="3"
            stroke-linecap="round" opacity=".95"/>
      <path class="s2" d="{strand(math.pi)}" fill="none" stroke-width="3"
            stroke-linecap="round" opacity=".95"/>
    </g>
  </g>{txt}
</svg>
"""


# ───────────────────────── 3. parallax waves ─────────────────────────
def waves(t, footer=False):
    h = 120 if footer else H
    span = W * 2
    layers = [
        # period, amp, baseline, colour, dur, opacity
        (760, 15, 0.62, DEEP,  52, .32),
        (560, 13, 0.72, CYAN,  35, .45),
        (420, 10, 0.82, GREEN, 28, .55),
        (300, 7, 0.90, CYAN,  21, .35),
    ]
    paths, css = [], []
    for i, (period, amp, base, col, dur, op) in enumerate(layers):
        y0 = h * base
        pts = []
        for x in range(0, span + 6, 6):
            y = y0 + amp * math.sin(2 * math.pi * (x / period))
            pts.append(f"{x},{y:.1f}")
        d = ("M" + " L".join(pts) +
             f" L{span},{h} L0,{h} Z")
        paths.append(f'<path class="w{i}" d="{d}" fill="{col}" '
                     f'fill-opacity="{op}"/>')
        # horizontal scroll by exactly one period = seamless;
        # additive vertical bob with real easing = organic, no kink
        css.append(f"""
    .w{i} {{ animation: sc{i} {dur}s linear infinite,
                       bob{i} {dur*0.7:.0f}s ease-in-out infinite; }}
    @keyframes sc{i} {{
      from {{ transform: translateX(0); }}
      to   {{ transform: translateX(-{period}px); }}
    }}
    @keyframes bob{i} {{
      0%,100% {{ translate: 0 0; }}
      50%     {{ translate: 0 {amp*0.5:.1f}px; }}
    }}""")
    txt = "" if footer else titles(t)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}"
     viewBox="0 0 {W} {h}" role="img" aria-label="{NAME}">
  <style>{base_style(t, ''.join(css))}</style>
  <rect width="{W}" height="{h}" fill="{t['bg']}"/>
  <g>{''.join(paths)}</g>{txt}
</svg>
"""


# ───────────────────────── 4. chromatogram ─────────────────────────
# Two unrelated reads. The footer is not the header's reverse complement or a
# shifted copy — it is a different stretch of sequence entirely, so no amount
# of staring lines the two up.
SEQ_TOP = ("ACGTACGGATCCTAGCATGCTTACGATCGGCATTAGCCTAAGGCTTACGA"
           "TCGATCCGGTAACGTTAGCCATGGATCTTAGCACGGTTACCGATCAGGTA")
SEQ_BOT = ("TTGACCATGGCTAAGCTTCGGATACCGTTAGCTAGGCATCCGATTACGTG"
           "CAGGTTCAAGCCTGATCGGAATTCCGGATCTAGCTTAGGCAACGTCCATG")


def chroma(t, footer=False, desync=False):
    """Sanger trace.

    desync=False reproduces the original: header and footer share a sequence,
    a direction and a period, so they read as one wave sliced in two.

    desync=True gives the footer its own sequence, the opposite travel
    direction and a period that shares no small common multiple with the
    header's, so the two never drift into agreement.
    """
    h = 120 if footer else H
    base = h - 18
    peak_w, gap = 26, 22

    if desync and footer:
        seq, dur, rightward, phase = SEQ_BOT, 91, True, 2.3
    else:
        seq, dur, rightward, phase = SEQ_TOP, 72, False, 1.7

    cols = {"A": GREEN, "C": CYAN, "G": DEEP, "T": AMBER}
    heights = {"A": 44, "C": 52, "G": 38, "T": 48}
    unit = peak_w + gap
    cycle = len(seq) * unit

    peaks, labels = [], []
    for rep in range(2):                       # two copies -> seamless wrap
        for i, ch in enumerate(seq):
            x = (rep * len(seq) + i) * unit + 40
            amp = heights[ch] * (0.78 + 0.22 * math.sin(i * phase))
            d = (f"M{x-peak_w},{base} "
                 f"C{x-peak_w*0.42},{base} {x-peak_w*0.36},{base-amp} "
                 f"{x},{base-amp} "
                 f"C{x+peak_w*0.36},{base-amp} {x+peak_w*0.42},{base} "
                 f"{x+peak_w},{base}")
            peaks.append(f'<path d="{d}" fill="none" stroke="{cols[ch]}" '
                         f'stroke-width="2.4" stroke-opacity=".85" '
                         f'stroke-linecap="round"/>')
            labels.append(f'<text class="bp" x="{x}" y="{base+13}" '
                          f'text-anchor="middle" fill="{cols[ch]}">{ch}</text>')

    # travelling right just means running the same seamless slide backwards
    frm, to = (f"-{cycle}px", "0") if rightward else ("0", f"-{cycle}px")
    css = f"""
    .bp   {{ font: 600 11px {FONT}; opacity: .55; }}
    .trace{{ animation: pan {dur}s linear infinite; }}
    @keyframes pan {{
      from {{ transform: translateX({frm}); }}
      to   {{ transform: translateX({to}); }}
    }}"""
    txt = "" if footer else titles(t, y1=54, y2=80)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}"
     viewBox="0 0 {W} {h}" role="img" aria-label="{NAME}">
  <defs>
    <linearGradient id="cf{'f' if footer else ''}" x1="0" x2="1">
      <stop offset="0"   stop-color="#fff" stop-opacity="0"/>
      <stop offset=".1"  stop-color="#fff" stop-opacity="1"/>
      <stop offset=".9"  stop-color="#fff" stop-opacity="1"/>
      <stop offset="1"   stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <mask id="cm{'f' if footer else ''}">
      <rect width="{W}" height="{h}"
            fill="url(#cf{'f' if footer else ''})"/>
    </mask>
  </defs>
  <style>{base_style(t, css)}</style>
  <rect width="{W}" height="{h}" fill="{t['bg']}"/>
  <line x1="0" y1="{base}" x2="{W}" y2="{base}"
        stroke="{t['sub']}" stroke-opacity=".18"/>
  <g mask="url(#cm{'f' if footer else ''})">
    <g class="trace">{''.join(peaks)}{''.join(labels)}</g>
  </g>{txt}
</svg>
"""


BUILDERS = {"aurora": aurora, "helix": helix,
            "waves": waves, "chromatogram": chroma,
            "chromatogram-alt": lambda t, footer=False: chroma(
                t, footer=footer, desync=True)}

out = os.path.dirname(os.path.abspath(__file__))
for name, fn in BUILDERS.items():
    for tname, t in THEMES.items():
        for kind, is_footer in (("header", False), ("footer", True)):
            path = os.path.join(out, f"{name}-{kind}-{tname}.svg")
            with open(path, "w") as f:
                f.write(fn(t, footer=is_footer))
print("wrote", len(BUILDERS) * 4, "svgs to", out)
