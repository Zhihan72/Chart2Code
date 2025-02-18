import matplotlib.pyplot as plt
import numpy as np

bodies = ['Merc', 'Earth', 'Moon', 'Mars', 'Eur', 'Titan']

water_data = [
    [0.1, 0.1, 0.2, 0.2, 0.1],          # Mercury
    # Removed Venus Data
    [70.0, 68.0, 72.0, 71.0, 69.0],     # Earth
    [0.1, 0.2, 0.1, 0.3, 0.2],          # Moon
    [2.0, 2.1, 2.2, 2.0, 2.1],          # Mars
    [52.5, 53.0, 52.0, 53.5, 52.3],     # Europa
    [40.0, 41.0, 40.5, 41.5, 40.3]      # Titan
]

fig, ax = plt.subplots(figsize=(12, 8))

box = ax.boxplot(water_data, patch_artist=True, notch=True, vert=False, labels=bodies)

single_color = '#00CED1'
for patch in box['boxes']:
    patch.set_facecolor(single_color)

plt.setp(box['medians'], color='blue', linestyle='--', linewidth=2)

ax.set_title("Planetary Water %", fontsize=18, fontweight='normal', pad=15)
ax.set_xlabel("Water %", fontsize=14)
ax.set_ylabel("Bodies", fontsize=14)

ax.grid(visible=True, linestyle='-', alpha=0.3, which='minor', linewidth=0.5)

for i, body in enumerate(bodies):
    max_val = max(water_data[i])
    ax.text(max_val + 2, i + 1, f'Max: {max_val:.1f}%', va='center', fontsize=9, color='black')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()