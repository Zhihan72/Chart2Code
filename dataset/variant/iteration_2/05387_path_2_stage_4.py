import matplotlib.pyplot as plt
import numpy as np

# Data for Monthly Production Outputs in Megawatt-hours (MWh)
solar = [450, 520, 495, 530, 600, 680, 750, 720, 640, 580, 540, 500]
wind = [350, 380, 410, 480, 520, 570, 620, 590, 530, 490, 450, 410]
hydro = [700, 690, 720, 750, 800, 850, 900, 870, 830, 790, 750, 710]
geothermal = [310, 300, 320, 330, 350, 360, 380, 370, 350, 340, 320, 310]

data = [solar, wind, hydro, geothermal]
single_color = '#f9a825'  # Using a single color consistently

fig, ax = plt.subplots(figsize=(10, 6))

# Plot a vertical boxplot with customized colors
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