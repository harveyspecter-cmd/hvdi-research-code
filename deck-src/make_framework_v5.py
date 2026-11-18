"""Framework visual v5: the original five-step layout, restyled as an infographic."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle

plt.rcParams["font.family"] = "Inter"
PAL = {
    "dark": dict(bg="#000000", ink="#F3F1EA", mut="#9A9D96", card="#111312", edge="#2B2E2B", hot="#E8601C", cool="#3D8FD6", mid="#B9B5A8", glow=0.10),
    "light": dict(bg="#FFFFFF", ink="#141414", mut="#5A5A5A", card="#F6F5F1", edge="#DAD8D0", hot="#C24E12", cool="#2A6FB0", mid="#8A867A", glow=0.07),
}
W, H = 24.8, 11.2


def draw(mode, out):
    c = PAL[mode]
    fig = plt.figure(figsize=(W / 2, H / 2), dpi=220)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")
    fig.patch.set_facecolor(c["bg"])

    def T(x, y, s, size=11, col=None, w="normal", **k):
        return ax.text(x, y, s, fontsize=size, color=col or c["ink"], fontweight=w, **k)

    def card(x, y, w, h, edge=None, fill=None, lw=1.0, r=0.32, glow=None):
        if glow:
            for k, a in ((0.22, 0.05), (0.12, 0.08)):
                ax.add_patch(FancyBboxPatch((x - k, y - k), w + 2 * k, h + 2 * k, boxstyle=f"round,pad=0,rounding_size={r + k}",
                                            fc=glow, ec="none", alpha=a))
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", fc=fill or c["card"],
                                    ec=edge or c["edge"], lw=lw))

    def badge(x, y, n, col):
        ax.add_patch(Circle((x, y), 0.3, fc=col, ec="none"))
        T(x, y - 0.01, str(n), 12, c["bg"], "bold", ha="center", va="center")

    def arrow(p, q, col, lw=1.6, cs="arc3", ls="-"):
        ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>,head_length=6,head_width=3.5", mutation_scale=1.6, color=col,
                                     lw=lw, connectionstyle=cs, linestyle=ls, shrinkA=0, shrinkB=0))

    # gates canopy
    card(0.6, 9.05, 23.6, 1.7, edge=c["hot"], fill=c["bg"], lw=1.4, r=0.4, glow=c["hot"])
    ax.add_patch(FancyBboxPatch((0.6, 9.05), 23.6, 1.7, boxstyle="round,pad=0,rounding_size=0.4", fc=c["hot"], ec="none", alpha=c["glow"]))
    T(1.1, 10.3, "X", 17, c["hot"], "bold", va="center")
    T(1.65, 10.3, "Gates, outside the arithmetic", 15, c["hot"], "bold", va="center")
    T(23.75, 10.3, "A blocked gate overrides every score", 13, c["ink"], "bold", va="center", ha="right")
    gates = ["Site power and grid", "Advanced packaging", "High-bandwidth memory", "Indium phosphide lasers", "Export policy"]
    x = 1.1
    for g in gates:
        wd = 0.62 + len(g) * 0.175
        ax.add_patch(FancyBboxPatch((x, 9.28), wd, 0.5, boxstyle="round,pad=0,rounding_size=0.25", fc=c["card"], ec=c["hot"], lw=0.9))
        ax.add_patch(Circle((x + 0.27, 9.53), 0.07, fc=c["hot"], ec="none"))
        T(x + 0.45, 9.525, g, 9.5, c["ink"], va="center")
        x += wd + 0.32

    yb, hb = 3.95, 4.05
    # 1 evidence
    card(0.6, yb, 4.35, hb); badge(1.2, yb + hb - 0.55, 1, c["mid"])
    T(1.7, yb + hb - 0.55, "Evidence", 15, w="bold", va="center")
    T(1.0, yb + 2.45, "217", 25, c["ink"], "bold", va="center"); T(2.6, yb + 2.45, "public sources", 10, c["mut"], va="center")
    T(1.0, yb + 1.6, "76", 25, c["hot"], "bold", va="center"); T(2.6, yb + 1.6, "dated claims", 10, c["mut"], va="center")
    T(1.0, yb + 0.8, "graded by who holds the proof", 9, c["mut"], va="center")
    for k, (nm, a) in enumerate((("buyer", 1.0), ("tracker", 0.75), ("filing", 0.55), ("vendor", 0.3))):
        xx = 0.95 + k * 0.98
        ax.add_patch(FancyBboxPatch((xx, yb + 0.2), 0.92, 0.36, boxstyle="round,pad=0,rounding_size=0.18", fc=c["cool"], ec="none", alpha=a))
        T(xx + 0.46, yb + 0.38, nm, 7.5, "#FFFFFF" if a > 0.6 else c["ink"], "bold", ha="center", va="center")

    # 2 five scores
    x2, w2 = 5.55, 8.0
    card(x2, yb, w2, hb); badge(x2 + 0.6, yb + hb - 0.55, 2, c["mid"])
    T(x2 + 1.1, yb + hb - 0.55, "Five scores, each 0 to 4", 15, w="bold", va="center")
    tiles = [("H", "Claimed\nmaturity", c["hot"], 4), ("T", "Technical\nproof", c["cool"], 3), ("A", "Adoption", c["cool"], 3),
             ("E", "Buyer\neconomics", c["cool"], 2), ("Q", "Capital\nquality", c["mid"], 2)]
    for k, (L, lab, col, lv) in enumerate(tiles):
        tx = x2 + 0.4 + k * 1.5 + (0.25 if k == 4 else 0)
        ax.add_patch(FancyBboxPatch((tx, yb + 1.1), 1.25, 1.9, boxstyle="round,pad=0,rounding_size=0.22",
                                    fc=col if k == 0 else c["bg"], ec=col, lw=1.6, alpha=1, ls="--" if k == 4 else "-"))
        T(tx + 0.625, yb + 2.5, L, 22, c["bg"] if k == 0 else col, "bold", ha="center", va="center")
        for d in range(4):
            ax.add_patch(Circle((tx + 0.29 + d * 0.22, yb + 1.95), 0.065, fc=(c["bg"] if k == 0 else col), ec="none",
                                alpha=0.95 if d < lv else 0.25))
        T(tx + 0.625, yb + 1.5, lab, 7.5, c["bg"] if k == 0 else c["mut"], ha="center", va="center", linespacing=1.1)
    bx0, bx1 = x2 + 1.9, x2 + 1.9 + 3 * 1.5 - 0.25
    ax.plot([bx0, bx0, bx1, bx1], [yb + 0.95, yb + 0.8, yb + 0.8, yb + 0.95], color=c["cool"], lw=1.4)
    T((bx0 + bx1) / 2, yb + 0.45, "Proven value   V = mean(T, A, E)", 11.5, c["cool"], "bold", ha="center", va="center")

    # 3 gap
    x3, w3 = 14.1, 3.1
    card(x3, yb, w3, hb); badge(x3 + 0.6, yb + hb - 0.55, 3, c["mid"])
    T(x3 + 1.1, yb + hb - 0.55, "Gap", 15, w="bold", va="center")
    T(x3 + w3 / 2, yb + 2.45, "D = H − V", 21, w="bold", ha="center", va="center")
    T(x3 + w3 / 2, yb + 1.75, "story minus proof", 10.5, c["mut"], ha="center", va="center")
    lx0, lx1, ly = x3 + 0.35, x3 + w3 - 0.35, yb + 0.85
    seg = (lx1 - lx0) / 4
    for k, (col, a) in enumerate(((c["cool"], 1), (c["mid"], 0.35), (c["mid"], 0.35), (c["hot"], 1))):
        ax.add_patch(Rectangle((lx0 + k * seg, ly - 0.09), seg - 0.03, 0.18, fc=col, ec="none", alpha=a))
    for k, t in enumerate(["−2", "−1", "0", "+1", "+2"]):
        T(lx0 + k * seg, ly - 0.38, t, 8.5, c["mut"], ha="center", va="center")

    # 4 verdict
    x4, w4 = 17.7, 3.95
    card(x4, yb, w4, hb); badge(x4 + 0.6, yb + hb - 0.55, 4, c["mid"])
    T(x4 + 1.1, yb + hb - 0.55, "Verdict", 15, w="bold", va="center")
    for k, (txt, col, a) in enumerate((("story ahead   D ≥ +1", c["hot"], 1), ("aligned", c["mid"], 0.45), ("proof ahead   D ≤ −1", c["cool"], 1))):
        yy = yb + 2.65 - k * 0.55
        ax.add_patch(FancyBboxPatch((x4 + 0.35, yy - 0.11), 0.22, 0.22, boxstyle="round,pad=0,rounding_size=0.11", fc=col, ec="none", alpha=a))
        T(x4 + 0.7, yy, txt, 10, col if a == 1 else c["ink"], "bold", va="center")
    xs = np.linspace(-2.2, 2.2, 23)
    for k, v in enumerate(xs):
        hgt = 0.55 * np.exp(-v * v / 1.1)
        ax.add_patch(Rectangle((x4 + 0.4 + k * 0.115, yb + 0.55), 0.08, hgt, fc=c["mid"], ec="none", alpha=0.6))
    T(x4 + 3.15, yb + 0.85, "stability:\nshare of\n20,000\nre-scorings", 8, c["mut"], ha="right", va="center", linespacing=1.05) if False else None
    T(x4 + 0.4, yb + 0.33, "stability across 20,000 re-scorings", 7.5, c["mut"], va="center")

    # 5 posture
    x5, w5 = 22.15, 2.05
    card(x5, yb, w5, hb, edge=c["hot"], lw=1.6, glow=c["hot"]); badge(x5 + 0.5, yb + hb - 0.55, 5, c["hot"])
    T(x5 + 0.88, yb + hb - 0.55, "Posture", 11.5, w="bold", va="center")
    for k, nm in enumerate(["Deploy", "Pilot", "Hold option", "Defer", "Prove baseline"]):
        yy = yb + 2.75 - k * 0.56
        ax.add_patch(FancyBboxPatch((x5 + 0.22, yy - 0.21), w5 - 0.44, 0.42, boxstyle="round,pad=0,rounding_size=0.21",
                                    fc=c["hot"], ec="none", alpha=0.16 + 0.04 * (4 - k)))
        T(x5 + w5 / 2, yy, nm, 8.5, c["ink"], ha="center", va="center")

    # flow arrows
    ym = yb + hb / 2
    for a, b in ((4.95, x2), (x2 + w2, x3), (x3 + w3, x4), (x4 + w4, x5)):
        arrow((a + 0.08, ym), (b - 0.08, ym), c["mid"], 1.8)
    arrow((x5 + w5 / 2, 9.05), (x5 + w5 / 2, yb + hb + 0.05), c["hot"], 1.8)

    # admission and outlook
    card(x2, 0.35, 6.3, 2.75); ax.add_patch(Rectangle((x2, 0.35 + 2.75 - 0.08), 6.3, 0.0, fc="none"))
    T(x2 + 0.4, 2.6, "Admission rule", 14, w="bold", va="center")
    T(x2 + 0.4, 2.05, "A score of 3 or more needs proof from a\nbuyer, an independent tracker or a filing.", 10.5, c["mut"], va="top", linespacing=1.35)
    T(x2 + 0.4, 0.85, "Vendor-only evidence stops at 2.", 10.5, c["hot"], "bold", va="center")
    arrow((x2 + 3.4, 3.1), (x2 + 3.4, yb - 0.05), c["mid"], 1.5)
    x6 = 15.4
    card(x6, 0.35, 24.2 - x6, 2.75)
    T(x6 + 0.4, 2.6, "Outlook", 14, w="bold", va="center")
    T(x6 + 0.4, 2.05, "Dated milestone on the weakest leg, punctuality of the\nlast one, and capital quality Q.", 10.5, c["mut"], va="top", linespacing=1.35)
    T(x6 + 0.4, 0.85, "Q is reported beside D, never subtracted.", 10.5, c["ink"], "bold", va="center")
    for k, nm in enumerate(["closing", "holding", "stalling"]):
        ax.add_patch(FancyBboxPatch((24.2 - 3.75 + k * 1.15, 2.42), 0.98, 0.36, boxstyle="round,pad=0,rounding_size=0.18",
                                    fc=c["bg"], ec=(c["cool"], c["mid"], c["hot"])[k], lw=1.1))
        T(24.2 - 3.75 + 0.49 + k * 1.15, 2.6, nm, 8, (c["cool"], c["mid"], c["hot"])[k], ha="center", va="center")
    qx = x2 + 0.4 + 4 * 1.5 + 0.25 + 1.05
    ax.plot([qx, qx, x6 - 0.15], [yb + 1.1, 1.75, 1.75], color=c["mid"], lw=1.3, ls=(0, (3, 3)))
    arrow((x6 - 0.4, 1.75), (x6 - 0.03, 1.75), c["mid"], 1.3)
    arrow((x5 + w5 / 2, 3.1), (x5 + w5 / 2, yb - 0.05), c["mid"], 1.5)
    fig.savefig(out, facecolor=c["bg"])
    plt.close(fig)


if __name__ == "__main__":
    draw("dark", "framework_v5_dark.png"); draw("light", "framework_v5_light.png"); print("ok")
