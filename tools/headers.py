"""Generates section header strips that match the banner."""
import math, random, sys
W, H = 1200, 76
COLS = ["#f0b27a", "#cf7a45", "#5eead4", "#818cf8", "#f6d9b0", "#e8915a"]
def strip(num, title, seed):
    random.seed(seed)
    sp = []
    for i in range(46):
        # a swarm that thins out toward the left
        t = random.random() ** 0.55
        x = 1180 - (1 - t) * 520
        y = H/2 + random.gauss(0, 15) * (0.4 + t)
        s = random.uniform(1.6, 5.0) * (0.5 + t)
        sp.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{s*random.uniform(1.2,2.6):.1f}" ry="{s:.1f}" fill="{random.choice(COLS)}" opacity="{0.15 + 0.6*t*random.random():.2f}" transform="rotate({random.uniform(-40,40):.0f} {x:.0f} {y:.0f})"/>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{title}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#060a15"/><stop offset="1" stop-color="#0e1733"/></linearGradient>
    <linearGradient id="bar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5eead4"/><stop offset="1" stop-color="#818cf8"/></linearGradient>
    <filter id="b" x="-10%" y="-40%" width="120%" height="180%"><feGaussianBlur stdDeviation="0.8"/></filter>
    <clipPath id="r"><rect width="{W}" height="{H}" rx="14"/></clipPath>
  </defs>
  <g clip-path="url(#r)">
    <rect width="{W}" height="{H}" fill="url(#bg)"/>
    <rect x="0" y="0" width="5" height="{H}" fill="url(#bar)"/>
    <g filter="url(#b)">{"".join(sp)}</g>
    <text x="34" y="47" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="16" fill="#5eead4" letter-spacing="2">{num}</text>
    <text x="80" y="49" font-family="ui-sans-serif, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="29" font-weight="700" fill="#f8fafc">{title}</text>
  </g>
</svg>
'''
out = sys.argv[1]
for i, (slug, title) in enumerate([("nasa", "NASA Headquarters"), ("splatting", "3D Gaussian splatting"), ("ml", "Machine learning"), ("systems", "Systems, graphics, and low-level"), ("hardware", "Hardware"), ("more", "More")], 1):
    open(f"{out}/h-{slug}.svg", "w").write(strip(f"{i:02d}", title, i * 7))
