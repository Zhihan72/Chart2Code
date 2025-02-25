import matplotlib.pyplot as plt
import numpy as np

# Data for Monthly Production Outputs in Megawatt-hours (MWh)
solar = [600, 495, 450, 720, 530, 520, 680, 750, 500, 540, 580, 640]
wind = [570, 480, 530, 380, 520, 590, 350, 620, 450, 410, 410, 490]
hydro = [750, 830, 710, 750, 790, 900, 870, 700, 720, 800, 850, 690]
geothermal = [360, 310, 370, 320, 330, 380, 300, 340, 310, 320, 350, 350]

data = [solar, wind, hydro, geothermal]
single_color = '#f9a825'

fig, ax = plt.subplots(figsize=(10, 6))
bp = ax.boxplot(data, vert=True, patch_artist=True, notch=True, whis=2.0,
                boxprops=dict(color='purple', linewidth=2.0),
                whiskerprops=dict(color='green', linewidth=1.0),
                capprops=dict(color='black', linewidth=2.0),
                medianprops=dict(color='blue', linewidth=3),
                flierprops=dict(marker='x', color='orange', alpha=0.7))

# Apply a single color for each box
for patch in bp['boxes']:
    patch.set_facecolor(single_color)

ax.set_xticklabels(['Solar', 'Wind', 'Hydro', 'Geothermal'])

ax.yaxis.grid(False)
plt.grid(axis='x', linestyle=':', color='grey', alpha=0.5)

plt.tight_layout()
plt.show()