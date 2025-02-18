import matplotlib.pyplot as plt
import numpy as np

# Decades for the x-axis
decades = ['1980s', '2000s', '2020s']

# Data for travel types over the decades
adventure = np.array([10, 20, 30])
cultural = np.array([30, 30, 25])
relaxation = np.array([40, 35, 40])

# Stack the data
data = np.vstack([adventure, cultural, relaxation])

# Color configuration for the layers
colors = ['#ffcc99', '#99ff99', '#66b3ff']

# Initialize the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Stacked area plot with altered linestyle for adventure
ax.stackplot(decades, data[0], labels=['Adventure Travel'], colors=colors[:1], linestyle='dotted', alpha=0.8)
ax.stackplot(decades, data[1:], labels=['Cultural Travel', 'Relaxation Travel'], colors=colors[1:], alpha=0.8)

# Title and labels
ax.set_title('Evolution of Travel Preferences\nAcross Decades', fontsize=18, weight='bold', pad=20)
ax.set_xlabel('Decade', fontsize=14, labelpad=15)
ax.set_ylabel('Percentage Share of Travel Type', fontsize=14, labelpad=15)

# Legend configuration with altered location and no legend title
ax.legend(loc='lower right', fontsize=11, bbox_to_anchor=(1, 0))

# Adding grid lines with altered orientation
ax.grid(axis='x', linestyle='-.', alpha=0.5)

# Set yticks without percentage labels
ax.set_yticks(np.arange(0, 101, 10))

# Alter the x-ticks and rotate them for dramatic effect
ax.set_xticks(decades)
ax.set_xticklabels(decades, rotation=45, fontsize=11)

# Remove all spines except left
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()