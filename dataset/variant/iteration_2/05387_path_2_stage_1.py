import matplotlib.pyplot as plt
import numpy as np

# Data for Monthly Production Outputs in Megawatt-hours (MWh)
solar = [450, 520, 495, 530, 600, 680, 750, 720, 640, 580, 540, 500]
wind = [350, 380, 410, 480, 520, 570, 620, 590, 530, 490, 450, 410]
hydro = [700, 690, 720, 750, 800, 850, 900, 870, 830, 790, 750, 710]
geothermal = [310, 300, 320, 330, 350, 360, 380, 370, 350, 340, 320, 310]

data = [solar, wind, hydro, geothermal]
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal']
colors = ['#f9a825', '#1e88e5', '#81c784', '#ff7043']

fig, ax = plt.subplots(figsize=(10, 6))

# Plot a vertical boxplot with customized colors
bp = ax.boxplot(data, vert=True, patch_artist=True, notch=False, whis=1.5,
                boxprops=dict(color='black', linewidth=1.5),
                whiskerprops=dict(color='black', linewidth=1.5),
                capprops=dict(color='black', linewidth=1.5),
                medianprops=dict(color='red', linewidth=2),
                flierprops=dict(marker='o', color='black', alpha=0.5))

# Set colors for each box
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

ax.set_title('Monthly Renewable Energy Production (2022)', fontsize=14, pad=20)
ax.set_ylabel('Monthly Production Output (MWh)', fontsize=12)
ax.set_xlabel('Energy Source', fontsize=12)
ax.set_xticklabels(energy_sources, fontsize=10)

ax.yaxis.grid(True, linestyle='--', color='grey', alpha=0.7)

plt.tight_layout()
plt.show()