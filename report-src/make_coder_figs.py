"""Appendix 10 figures: human second coding (five coders, 30 claims). Not part of the public repo."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "axes.spines.top": False, "axes.spines.right": False})
BLUE, ORANGE, GREEN, GREY, PURPLE = "#2A6FB0", "#C24E12", "#4E9A6B", "#8A867A", "#7B5EA7"
coders = ["C1", "C2", "C3", "C4", "C5", "Majority"]
kind = [67, 57, 53, 57, 80, 73]; exact = [65, 59, 75, 35, 38, 64]; within = [95, 100, 94, 88, 83, 100]
qwk = [0.70, 0.71, 0.77, 0.37, 0.40, 0.82]

fig, ax = plt.subplots(1, 2, figsize=(10.4, 3.6), gridspec_kw={"width_ratios": [1.35, 1]})
w = 0.26
for i, (vals, lab, col) in enumerate(((kind, "Same kind (stage or narrative)", BLUE), (exact, "Same level (where kind matched)", ORANGE), (within, "Within one level", GREEN))):
    xs = [x + (i - 1) * w for x in range(len(coders))]
    ax[0].bar(xs, vals, w * 0.92, color=col, label=lab)
ax[0].set_xticks(range(len(coders))); ax[0].set_xticklabels(coders); ax[0].set_ylim(0, 118); ax[0].set_ylabel("Agreement with first coder (%)")
ax[0].grid(axis="y", color="#E3E1DA", lw=0.6); ax[0].set_axisbelow(True)
ax[0].legend(frameon=False, fontsize=7.5, loc="upper left", ncol=3)
ax[0].set_title("(a) Agreement with the first coder", loc="left", fontsize=9.5)
labels = ["C1 vs first coder", "C2 vs first coder", "C3 vs first coder", "C4 vs first coder", "C5 vs first coder", "Majority vs first coder", "Among coders: Fleiss κ (kind)", "Among coders: Krippendorff α (level)"]
vals = qwk + [0.16, 0.51]
cols = [BLUE] * 5 + [ORANGE] + [PURPLE, PURPLE]
for lo, hi, name in ((0, 0.2, "slight"), (0.2, 0.4, "fair"), (0.4, 0.6, "moderate"), (0.6, 0.8, "substantial"), (0.8, 1.0, "almost\nperfect")):
    ax[1].axvspan(lo, hi, color=GREY, alpha=0.03 + 0.025 * (lo * 5))
    ax[1].text((lo + hi) / 2, -0.95, name, fontsize=6.5, color=GREY, ha="center", va="center")
ys = list(range(len(labels)))[::-1]
ax[1].barh(ys, vals, 0.65, color=cols)
for y, v in zip(ys, vals):
    ax[1].text(v + 0.015, y, f"{v:.2f}", va="center", fontsize=7.5)
ax[1].set_yticks(ys); ax[1].set_yticklabels(labels, fontsize=7.5); ax[1].set_xlim(0, 1); ax[1].set_ylim(-1.4, len(labels) - 0.4)
ax[1].set_xlabel("Coefficient (0 = chance, 1 = perfect); bands: Landis & Koch (1977)", fontsize=7)
ax[1].set_title("(b) Agreement coefficients", loc="left", fontsize=9.5, pad=22)
fig.tight_layout(); fig.savefig("figA1_coder_agreement.png", dpi=220, bbox_inches="tight"); plt.close(fig)

# A2: gap per reading for the two story-ahead technologies
readers = ["First\ncoder", "C1", "C2", "C3", "C4", "C5", "Majority"]
D = {"NVLink": [1.33, 0.33, 1.33, 1.33, 0.33, -0.67, 1.33], "Native UALink": [1.00, 1.00, 2.00, 0.00, 1.00, 0.00, 1.00]}
fig, ax = plt.subplots(figsize=(8.6, 3.0))
for j, (tech, ys) in enumerate(D.items()):
    xs = [x + (j - 0.5) * 0.22 for x in range(len(readers))]
    ax.scatter(xs, ys, s=[70 if y >= 1 else 40 for y in ys], color=[ORANGE if y >= 1 else GREY for y in ys], marker="o" if j == 0 else "D", zorder=3, label=tech)
ax.axhline(1, color=ORANGE, lw=1, ls="--"); ax.text(3.0, 1.07, "story-ahead threshold (D = +1)", fontsize=7.5, color=ORANGE, ha="center")
ax.axhline(-1, color=BLUE, lw=0.8, ls=":")
ax.set_xticks(range(len(readers))); ax.set_xticklabels(readers); ax.set_ylabel("Gap D = H − V"); ax.set_ylim(-1.3, 2.75)
ax.grid(axis="y", color="#E3E1DA", lw=0.6); ax.set_axisbelow(True)
from matplotlib.lines import Line2D
ax.legend(handles=[Line2D([], [], marker="o", ls="", color=GREY, label="NVLink"), Line2D([], [], marker="D", ls="", color=GREY, label="Native UALink"),
                   Line2D([], [], marker="s", ls="", color=ORANGE, label="story ahead"), Line2D([], [], marker="s", ls="", color=GREY, label="aligned")],
          frameon=False, fontsize=8, ncol=4, loc="upper left")
fig.tight_layout(); fig.savefig("figA2_coder_verdicts.png", dpi=220, bbox_inches="tight"); plt.close(fig)

# A3: sensitivity
cases = ["Report stability\n(claim resampling)", "Coders' average reading\n(one level lower, p = 0.40)", "Most cautious coder\n(one level lower, p = 0.70)"]
nv = [58, 20, 3]; ua = [61, 35, 9]
fig, ax = plt.subplots(figsize=(8.0, 2.9))
for i, (vals, lab, col) in enumerate(((nv, "NVLink", ORANGE), (ua, "Native UALink", PURPLE))):
    xs = [x + (i - 0.5) * 0.34 for x in range(3)]
    ax.bar(xs, vals, 0.32, color=col, label=lab)
    for x, v in zip(xs, vals):
        ax.text(x, v + 1.5, f"{v}%", ha="center", fontsize=8)
ax.set_xticks(range(3)); ax.set_xticklabels(cases, fontsize=8); ax.set_ylim(0, 75); ax.set_ylabel("Draws keeping 'story ahead' (%)")
ax.grid(axis="y", color="#E3E1DA", lw=0.6); ax.set_axisbelow(True); ax.legend(frameon=False, fontsize=8)
fig.tight_layout(); fig.savefig("figA3_coder_sensitivity.png", dpi=220, bbox_inches="tight"); plt.close(fig)
print("ok")
