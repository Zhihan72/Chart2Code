import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import seaborn as sns

sns.set_theme(style="whitegrid")

regions = ['Sunland', 'Windy Valley', 'Waterfront', 'Earthcore']
sunland_energy = [320, 300, 310, 305, 315, 330, 335, 325, 340, 330, 325, 335]
windy_valley_energy = [250, 260, 245, 255, 265, 270, 275, 260, 255, 250, 265, 270]
waterfront_energy = [180, 190, 185, 175, 195, 200, 205, 195, 200, 190, 185, 195]
earthcore_energy = [140, 135, 145, 140, 150, 155, 160, 155, 150, 145, 140, 155]

energy_data = [sunland_energy, windy_valley_energy, waterfront_energy, earthcore_energy]

fig, ax = plt.subplots(figsize=(12, 8))

boxplots = ax.boxplot(energy_data, vert=True, patch_artist=True, showmeans=True, notch=True)

# New set of colors
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']
for patch, color in zip(boxplots['boxes'], colors):
    patch.set(facecolor=color, alpha=0.6)

for whisker in boxplots['whiskers']:
    whisker.set(color='#7570b3', linewidth=2, linestyle='--')
for cap in boxplots['caps']:
    cap.set(color='#7570b3', linewidth=2)
for median in boxplots['medians']:
    median.set(color='green', linewidth=2)
for mean in boxplots['means']:
    mean.set(marker='o', color='blue', markersize=6)

for i, region_data in enumerate(energy_data, start=1):
    q1, q3 = np.percentile(region_data, [25, 75])
    ax.text(i, q1 - 5, f"25th Pct: {q1:.1f}", ha='center', fontsize=10, color='#333333')
    ax.text(i, q3 + 5, f"75th Pct: {q3:.1f}", ha='center', fontsize=10, color='#333333')

ax.set_title('2023 Renewable Energy Output Overview\nFrom Various Territories', fontsize=16, pad=15)
ax.set_ylabel('Output Volume (Gigawatts)', fontsize=12)
ax.set_xticks([1, 2, 3, 4])
ax.set_xticklabels(regions, fontsize=12)

ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.xaxis.grid(False)

highlight_levels = [150, 250, 350]
for level in highlight_levels:
    ax.axhline(level, color='red', linestyle='--', linewidth=0.8, alpha=0.5)

from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=color, edgecolor='r', label=region) for color, region in zip(colors, regions)]
legend_elements.extend([Patch(facecolor='none', edgecolor='r', linestyle='--', label=f"Level: {level} GWh") for level in highlight_levels])
ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, title="Territories & Levels")

plt.tight_layout()
plt.show()