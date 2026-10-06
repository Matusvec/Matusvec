"""Generates the profile banner: a Mars made of Gaussian splats that refines like a training run."""
import math, random, sys
random.seed(11)
W, H = 1200, 380
CX, CY, R = 965, 205, 168
L = (-0.56, -0.50, 0.66)
ln = math.sqrt(sum(v*v for v in L)); L = tuple(v/ln for v in L)

def noise(x, y, z, o=0.0):
    return (math.sin(2.1*x + 1.3*y + o) * math.cos(1.7*z - 0.9*x + o*0.7)
            + 0.5*math.sin(4.3*y - 2.2*z + 1.1 + o) * math.cos(3.9*x + 0.4)
            + 0.25*math.sin(8.1*z + 5.3*x - 1.7) * math.cos(7.7*y + 2.2 + o))
STOPS = [(0.0, (62, 28, 20)), (0.30, (150, 62, 36)), (0.55, (203, 112, 62)), (0.80, (232, 172, 116)), (1.0, (248, 222, 180))]
def ramp(t):
    t = max(0.0, min(1.0, t))
    for (a, ca), (b, cb) in zip(STOPS, STOPS[1:]):
        if t <= b:
            k = (t - a) / (b - a)
            return tuple(ca[i] + (cb[i] - ca[i]) * k for i in range(3))
    return STOPS[-1][1]

def splat(size_lo, size_hi, alpha):
    # uniform point on the visible hemisphere
    while True:
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x*x + y*y < 0.985: break
    z = math.sqrt(max(0.0, 1 - x*x - y*y))
    lam = max(0.0, x*L[0] + y*L[1] + z*L[2])
    t = 0.5 + 0.34*noise(x*1.6, y*1.6, z*1.6) + 0.10*noise(x*5, y*5, z*5, 2.0)
    r, g, b = ramp(t)
    if y < -0.78:  # polar cap
        k = min(1.0, (-0.78 - y) / 0.10)
        r, g, b = r + (240 - r)*k, g + (234 - g)*k, b + (226 - b)*k
    sh = 0.14 + 1.08 * lam**0.7
    r, g, b = (min(255, int(c*sh)) for c in (r, g, b))
    a = alpha * min(1.0, 0.05 + lam*2.4)
    if a < 0.03: return None
    s = random.uniform(size_lo, size_hi)
    rx, ry = s * max(z, 0.28), s * random.uniform(0.55, 1.0)
    rot = math.degrees(math.atan2(y, x)) + random.uniform(-25, 25)
    return f'<ellipse cx="{CX + x*R:.1f}" cy="{CY + y*R:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="rgb({r},{g},{b})" opacity="{a:.2f}" transform="rotate({rot:.0f} {CX + x*R:.1f} {CY + y*R:.1f})"/>'

def layer(n, lo, hi, alpha):
    out = []
    while len(out) < n:
        s = splat(lo, hi, alpha)
        if s: out.append(s)
    return "\n      ".join(out)

def floaters(n):
    out = []
    cols = ["#f0b27a", "#cf7a45", "#5eead4", "#818cf8", "#f6d9b0"]
    for _ in range(n):
        ang = random.uniform(-2.6, 0.9)          # biased to the lit, upper-left side
        d = R * random.uniform(1.04, 1.55)
        x, y = CX + d*math.cos(ang), CY + d*math.sin(ang)
        if not (560 < x < W - 10 and 8 < y < H - 8): continue
        s = random.uniform(1.2, 4.2)
        out.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{s*random.uniform(1,2.4):.1f}" ry="{s:.1f}" fill="{random.choice(cols)}" opacity="{random.uniform(0.18,0.6):.2f}" transform="rotate({random.uniform(0,180):.0f} {x:.1f} {y:.1f})"/>')
    return "\n      ".join(out)

stars = "\n    ".join(f'<circle cx="{random.uniform(0,W):.0f}" cy="{random.uniform(0,H):.0f}" r="{random.choice([0.6,0.8,1.1]):.1f}" fill="#cbd5e1" opacity="{random.uniform(0.08,0.4):.2f}"/>' for _ in range(90))

def chip(x, y, text):
    w = 26 + len(text) * 9.1
    return (f'<rect x="{x}" y="{y}" width="{w:.0f}" height="32" rx="16" fill="#0f1b3a" stroke="#2b3b66"/>'
            f'<text class="m c" x="{x + w/2:.0f}" y="{y + 21}" text-anchor="middle" font-size="14">{text}</text>'), x + w + 10

chips, x = [], 64
for t in ["GAUSSIAN SPLATTING", "REINFORCEMENT LEARNING", "C++ · SYSTEMS"]:
    c, x = chip(x, 284, t); chips.append(c)

