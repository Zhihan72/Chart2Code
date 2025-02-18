import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import seaborn as sns

sns.set_theme(style="whitegrid")

regions = ['Solaria', 'Ventara', 'Aqua-Land', 'Geothermica', 'BioBoost', 'HydroHaven']
solaria_energy = [320, 300, 310, 305, 315, 330, 335, 325, 340, 330, 325, 335]
ventara_energy = [250, 260, 245, 255, 265, 270, 275, 260, 255, 250, 265, 270]
aqua_land_energy = [180, 190, 185, 175, 195, 200, 205, 195, 200, 190, 185, 195]
geothermica_energy = [140, 135, 145, 140, 150, 155, 160, 155, 150, 145, 140, 155]
bioboost_energy = [280, 275, 285, 290, 295, 305, 310, 300, 305, 310, 300, 295]
hydrohaven_energy = [160, 155, 165, 160, 170, 175, 180, 175, 170, 165, 160, 175]

energy_data = [solaria_energy, ventara_energy, aqua_land_energy, geothermica_energy, bioboost_energy, hydrohaven_energy]

fig, ax = plt.subplots(figsize=(12, 8))

boxplots = ax.boxplot(energy_data, vert=True, patch_artist=True, showmeans=True, notch=True)

colors = ['#FFD700', '#87CEEB', '#8A2BE2', '#FF8C00', '#DA70D6', '#32CD32']
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
    ax.text(i, q1 - 5, f"Q1: {q1:.1f}", ha='center', fontsize=10, color='#333333')
    ax.text(i, q3 + 5, f"Q3: {q3:.1f}", ha='center', fontsize=10, color='#333333')

ax.set_title('Monthly Renewable Energy Production in 2023\nAcross Six Regions', fontsize=16, pad=15)
ax.set_ylabel('Energy Production (GWh)', fontsize=12)
ax.set_xticks(range(1, len(regions) + 1))
ax.set_xticklabels(regions, fontsize=12)

ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))

ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.xaxis.grid(False)

highlight_levels = [150, 250, 350]
for level in highlight_levels:
    ax.axhline(level, color='red', linestyle='--', linewidth=0.8, alpha=0.5)

from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=color, edgecolor='r', label=region) for color, region in zip(colors, regions)]
legend_elements.extend([Patch(facecolor='none', edgecolor='r', linestyle='--', label=f"Highlight: {level} GWh") for level in highlight_levels])
ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, title="Regions & Highlights")

plt.tight_layout()
plt.show()