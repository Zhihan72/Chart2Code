import numpy as np
import matplotlib.pyplot as plt

solar = np.array([
    5, 10, 15, 20, 30, 45, 60, 85, 110, 140, 
    175, 215, 250, 295, 350, 410, 475, 550, 640, 740, 850
])
wind = np.array([
    10, 15, 20, 30, 45, 60, 75, 90, 110, 130, 
    155, 185, 220, 265, 320, 380, 450, 530, 620, 720, 830
])

energy_data = [solar, wind]
labels = ['Solar', 'Wind']

fig, ax = plt.subplots(figsize=(14, 8))

# Updated color for the boxplots
box_colors = ['#FF5733', '#33FF57']  # New set of colors: orange-red and green

ax.boxplot(energy_data, vert=False, patch_artist=True,
           labels=labels, boxprops=dict(facecolor=box_colors[0], alpha=0.75))

# Apply a custom color for each boxplot to distinguish them
for patch, color in zip(ax.artists, box_colors):
    patch.set_facecolor(color)

ax.set_title("Renewable Energy Generation Over Time", fontsize=18, fontweight='bold')
ax.set_xlabel('Adoption (GW)', fontsize=14)

ax.grid(linestyle=':', alpha=0.7)

plt.tight_layout()
plt.show()