print(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Matus Vecera. Computer science and physics at Notre Dame. Gaussian splatting, reinforcement learning, C++ and low-level systems.">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#060a15"/><stop offset="1" stop-color="#0e1733"/></linearGradient>
    <radialGradient id="glow" cx="{CX}" cy="{CY}" r="{R*1.75}" gradientUnits="userSpaceOnUse">
      <stop offset="0.5" stop-color="#e8915a" stop-opacity="0.22"/><stop offset="0.72" stop-color="#5eead4" stop-opacity="0.07"/><stop offset="1" stop-color="#5eead4" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="base" cx="{CX - 0.36*R:.0f}" cy="{CY - 0.33*R:.0f}" r="{R*1.3:.0f}" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#d98a4e" stop-opacity="0.95"/><stop offset="0.5" stop-color="#8a3b22" stop-opacity="0.9"/><stop offset="0.82" stop-color="#2a1410" stop-opacity="0.55"/><stop offset="1" stop-color="#150b0a" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="bar" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#5eead4"/><stop offset="1" stop-color="#818cf8"/></linearGradient>
    <linearGradient id="fade" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#070c19"/><stop offset="1" stop-color="#070c19" stop-opacity="0"/></linearGradient>
    <filter id="b1" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="0.9"/></filter>
    <filter id="b2" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3.2"/></filter>
    <filter id="b3" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="11"/></filter>
    <clipPath id="r"><rect width="{W}" height="{H}" rx="18"/></clipPath>
  </defs>
  <style>
    .t {{ font-family: ui-sans-serif, -apple-system, "Segoe UI", Helvetica, Arial, sans-serif; fill: #f8fafc; }}
    .m {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; fill: #5eead4; letter-spacing: 2px; }}
    .c {{ fill: #c7d2fe; letter-spacing: 1.2px; }}
    .s {{ fill: #cbd5e1; }}
    /* the planet "trains": coarse blobs densify into fine splats, hold, then reset */
    .fine   {{ animation: fine 12s ease-in-out infinite; }}
    .mid    {{ animation: mid 12s ease-in-out infinite; }}
    .coarse {{ animation: coarse 12s ease-in-out infinite; opacity: 0; }}
    .fl     {{ animation: drift 9s ease-in-out infinite alternate; }}
    @keyframes fine   {{ 0%, 58% {{ opacity: 1; }} 66%, 74% {{ opacity: 0; }} 86% {{ opacity: 0.15; }} 100% {{ opacity: 1; }} }}
    @keyframes mid    {{ 0%, 58% {{ opacity: 0.85; }} 66%, 74% {{ opacity: 0; }} 86% {{ opacity: 1; }} 100% {{ opacity: 0.85; }} }}
    @keyframes coarse {{ 0%, 58% {{ opacity: 0; }} 66%, 76% {{ opacity: 1; }} 88% {{ opacity: 0.25; }} 100% {{ opacity: 0; }} }}
    @keyframes drift  {{ from {{ transform: translate(0, 0); }} to {{ transform: translate(-7px, -5px); }} }}
    @media (prefers-reduced-motion: reduce) {{ .fine, .mid, .coarse, .fl {{ animation: none; }} }}
  </style>
  <g clip-path="url(#r)">
    <rect width="{W}" height="{H}" fill="url(#bg)"/>
    {stars}
    <circle cx="{CX}" cy="{CY}" r="{R*1.75}" fill="url(#glow)"/>
    <ellipse cx="{CX}" cy="{CY}" rx="{R*1.62}" ry="{R*0.42}" fill="none" stroke="#5eead4" stroke-opacity="0.35" stroke-width="1" transform="rotate(-16 {CX} {CY})"/>
    <g class="coarse" filter="url(#b3)">
      {layer(46, 30, 58, 0.75)}
    </g>
    <g class="mid" filter="url(#b2)">
      <circle cx="{CX}" cy="{CY}" r="{R*0.97:.0f}" fill="url(#base)"/>
      {layer(240, 9, 19, 0.75)}
    </g>
    <g class="fine" filter="url(#b1)">
      {layer(1500, 3.0, 7.4, 0.95)}
    </g>
    <path d="M {CX - R*1.62*math.cos(math.radians(16)) :.1f} {CY + R*1.62*math.sin(math.radians(16)):.1f} A {R*1.62:.1f} {R*0.42:.1f} -16 0 0 {CX + R*1.62*math.cos(math.radians(16)):.1f} {CY - R*1.62*math.sin(math.radians(16)):.1f}" fill="none" stroke="#5eead4" stroke-opacity="0.75" stroke-width="1.2"/>
    <g class="fl" filter="url(#b1)">
      {floaters(70)}
    </g>
    <text class="m" x="64" y="92" font-size="14.5">CS + PHYSICS · NOTRE DAME '29 · NASA HQ</text>
    <text class="t" x="61" y="162" font-size="68" font-weight="700">Matus Vecera</text>
    <rect x="64" y="182" width="84" height="4" rx="2" fill="url(#bar)"/>
    <text class="t s" x="64" y="226" font-size="21">I rebuild real places in 3D, train agents that learn to cooperate,</text>
    <text class="t s" x="64" y="254" font-size="21">and write engines from the GPU up.</text>
    {"".join(chips)}
  </g>
</svg>''')
