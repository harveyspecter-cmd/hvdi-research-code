"""Figure A4: back-test gap and proof over time (exploratory)."""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "axes.spines.top": False, "axes.spines.right": False})
BLUE, ORANGE, GREY = "#2A6FB0", "#C24E12", "#8A867A"
S = dict(oD=[(8,-24),(10,2),(-70,6)], oV=[(8,6),(8,-12),(-40,-14)], name="OpenFlow SDN (stalled)", x=[2013, 2015, 2017], D=[0.67, 0.33, 1.33], V=[2.33, 1.67, 1.67], p=[16, 2, 25], c=ORANGE, m="s")
G = dict(oD=[(8,6),(8,-24),(8,-24)], oV=[(8,4),(-55,8),(-40,8)], name="400G Ethernet (realised)", x=[2018, 2020, 2022], D=[1.67, 0.00, 0.67], V=[1.33, 2.00, 2.33], p=[57, 15, 13], c=BLUE, m="o")
fig, ax = plt.subplots(1, 2, figsize=(9.2, 3.5))
for t in (S, G):
    k = [str(i) for i in range(1, 4)]
    ax[0].plot(k, t["D"], marker=t["m"], color=t["c"], lw=2, ms=7, label=t["name"])
    ax[1].plot(k, t["V"], marker=t["m"], color=t["c"], lw=2, ms=7, label=t["name"])
    for i, (d, p, yr) in enumerate(zip(t["D"], t["p"], t["x"])):
        ax[0].annotate(f"{yr}: {d:+.2f}\n({p}% ahead)", (i, d), textcoords="offset points",
                       xytext=t["oD"][i], fontsize=6.8, color=t["c"])
    for i, (v, yr) in enumerate(zip(t["V"], t["x"])):
        ax[1].annotate(f"{yr}: {v:.2f}", (i, v), textcoords="offset points", xytext=t["oV"][i], fontsize=6.8, color=t["c"])
ax[0].axhspan(-1, 1, color=GREY, alpha=0.10, lw=0); ax[0].axhline(1, color=GREY, ls="--", lw=1)
ax[0].text(2.55, 2.15, "dashed line: story ahead (D ≥ +1)", fontsize=6.8, color=GREY, ha="right", va="top")
ax[0].set_ylim(-0.4, 2.2); ax[0].set_ylabel("Gap D = H − V")
ax[0].set_title("(a) Gap over time", loc="left", fontsize=9.5)
ax[1].set_ylim(1, 2.8); ax[1].set_ylabel("Proof V = mean(T, A, E)")
ax[1].set_title("(b) Proof over time", loc="left", fontsize=9.5)
for a in ax:
    a.set_xlabel("Window (1st, 2nd, 3rd; years in labels)"); a.set_xlim(-0.2, 2.6)
ax[1].legend(frameon=False, fontsize=7.5, loc="upper left")
fig.tight_layout(); fig.savefig("figA4_backtest.png", dpi=200, bbox_inches="tight")
