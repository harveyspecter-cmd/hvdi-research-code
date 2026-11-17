"""Framework diagram: one picture of the HVDI, in light (report, print deck) and dark (screen deck)."""
import pathlib
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

HERE = pathlib.Path(__file__).resolve().parent
PAL = {
    "light": dict(bg="#FFFFFF", ink="#141414", mut="#555555", box="#F3F2ED", line="#BDBAB0", hot="#B4470F", cool="#2A6FB0", mid="#6F6B60"),
    "dark": dict(bg="#000000", ink="#F3F1EA", mut="#9A9D96", box="#101211", line="#3A3D3A", hot="#E8601C", cool="#3D8FD6", mid="#B9B5A8"),
}


def draw(mode: str, out: pathlib.Path, scale: float = 1.0, footer: bool = True) -> None:
    c = PAL[mode]
    y_lo = 0.0 if footer else 0.3
    fig, ax = plt.subplots(figsize=(12.4, 5.9 - y_lo), dpi=200)
    fig.patch.set_facecolor(c["bg"]); ax.set_facecolor(c["bg"])
    ax.set_xlim(0, 12.4); ax.set_ylim(y_lo, 5.9); ax.axis("off")

    def box(x, y, w, h, edge=None, fill=None, lw=1.0):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.09", fc=fill or c["box"],
                                    ec=edge or c["line"], lw=lw, zorder=2))

    def txt(x, y, s, size=9.5, col=None, bold=False, ha="left", va="center"):
        ax.text(x, y, s, fontsize=size * scale, color=col or c["ink"], fontweight="bold" if bold else "normal", ha=ha, va=va,
                zorder=4, linespacing=1.35)

    def arrow(x1, y1, x2, y2, col=None, style="-|>", ls="-"):
        ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style, mutation_scale=12, lw=1.3, ls=ls,
                                     color=col or c["mut"], zorder=3, shrinkA=0, shrinkB=0))

    # gate band
    box(0.2, 4.85, 12.0, 0.85, edge=c["hot"], lw=1.3)
    txt(0.4, 5.42, "X  Gates, outside the arithmetic", 11, c["hot"], True)
    txt(0.4, 5.07, "Site power and grid   ·   Advanced packaging   ·   High-bandwidth memory   ·   Indium phosphide lasers   ·   Export policy", 9.2, c["mut"])
    txt(12.0, 5.42, "A blocked gate overrides every score", 10, c["ink"], True, ha="right")

    y0, h = 2.35, 2.0
    # 1 evidence
    box(0.2, y0, 2.15, h)
    txt(0.35, y0 + h - 0.25, "1  Evidence", 11, c["ink"], True)
    txt(0.35, y0 + 1.12, "217 public sources and\n76 dated claims, each with\npublisher, date and unit", 8.8, c["mut"])
    txt(0.35, y0 + 0.35, "Graded by who holds it:\nbuyer, tracker, filing, vendor", 8.8, c["ink"])
    # 2 scores
    box(2.75, y0, 4.05, h)
    txt(2.9, y0 + h - 0.25, "2  Five scores, each 0 to 4", 11, c["ink"], True)
    tiles = [("H", "Claimed\n(dated claims)", c["hot"], 2.9), ("T", "Technical\nproof", c["cool"], 3.72), ("A", "Adoption", c["cool"], 4.47),
             ("E", "Buyer\neconomics", c["cool"], 5.22), ("Q", "Capital\nquality", c["mid"], 6.04)]
    for k, lab, col, x in tiles:
        box(x, y0 + 0.5, 0.66, 0.95, edge=col, fill=c["bg"], lw=1.2)
        txt(x + 0.33, y0 + 1.17, k, 15, col, True, ha="center")
        txt(x + 0.33, y0 + 0.74, lab, 6.6, c["mut"], ha="center")
    ax.plot([3.72, 5.88], [y0 + 0.36, y0 + 0.36], color=c["cool"], lw=1.2, zorder=3)
    txt(4.8, y0 + 0.2, "Proven value  V = mean(T, A, E)", 8.6, c["cool"], True, ha="center")
    # 3 gap
    box(7.2, y0, 1.45, h)
    txt(7.35, y0 + h - 0.25, "3  Gap", 11, c["ink"], True)
    txt(7.925, y0 + 1.05, "D = H − V", 13, c["ink"], True, ha="center")
    txt(7.925, y0 + 0.45, "story minus\nproof", 8.6, c["mut"], ha="center")
    # 4 verdict
    box(9.05, y0, 1.6, h)
    txt(9.2, y0 + h - 0.25, "4  Verdict", 11, c["ink"], True)
    txt(9.2, y0 + 1.28, "D ≥ +1  story ahead", 8.6, c["hot"], True)
    txt(9.2, y0 + 0.98, "between  aligned", 8.6, c["ink"])
    txt(9.2, y0 + 0.68, "D ≤ −1  proof ahead", 8.6, c["cool"], True)
    txt(9.2, y0 + 0.27, "Stability: share of\n20,000 re-scorings", 7.8, c["mut"])
    # 5 posture
    box(11.05, y0, 1.15, h, edge=c["ink"], lw=1.3)
    txt(11.17, y0 + h - 0.25, "5  Posture", 11, c["ink"], True)
    txt(11.17, y0 + 0.82, "Deploy\nPilot\nHold option\nDefer\nProve baseline", 8.6, c["ink"])
    for x1, x2 in ((2.35, 2.75), (6.8, 7.2), (8.65, 9.05), (10.65, 11.05)):
        arrow(x1, y0 + h / 2, x2, y0 + h / 2)
    # lower row
    box(2.75, 0.4, 3.3, 1.3)
    txt(2.9, 1.45, "Admission rule", 10, c["ink"], True)
    txt(2.9, 0.88, "A score of 3 or more needs proof from a buyer,\nan independent tracker or a filing.\nVendor-only evidence stops at 2.", 8.6, c["mut"])
    arrow(4.4, 1.7, 4.4, y0, style="-|>")
    box(8.2, 0.4, 4.0, 1.3)
    txt(8.35, 1.45, "Outlook", 10, c["ink"], True)
    txt(8.35, 0.88, "Dated milestone on the weakest leg, punctuality\nof the last one, and capital quality Q.\nQ is reported beside D, never subtracted.", 8.6, c["mut"])
    arrow(6.37, y0 + 0.5, 6.37, 1.05, col=c["mid"], style="-")
    arrow(6.37, 1.05, 8.2, 1.05, col=c["mid"])
    arrow(11.62, 1.7, 11.62, y0)
    arrow(11.62, 4.85, 11.62, y0 + h, col=c["hot"])
    if footer:
        txt(0.2, 0.12, "Read left to right: evidence is graded, scored, differenced and tested before it becomes a posture.", 8.6, c["mut"])
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
    fig.savefig(out, facecolor=c["bg"]); plt.close(fig)


if __name__ == "__main__":
    draw("light", HERE / "fig_framework.png")
    deck = HERE.parent / "deck"
    if deck.exists() or len(sys.argv) > 1:
        d = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else deck
        draw("dark", d / "framework_dark.png", 1.12, False); draw("light", d / "framework_light.png", 1.12, False)
    print("framework figures ok")
