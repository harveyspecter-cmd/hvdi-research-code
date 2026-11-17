"""Framework visual v4: two streams (story, proof) meet in a divergence dial, haloed by the gates."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Circle, FancyBboxPatch, Arc

PAL = {
    "dark": dict(bg="#000000", hot="#E8601C", cool="#3D8FD6", mid="#B9B5A8", ink="#F3F1EA", mut="#9A9D96", line="#2c2e2b", card="#101211"),
    "light": dict(bg="#FFFFFF", hot="#C24E12", cool="#2A6FB0", mid="#8A867A", ink="#141414", mut="#555555", line="#D5D3CC", card="#F3F2ED"),
}
W, H = 24.6, 11.0


def bez(p0, p1, p2, p3, n=200):
    t = np.linspace(0, 1, n)[:, None]
    return (1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t ** 2 * p2 + t ** 3 * p3


def ribbon(ax, p0, p3, w0, w1, col, a0=0.08, a1=0.55):
    p0, p3 = np.array(p0), np.array(p3)
    p1 = p0 + np.array([(p3[0] - p0[0]) * 0.55, 0])
    p2 = p3 - np.array([(p3[0] - p0[0]) * 0.45, 0])
    c = bez(p0, p1, p2, p3)
    n = len(c)
    for i in range(n - 1):
        f = i / (n - 1)
        w = w0 + (w1 - w0) * f
        ax.fill_between([c[i, 0], c[i + 1, 0] + 0.01], c[i, 1] - w / 2, c[i, 1] + w / 2,
                        color=col, alpha=a0 + (a1 - a0) * f, lw=0)
    ax.plot(c[:, 0], c[:, 1], color=col, lw=1.4, alpha=0.9)


def draw(mode, out):
    c = PAL[mode]
    fig = plt.figure(figsize=(W / 2, H / 2), dpi=220)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")
    fig.patch.set_facecolor(c["bg"])
    T = lambda x, y, s, size=11, col=c["ink"], **k: ax.text(x, y, s, fontsize=size, color=col, family="DejaVu Sans", **k)

    cx, cy, R1, R0 = 14.6, 3.85, 3.55, 2.55
    ang = lambda d: 90 - d * 35
    # streams flow under the raised feet of the dial into its hollow
    ribbon(ax, (5.3, 6.6), (cx - 0.75, cy + 0.12), 1.0, 0.3, c["hot"])
    ribbon(ax, (5.3, 2.2), (cx - 0.75, cy - 0.3), 1.0, 0.3, c["cool"])
    ax.add_patch(Circle((cx - 0.62, cy - 0.09), 0.14, fc=c["ink"], ec="none", zorder=5))
    for y, col in ((6.6, c["hot"]), (2.2, c["cool"])):
        ax.add_patch(FancyBboxPatch((0.45, y - 1.3), 4.85, 2.6, boxstyle="round,pad=0,rounding_size=0.45",
                                    fc=c["card"], ec=col, lw=1.3))
    T(0.9, 7.35, "Story", 17, c["hot"], weight="bold")
    T(0.9, 6.65, "H  claimed maturity", 11.5, c["ink"], weight="bold")
    T(0.9, 6.15, "76 dated public claims,\nstage and narrative", 9.5, c["mut"], va="top")
    T(0.9, 2.95, "Proof", 17, c["cool"], weight="bold")
    for k, ch in enumerate("TAE"):
        ax.add_patch(FancyBboxPatch((0.9 + k * 0.78, 1.95), 0.62, 0.68, boxstyle="round,pad=0,rounding_size=0.14",
                                    fc=c["bg"], ec=c["cool"], lw=1.2))
        T(1.21 + k * 0.78, 2.29, ch, 12, c["cool"], weight="bold", ha="center", va="center")
    T(3.35, 2.29, "V = mean", 10, c["ink"], weight="bold", va="center")
    T(0.9, 1.75, "3 or more only with a buyer,\ntracker or filing", 9, c["mut"], va="top")
    T(2.9, 4.4, "217 sources, each graded\nby who holds the proof", 9, c["mut"], ha="center", va="center", style="italic")
    # dial
    for d0, d1, col, al in ((-2, -1, c["cool"], 0.85), (-1, 1, c["mid"], 0.28), (1, 2, c["hot"], 0.9)):
        ax.add_patch(Wedge((cx, cy), R1, ang(d1), ang(d0), width=R1 - R0, fc=col, alpha=al, ec=c["bg"], lw=3))
    rm = (R0 + R1) / 2
    for d, txt, col in ((-1.5, "proof\nahead", c["bg"]), (0, "aligned", c["ink"]), (1.5, "story\nahead", c["bg"])):
        a = ang(d)
        T(cx + rm * np.cos(np.radians(a)), cy + rm * np.sin(np.radians(a)), txt, 9.5, col, ha="center", va="center",
          weight="bold", rotation=a - 90, linespacing=1.0)
    for d in (-2, -1, 0, 1, 2):
        a = np.radians(ang(d)); r = R1 + 0.3
        T(cx + r * np.cos(a), cy + r * np.sin(a), f"{d:+d}" if d else "0", 9, c["mut"], ha="center", va="center")
    T(cx + 0.05, cy + 1.6, "D = H − V", 19.5, c["ink"], weight="bold", ha="center", va="center")
    T(cx + 0.05, cy + 0.9, "the gap", 10, c["mut"], ha="center", va="center")
    T(cx + 0.3, cy - 0.75, "Verdict, kept or lost across\n20,000 random re-scorings", 9.5, c["mut"], ha="center", va="top")
    # gate halo
    Rg = R1 + 1.35
    ax.add_patch(Arc((cx, cy), 2 * Rg, 2 * Rg, theta1=22, theta2=158, color=c["hot"], lw=1.1, ls=(0, (2, 4)), alpha=0.8))
    for nm, a in (("power", 150), ("packaging", 120), ("memory", 90), ("lasers", 60), ("export", 30)):
        r = np.radians(a); x, y = cx + Rg * np.cos(r), cy + Rg * np.sin(r)
        ax.add_patch(Circle((x, y), 0.2, fc=c["bg"], ec=c["hot"], lw=1.5))
        T(x + 0.62 * np.cos(r), y + 0.5 * np.sin(r), nm, 9.5, c["ink"], ha="center", va="center")
    T(cx, cy + Rg + 1.05, "X  gates: a blocked gate overrides every score", 11, c["hot"], ha="center", va="center", weight="bold")
    # Q beside
    ax.plot([5.3, 20.2], [0.55, 0.55], color=c["mid"], lw=1.2, ls=(0, (1, 3)))
    ax.add_patch(Circle((20.2, 0.55), 0.13, fc=c["mid"], ec="none"))
    T(5.3, 0.82, "Q  capital quality runs beside the gap, never subtracted from it", 9.5, c["mid"])
    # posture
    px = 20.4
    T(px, 8.3, "Posture", 15, c["ink"], weight="bold")
    T(px, 7.75, "timed by the outlook:\nclosing, holding, stalling", 9, c["mut"], va="top")
    for k, nm in enumerate(["Deploy", "Pilot at scale", "Hold an option", "Defer", "Prove the baseline"]):
        y = 6.1 - k * 0.98
        ax.add_patch(FancyBboxPatch((px, y - 0.36), 3.9, 0.72, boxstyle="round,pad=0,rounding_size=0.36",
                                    fc=c["card"], ec=c["line"], lw=1))
        T(px + 0.35, y, nm, 11, c["ink"], va="center")
    fig.savefig(out, facecolor=c["bg"])
    plt.close(fig)


if __name__ == "__main__":
    draw("dark", "framework_v4_dark.png"); draw("light", "framework_v4_light.png"); print("ok")
