import matplotlib.pyplot as plt
import numpy as np

planetary_labels = ['Moon', 'Titan', 'Mars', 'Mercury', 'Europa', 'Earth', 'Venus']

water_content_data = [
    [0.1, 0.2, 0.1, 0.3, 0.2],
    [40.0, 41.0, 40.5, 41.5, 40.3],
    [2.0, 2.1, 2.2, 2.0, 2.1],
    [0.1, 0.1, 0.2, 0.2, 0.1],
    [52.5, 53.0, 52.0, 53.5, 52.3],
    [70.0, 68.0, 72.0, 71.0, 69.0],
    [0.0, 0.0, 0.1, 0.1, 0.0]
]

fig, ax = plt.subplots(figsize=(12, 8))
box = ax.boxplot(water_content_data, patch_artist=True, notch=False, vert=False, labels=planetary_labels)

colors = ['#FFD700', '#BA55D3', '#FF6347', '#FFA07A', '#98FB98', '#1E90FF', '#FF4500']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.setp(box['medians'], color='black')

ax.set_title("Hydration Analysis: Surface Water Levels on Celestial Objects", 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Percentage of Water", fontsize=12)
ax.set_ylabel("Celestial Labels", fontsize=12)

ax.grid(True, linestyle='--', alpha=0.5, which='both', linewidth=0.7)

for i, (planet, data) in enumerate(zip(planetary_labels, water_content_data)):
    max_val = max(data)
    ax.text(max_val + 3, i + 1, f'Peak: {max_val:.1f}%', va='center', fontsize=10, color=colors[i])

plt.tight_layout()
plt.show()