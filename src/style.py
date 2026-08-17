from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

OUTPUT_DIR = Path.home() / "TFM QMUL" / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

PRIMARY_COLOR = "#4D5966"
SECONDARY_COLOR = "#D98986"
INTERVAL_FILL = "#E7EBF0"
EVENT_FILL = "#F2DDDB"
GRID_COLOR = "#D9DEE3"
DARK_TEXT = "#2E2E2E"

HEATMAP_CMAP = LinearSegmentedColormap.from_list(
    "rose_only", ["#F7F1F1", "#E7B6B4", "#D98986", "#A76562", "#68403F"]
)

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
    "font.size": 10,
    "axes.titlesize": 13,
    "axes.labelsize": 13,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,
    "legend.fontsize": 11,
    "axes.linewidth": 0.8,
    "lines.linewidth": 1.8,
    "lines.markersize": 5.5,
    "xtick.major.width": 0.8,
    "ytick.major.width": 0.8,
    "xtick.major.size": 3.5,
    "ytick.major.size": 3.5,
    "figure.dpi": 140,
    "savefig.dpi": 600,
    "savefig.bbox": "tight",
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "svg.fonttype": "none",
})


def finish_axis(ax, grid_axis="both"):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    if grid_axis:
        ax.grid(axis=grid_axis, color=GRID_COLOR, linewidth=0.65, alpha=0.75)
    ax.set_axisbelow(True)


def save_figure(fig, stem):
    stem = OUTPUT_DIR / stem
    for extension in ("png", "pdf", "svg"):
        fig.savefig(stem.with_suffix(f".{extension}"), dpi=600, bbox_inches="tight")
    print("Saved:", stem)
