import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

enrollments = {
    "Anthro": [300, 320, 340, 360, 380, 400, 450, 470, 480, 490, 500],
    "Socio": [280, 290, 310, 330, 350, 370, 390, 420, 450, 460, 470],
    "History": [260, 270, 280, 300, 320, 340, 360, 370, 380, 400, 410],
    "Lit": [220, 230, 240, 250, 270, 290, 310, 320, 330, 340, 350],
}

# New set of colors for the bars
colors = ['#e69f00', '#56b4e9', '#f0e442', '#009e73']

fig, ax = plt.subplots(figsize=(16, 10))

x = np.arange(len(years))

neg_offsets = np.zeros_like(years)
pos_offsets = np.zeros_like(years)

marker_styles = ['o', 'v', '^', '<']

for i, (discipline, counts) in enumerate(enrollments.items()):
    pos_bars = np.array(counts) > 340
    ax.barh(x[pos_bars], np.array(counts)[pos_bars] - 340, left=pos_offsets[pos_bars], 
            color=colors[i], label=discipline, edgecolor='black', hatch=marker_styles[i % len(marker_styles)])
    pos_offsets[pos_bars] += np.array(counts)[pos_bars] - 340

    ax.barh(x[~pos_bars], 340 - np.array(counts)[~pos_bars], left=neg_offsets[~pos_bars], 
            color=colors[i], edgecolor='grey', hatch=marker_styles[(i+1) % len(marker_styles)])
    neg_offsets[~pos_bars] += 340 - np.array(counts)[~pos_bars]

ax.axvline(0, color='red', linestyle=':', linewidth=1.5)
ax.grid(visible=True, linestyle='--', color='grey', alpha=0.7)

ax.set_title("Enrollments 2010-2020", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Deviation from 340", fontsize=12)
ax.set_yticks(x)
ax.set_yticklabels(years, fontsize=10)

ax.legend(title="Disciplines", loc='lower right', frameon=False)

plt.tight_layout()
plt.show()