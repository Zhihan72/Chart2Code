import matplotlib.pyplot as plt
import numpy as np

# Define zones and corresponding counts
zones = ['Sunlight', 'Twilight', 'Midnight', 'Abyssal', 'Hadal']
expeditions = [50, 35, 20, 15, 5]

# Sort the zones and expeditions based on expeditions in ascending order
sorted_indices = np.argsort(expeditions)
zones_sorted = [zones[i] for i in sorted_indices]
expeditions_sorted = [expeditions[i] for i in sorted_indices]

# Use a single color for all bars
single_color = '#1f77b4'

fig, ax = plt.subplots(figsize=(10, 6))

# Create horizontal bars
bars = ax.barh(zones_sorted, expeditions_sorted, color=single_color, edgecolor='black', height=0.6)

# Set labels and title
ax.set_xlabel('Expeditions', fontsize=12, fontweight='bold')
ax.set_title('Ocean Depths Exploration (Sorted)', fontsize=14, fontweight='bold', pad=15)

# Add grid for x-axis
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7, axis='x')

# Annotate bar values
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2, f'{width}', va='center', fontsize=10, fontweight='bold', color='black')

# Set y-ticks
ax.set_yticks(np.arange(len(zones_sorted)))
ax.set_yticklabels(zones_sorted, ha='center', fontsize=11)

plt.tight_layout()
plt.show()