import matplotlib.pyplot as plt
import numpy as np

zones = ['Sunlight', 'Abyssal', 'Hadal']
expeditions = [50, 15, 5]

# Sort the zones and expeditions based on the expeditions in ascending order
sorted_indices = np.argsort(expeditions)
zones_sorted = [zones[i] for i in sorted_indices]
expeditions_sorted = [expeditions[i] for i in sorted_indices]

# Different color for each bar
colors = ['#ff6f61', '#ffa500', '#b565a7']

fig, ax = plt.subplots(figsize=(10, 6))

# Create horizontal bars with varied colors
bars = ax.barh(zones_sorted, expeditions_sorted, color=colors, edgecolor='gray', height=0.6, linestyle='dashdot')

# Set labels and title with different font styles
ax.set_xlabel('Expeditions', fontsize=12, fontweight='light', style='italic', color='darkblue')
ax.set_title('Ocean Depths Exploration (Sorted)', fontsize=16, fontweight='heavy', pad=20, color='darkred')

ax.grid(True, which='major', linestyle='-.', linewidth=0.8, alpha=0.5, axis='both')

# Add a legend
ax.legend(bars, zones_sorted, title="Ocean Zones", loc='upper right', fontsize=8)

# Annotate bar values
for bar, color in zip(bars, colors):
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2, f'{width}', va='center', fontsize=9, color='gray', backgroundcolor=color)

# Adjust y-ticks
ax.set_yticks(np.arange(len(zones_sorted)))

plt.tight_layout()
plt.show()