import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

enrollments = {
    "Anthropology": [300, 320, 340, 360, 380, 400, 450, 470, 480, 490, 500],
    "Sociology": [280, 290, 310, 330, 350, 370, 390, 420, 450, 460, 470],
    "History": [260, 270, 280, 300, 320, 340, 360, 370, 380, 400, 410],
    "Philosophy": [240, 250, 260, 280, 300, 320, 330, 340, 350, 360, 370],
    "Literature": [220, 230, 240, 250, 270, 290, 310, 320, 330, 340, 350],
}

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

fig, ax = plt.subplots(figsize=(16, 10))

x = np.arange(len(years))

neg_offsets = np.zeros_like(years)
pos_offsets = np.zeros_like(years)

# Changed marker style
marker_styles = ['o', 'v', '^', '<', '>']

for i, (discipline, counts) in enumerate(enrollments.items()):
    pos_bars = np.array(counts) > 340
    ax.barh(x[pos_bars], np.array(counts)[pos_bars] - 340, left=pos_offsets[pos_bars], 
            color=colors[i], label=discipline, edgecolor='black', hatch=marker_styles[i % len(marker_styles)])
    pos_offsets[pos_bars] += np.array(counts)[pos_bars] - 340

    ax.barh(x[~pos_bars], 340 - np.array(counts)[~pos_bars], left=neg_offsets[~pos_bars], 
            color=colors[i], edgecolor='grey', hatch=marker_styles[(i+1) % len(marker_styles)])
    neg_offsets[~pos_bars] += 340 - np.array(counts)[~pos_bars]

# Modified central axis indicator with a different linestyle and linewidth
ax.axvline(0, color='red', linestyle=':', linewidth=1.5)

# Added grid lines with different style
ax.grid(visible=True, linestyle='--', color='grey', alpha=0.7)

ax.set_title("Diverging Bar Chart of Student Enrollments from 2010 to 2020", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Number of Enrollments (Deviation from 340)", fontsize=12)
ax.set_yticks(x)
ax.set_yticklabels(years, fontsize=10)

# Changed legend location and frame
ax.legend(title="Disciplines", loc='lower right', frameon=False)

plt.tight_layout()
plt.show()