import matplotlib.pyplot as plt
import numpy as np

wax_types = ['Soy Wax', 'Beeswax', 'Paraffin Wax', 'Palm Wax', 'Gel Wax']

soy_wax_weights = [160, 150, 170, 155, 172, 162, 180, 165, 160, 175]
beeswax_weights = [150, 140, 160, 145, 155, 148, 148, 158, 155, 150]
paraffin_weights = [130, 142, 140, 138, 135, 150, 135, 145, 144, 148]
palm_wax_weights = [170, 180, 165, 178, 170, 160, 168, 175, 185, 165]
gel_wax_weights = [128, 135, 130, 132, 132, 120, 130, 125, 138, 128]

data = [soy_wax_weights, beeswax_weights, paraffin_weights, palm_wax_weights, gel_wax_weights]

# Shuffled list of colors
colors = ['#FF6347', '#FFD700', '#20B2AA', '#8A2BE2', '#FF4500']

fig, ax = plt.subplots(figsize=(12, 7))

bp = ax.boxplot(data, vert=False, patch_artist=True, notch=True,
                boxprops=dict(linewidth=2.0, linestyle='-.'),  # Changed line style
                whiskerprops=dict(linewidth=2.0, linestyle='-.'),  # Changed line style
                capprops=dict(linewidth=2.0, linestyle='-.'),  # Changed line style
                medianprops=dict(color='blue', linewidth=2),  # Changed median color
                flierprops=dict(marker='*', color='blue', alpha=0.7))  # Changed marker type and color

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

ax.set_title('Candle Weight Distribution by Wax Type\nAmong Local Artisans', fontsize=14, pad=15)
ax.set_xlabel('Weight (grams)', fontsize=11)
ax.set_ylabel('Wax Types', fontsize=11)
ax.set_yticklabels(wax_types, fontsize=11)

ax.grid(axis='x', linestyle=':', alpha=0.5)  # Changed grid style and transparency

plt.figtext(0.13, 0.89, "Notched boxes indicate 95% CI around the median.", fontsize=10)

plt.tight_layout()

plt.show()