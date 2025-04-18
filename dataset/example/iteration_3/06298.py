import matplotlib.pyplot as plt
import squarify
import numpy as np

# Backstory: We will create a visualization of the global market distribution of gaming platforms and their growth trends over time.
# The treemap will show the market share of various gaming platforms, and an added line plot will represent 
# the growth trend of each platform from 2015 to 2022.

# Define data for gaming platforms and their market shares
gaming_platforms = {
    "Console Gaming": {
        "PlayStation": 35,
        "Xbox": 25,
        "Nintendo": 20
    },
    "PC Gaming": {
        "Steam": 50,
        "Epic Games": 20,
        "Blizzard": 15
    },
    "Mobile Gaming": {
        "iOS": 30,
        "Android": 45
    }
}

# Growth data for overlay plot (hypothetical, directly constructed)
years = np.arange(2015, 2023)
growth_trends = {
    "PlayStation": [30, 32, 34, 35, 36, 38, 40, 42],
    "Xbox": [20, 22, 23, 25, 27, 28, 30, 32],
    "Nintendo": [18, 19, 18, 20, 22, 23, 24, 25],
    "Steam": [40, 42, 44, 46, 48, 50, 52, 54],
    "Epic Games": [10, 12, 14, 16, 18, 19, 20, 21],
    "Blizzard": [14, 15, 14, 15, 16, 15, 16, 17],
    "iOS": [25, 27, 29, 29, 31, 32, 33, 34],
    "Android": [40, 42, 44, 45, 46, 47, 48, 49]
}

# Prepare treemap data
labels = []
sizes = []
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6", "#ff6666", "#c2f0c2"]
for category, subcategories in gaming_platforms.items():
    for subcategory, size in subcategories.items():
        labels.append(f"{subcategory}\n({size}%)")
        sizes.append(size)

# Create figure and axis for treemap
fig, ax1 = plt.subplots(figsize=(14, 9))

# Plot the treemap
squarify.plot(sizes=sizes, label=labels, color=colors[:len(labels)], alpha=0.8, ax=ax1, edgecolor='black', linewidth=1)
ax1.set_title("Global Market Distribution of Gaming Platforms\nAnd Growth Trends (2015-2022)", fontsize=16, fontweight='bold', pad=20)
ax1.axis('off')

# Add overlay plot (Growth trends)
ax2 = ax1.twinx()  # Create a secondary y-axis
for platform, growth in growth_trends.items():
    ax2.plot(years, growth, marker='o', linestyle='-', label=platform)

# Overlay plot configurations
ax2.set_ylabel('Growth in Market Share (%)', fontsize=12)
ax2.set_xlabel('Years', fontsize=12)
ax2.grid(False)
ax2.legend(title='Growth Trends', loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()