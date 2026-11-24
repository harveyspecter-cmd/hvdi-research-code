"""Figure 2: the worked example (native UALink) as a 3D score view with verdict panel."""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Wedge, Circle
import numpy as np

plt.rcParams.update({"font.family": "Inter", "font.size": 9})
ORANGE, BLUE, GREY, INK, MUT = "#C24E12", "#2A6FB0", "#8A867A", "#1D1D1B", "#5F615C"
S = [("H", "Claimed\nmaturity", 2, ORANGE), ("T", "Technical\nproof", 1, BLUE), ("A", "Adoption", 1, BLUE),
     ("E", "Buyer\neconomics", 1, BLUE), ("Q", "Capital\nquality", 1, GREY)]
V, H = 1.00, 2

fig = plt.figure(figsize=(10.5, 4.6), dpi=220)
ax = fig.add_axes([0.0, 0.02, 0.6, 0.96]); ax.axis("off")
U, W, DX, DY = 1.0, 0.9, 0.42, 0.30   # unit height, bar width, depth offset
from matplotlib.colors import to_rgb
def shade(c, f): return tuple(min(1, max(0, v * f)) for v in to_rgb(c))
def poly(pts, fc, ec="white", a=1.0, lw=0.8, z=2): ax.add_patch(plt.Polygon(pts, closed=True, fc=fc, ec=ec, alpha=a, lw=lw, zorder=z))
xs = [0.6 + i * 1.45 for i in range(len(S))]
X0, X1 = 0.2, xs[-1] + W + 0.25
# floor
poly([(X0, 0), (X1, 0), (X1 + DX, DY), (X0 + DX, DY)], "#F2F0EA", ec="#D9D6CC", z=1)
# level grid on back wall
for z in range(0, 4):
    ax.plot([X0 + DX, X1 + DX], [z * U + DY] * 2, color="#E3E0D8", lw=0.7, zorder=0)
    ax.text(X1 + DX + 0.12, z * U + DY, str(z), color=MUT, fontsize=8, va="center")
ax.text(X1 + DX + 0.12, 3.45 * U + DY, "Level", color=MUT, fontsize=8)
def plane(z, c, a):
    poly([(X0, z * U), (X1, z * U), (X1 + DX, z * U + DY), (X0 + DX, z * U + DY)], c, ec=c, a=a, lw=0.9, z=1.5)
plane(V, BLUE, 0.13)
for x, (k, lab, v, c) in zip(xs, S):
    h = v * U
    poly([(x, 0), (x + W, 0), (x + W, h), (x, h)], c, z=3)
    poly([(x + W, 0), (x + W + DX, DY), (x + W + DX, h + DY), (x + W, h)], shade(c, 0.7), z=3)
    poly([(x, h), (x + W, h), (x + W + DX, h + DY), (x + DX, h + DY)], shade(c, 1.25), z=3)
    ax.text(x + W / 2 + DX / 2, h + DY + 0.12, f"{k} {v}", ha="center", fontsize=11.5, fontweight="bold", color=c, zorder=5)
    ax.text(x + W / 2, -0.12, lab, ha="center", va="top", fontsize=8, color=MUT, linespacing=1.1)
plane(H, ORANGE, 0.10)
# plane labels and gap
ax.text(X0 - 0.08, H * U + 0.02, "claimed\nlevel 2", color=ORANGE, fontsize=8.5, ha="right", va="center", fontweight="bold")
ax.text(X0 - 0.08, V * U + 0.02, "proven value\n1.00", color=BLUE, fontsize=8.5, ha="right", va="center", fontweight="bold")
gx = X1 + DX + 0.75
ax.annotate("", xy=(gx, H * U + DY / 2), xytext=(gx, V * U + DY / 2), arrowprops=dict(arrowstyle="<->", color=INK, lw=1.6))
ax.text(gx + 0.12, (H + V) / 2 * U + DY / 2, "gap\n+1.00", color=INK, fontsize=11, fontweight="bold", va="center")
ax.text(X0, -0.78, va="top", s= "Proven value is the mean of technical proof, adoption and buyer economics.\nCapital quality (grey) is reported beside the gap, never subtracted.", fontsize=7.3, color=MUT)
ax.set_xlim(X0 - 1.25, gx + 0.9); ax.set_ylim(-1.5, 3.8); ax.set_aspect("equal")

# right panel
P = fig.add_axes([0.62, 0.06, 0.37, 0.88]); P.axis("off"); P.set_xlim(0, 1); P.set_ylim(0, 1)
P.add_patch(FancyBboxPatch((0.0, 0.0), 1, 1, boxstyle="round,pad=0,rounding_size=0.04", fc="#F6F5F1", ec="#D9D6CC"))
P.text(0.06, 0.9, "Native UALink scale-up", fontsize=12, fontweight="bold", color=INK)
P.text(0.06, 0.66, "+1.00", fontsize=30, fontweight="bold", color=ORANGE)
P.text(0.52, 0.735, "Story ahead of proof", fontsize=9.5, color=ORANGE, fontweight="bold")
P.text(0.52, 0.68, "on the +1.0 threshold", fontsize=8.5, color=MUT)
# stability ring
cx, cy, r = 0.14, 0.44, 0.085
P.add_patch(Wedge((cx, cy), r, 90 - 360 * 0.61, 90, width=0.03, fc=INK, transform=P.transData))
P.add_patch(Wedge((cx, cy), r, 90, 90 + 360 * 0.39, width=0.03, fc="#E3E0D8"))
P.text(cx, cy, "61%", ha="center", va="center", fontsize=9, fontweight="bold", color=INK)
P.text(0.28, 0.47, "Stable in 61% of 20,000 re-scorings", fontsize=8.5, color=INK, va="center")
P.text(0.28, 0.41, "90% of gaps between 0.00 and +1.41", fontsize=8.5, color=MUT, va="center")
# outlook
P.text(0.06, 0.27, "Outlook  likely to stall", fontsize=10, fontweight="bold", color=INK)
for i, (lab, sym, c) in enumerate((("Milestone", "▲", BLUE), ("On time", "▼", ORANGE), ("Money", "▼", ORANGE), ("Gates", "●", INK))):
    x = 0.06 + i * 0.235
    P.add_patch(FancyBboxPatch((x, 0.10), 0.2, 0.12, boxstyle="round,pad=0,rounding_size=0.02", fc="white", ec="#D9D6CC"))
    P.text(x + 0.1, 0.175, sym, ha="center", fontsize=10, color=c); P.text(x + 0.1, 0.12, lab, ha="center", fontsize=7.5, color=MUT)
P.text(0.06, 0.012, "Switch silicon samples at the end of 2026, volume in 2027.\nThe first racks shipped without it.", fontsize=7.3, color=MUT)
fig.savefig("fig_info_ualink_card.png", dpi=220, bbox_inches="tight", facecolor="white")
print("ok")
