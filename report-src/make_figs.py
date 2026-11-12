"""Figures for the report (light background, print-safe)."""
import json
import pathlib

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = pathlib.Path(__file__).resolve().parent
D = json.loads((HERE.parent / "hvdi" / "site" / "data.json").read_text())
SHORT = {"eth_scaleout": "Ethernet scale-out", "infiniband": "InfiniBand", "uet": "Ultra Ethernet transport",
         "nvlink": "NVLink", "ualink": "UALink (native)", "eth_scaleup": "Ethernet scale-up", "dpu": "Merchant DPU",
         "cpo": "Co-packaged optics", "lpo": "Linear pluggable optics", "aec": "Active electrical cables"}
AHEAD, ALIGNED, INK, GRID = "#B4470F", "#4A5560", "#1A1A1A", "#D9D9D9"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": "#888888"})
cats = [dict(id=c["id"], H=c["scores"]["H"]["v"], V=c["byw"]["equal"]["V"], D=c["byw"]["equal"]["D"],
             lo=c["d05"], hi=c["d95"], cls=c["byw"]["equal"]["cls"]) for c in D["cats"]]

# Figure 1: claimed against proven
fig, ax = plt.subplots(figsize=(6.3, 4.6), dpi=200)
ax.plot([0, 4], [0, 4], color="#888888", lw=1)
ax.plot([0, 3], [1, 4], color="#888888", lw=1, ls="--")
ax.plot([1, 4], [0, 3], color="#888888", lw=1, ls="--")
seen = {}
OFF = {"ualink": (0, 9, "center"), "uet": (0, -15, "center"), "eth_scaleup": (0, 24, "center"),
       "dpu": (22, 42, "center"), "cpo": (14, -28, "center"), "nvlink": (10, 8, "left"),
       "eth_scaleout": (-8, -14, "right"), "infiniband": (-8, -4, "right"), "lpo": (10, 4, "left"), "aec": (10, -10, "left")}
for c in cats:
    key = (c["V"], c["H"]); n = seen.get(key, 0); seen[key] = n + 1
    x = c["V"] + 0.045 * n
    col = AHEAD if c["cls"] == "ahead" else ALIGNED
    ax.scatter([x], [c["H"]], s=46, color=col, zorder=3, edgecolor="white", linewidth=0.8)
    dx, dy, ha = OFF[c["id"]]
    ax.annotate(SHORT[c["id"]], (x, c["H"]), xytext=(dx, dy), textcoords="offset points", fontsize=8, color=INK, ha=ha,
                arrowprops=dict(arrowstyle="-", color="#999999", lw=0.5) if abs(dy) > 20 else None)
ax.set_xlim(0.5, 4.1); ax.set_ylim(1.5, 4.4)
ax.set_xlabel("Proven value V (mean of technical proof, adoption, buyer economics)")
ax.set_ylabel("Claimed maturity H")
ax.set_yticks([2, 3, 4]); ax.grid(color=GRID, lw=0.6); ax.set_axisbelow(True)
ax.text(0.62, 4.27, "Story ahead of proof (D ≥ +1)", fontsize=8, color=AHEAD)
ax.text(3.0, 1.6, "Proof ahead of story (D ≤ −1)", fontsize=8, color=ALIGNED)
for s in ("top", "right"): ax.spines[s].set_visible(False)
fig.tight_layout(); fig.savefig(HERE / "fig1_claimed_vs_proven.png"); plt.close(fig)

# Figure 2: gap with 90% interval
cats.sort(key=lambda c: c["D"])
fig, ax = plt.subplots(figsize=(6.3, 3.9), dpi=200)
ax.axvspan(-1, 1, color="#EEF0F2", zorder=0)
for v in (-1, 1): ax.axvline(v, color="#888888", lw=0.8, ls="--")
for i, c in enumerate(cats):
    col = AHEAD if c["cls"] == "ahead" else ALIGNED
    ax.plot([c["lo"], c["hi"]], [i, i], color=col, lw=2.2, solid_capstyle="round", zorder=2)
    ax.scatter([c["D"]], [i], s=40, color=col, zorder=3, edgecolor="white", linewidth=0.8)
    ax.text(3.25, i, f"{c['D']:+.2f}", va="center", fontsize=8, color=INK)
ax.set_yticks(range(len(cats))); ax.set_yticklabels([SHORT[c["id"]] for c in cats])
ax.set_xlim(-2.2, 3.7); ax.set_xlabel("Gap D = H − V")
ax.grid(axis="x", color=GRID, lw=0.6); ax.set_axisbelow(True)
for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
ax.tick_params(axis="y", length=0)
fig.tight_layout(); fig.savefig(HERE / "fig2_gap_interval.png"); plt.close(fig)
print("figs ok", [(c["id"], c["D"], c["lo"], c["hi"]) for c in cats][:3])
