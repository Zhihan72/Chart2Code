import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

steps = [
    "Intro Request",
    "Drive Test",
    "Completion of Test Drive",
    "Negotiation on Price",
    "EV Delivered",
    "Ownership for Over Half a Year"
]

consumer_counts = np.array([5000, 3800, 3500, 2900, 2000, 1700])

widths = consumer_counts / consumer_counts[0]

colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#a65628', '#f781bf']

fig, ax = plt.subplots(figsize=(12, 10))

for i in range(len(steps)):
    top_width = widths[i-1] if i > 0 else 1.0
    bottom_width = widths[i]
    
    trapezoid = patches.Polygon(
        [
            [(1 - top_width) / 2, i], [(1 + top_width) / 2, i], 
            [(1 + bottom_width) / 2, i + 1], [(1 - bottom_width) / 2, i + 1]
        ], closed=True, color=colors[i]
    )
    ax.add_patch(trapezoid)
    
    ax.text(0.5, i + 0.5, f"{steps[i]}\n{consumer_counts[i]} Persons",
            ha='center', va='center', fontsize=11, color='black', weight='bold')

ax.set_xlim(0, 1)
ax.set_ylim(0, len(steps))
ax.axis('off')

plt.tight_layout()
plt.show()