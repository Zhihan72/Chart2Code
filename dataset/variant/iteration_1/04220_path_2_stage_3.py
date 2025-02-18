import numpy as np
import matplotlib.pyplot as plt
from math import pi

categories = ['Atk', 'Def', 'Mgc', 'Spd', 'HP']
num_vars = len(categories)

warrior = [8, 9, 2, 5, 10]
mage = [3, 4, 10, 6, 4]
rogue = [7, 5, 3, 10, 6]
ranger = [6, 6, 5, 8, 7]

data = [warrior, mage, rogue, ranger]
colors = ['red', 'blue', 'green', 'purple']

angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

def plot_radar_chart(ax, data, color):
    data += data[:1]  # Completes the loop on the radar chart
    ax.plot(angles, data, color=color, linewidth=2)
    ax.fill(angles, data, color=color, alpha=0.25)  # Fills the area inside the radar chart

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each class in the radar chart
for idx, class_data in enumerate(data):
    plot_radar_chart(ax, class_data, colors[idx])

# Remove inner y-ticks
ax.set_yticks([])

# Set category labels on the radar chart
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10, color='black', weight='bold')

plt.tight_layout()
plt.show()