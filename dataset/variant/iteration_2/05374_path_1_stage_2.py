import matplotlib.pyplot as plt
import numpy as np

wax_types = ['Soy Wax', 'Beeswax', 'Paraffin Wax', 'Palm Wax', 'Gel Wax']

soy_wax_weights = [160, 150, 170, 155, 172, 162, 180, 165, 160, 175]
beeswax_weights = [150, 140, 160, 145, 155, 148, 148, 158, 155, 150]
paraffin_weights = [130, 142, 140, 138, 135, 150, 135, 145, 144, 148]
palm_wax_weights = [170, 180, 165, 178, 170, 160, 168, 175, 185, 165]
gel_wax_weights = [128, 135, 130, 132, 132, 120, 130, 125, 138, 128]

data = [soy_wax_weights, beeswax_weights, paraffin_weights, palm_wax_weights, gel_wax_weights]

# Manually shuffled list of colors
colors = ['#8A2BE2', '#20B2AA', '#FF4500', '#FFD700', '#FF6347']

fig, ax = plt.subplots(figsize=(14, 8))

bp = ax.boxplot(data, vert=False, patch_artist=True, notch=True,
                boxprops=dict(linewidth=1.5),
                whiskerprops=dict(linewidth=1.5),
                capprops=dict(linewidth=1.5),
                medianprops=dict(color='black', linewidth=2),
                flierprops=dict(marker='o', color='black', alpha=0.5))

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

ax.set_title('Distribution of Candle Weights by Type of Wax Used\nAmong Local Artisans', fontsize=16, pad=20)
ax.set_xlabel('Weight (grams)', fontsize=12)
ax.set_ylabel('Types of Wax', fontsize=12)
ax.set_yticklabels(wax_types, fontsize=12)

ax.grid(axis='x', linestyle='--', alpha=0.7)

plt.figtext(0.15, 0.85, "Notched boxes indicate 95% CI around the median.", fontsize=10)

plt.tight_layout()

plt.show()