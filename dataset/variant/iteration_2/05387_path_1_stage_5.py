import matplotlib.pyplot as plt
import numpy as np

solar = [450, 520, 495, 530, 600, 680, 750, 720, 640, 580, 540, 500]
wind = [350, 380, 410, 480, 520, 570, 620, 590, 530, 490, 450, 410]
hydro = [700, 690, 720, 750, 800, 850, 900, 870, 830, 790, 750, 710]

# Combining all data into a single list for a single boxplot
data_combined = solar + wind + hydro

fig, ax = plt.subplots(figsize=(8, 14))

# Drawing a vertical boxplot of the combined data
bp = ax.boxplot(data_combined, vert=True, patch_artist=True, notch=False, widths=0.4,
                boxprops=dict(facecolor='lightgray', color='black', linewidth=1.5),
                whiskerprops=dict(color='black', linewidth=1.5),
                capprops=dict(color='black', linewidth=1.5),
                medianprops=dict(color='red', linewidth=2),
                flierprops=dict(marker='o', color='black', alpha=0.5))

plt.tight_layout()
plt.show()