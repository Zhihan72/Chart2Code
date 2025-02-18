import matplotlib.pyplot as plt
import squarify
import numpy as np

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
    }
}

years = np.arange(2015, 2023)
growth_trends = {
    "PlayStation": [30, 32, 34, 35, 36, 38, 40, 42],
    "Xbox": [20, 22, 23, 25, 27, 28, 30, 32],
    "Nintendo": [18, 19, 18, 20, 22, 23, 24, 25],
    "Steam": [40, 42, 44, 46, 48, 50, 52, 54],
    "Epic Games": [10, 12, 14, 16, 18, 19, 20, 21],
    "Blizzard": [14, 15, 14, 15, 16, 15, 16, 17]
}

labels = []
sizes = []
colors = ["#c2f0c2", "#ff9999", "#ffb3e6", "#66b3ff", "#ffcc99", "#99ff99"]
for category, subcategories in gaming_platforms.items():
    for subcategory, size in subcategories.items():
        labels.append(f"{subcategory}\n({size}%)")
        sizes.append(size)

fig, ax1 = plt.subplots(figsize=(14, 9))

squarify.plot(sizes=sizes, label=labels, color=colors[:len(labels)], alpha=0.8, ax=ax1, edgecolor='grey', linewidth=1.5)
ax1.set_title("Global Market Distribution of Gaming Platforms\nAnd Growth Trends (2015-2022)", fontsize=16, fontweight='bold', pad=20)
ax1.axis('off')

ax2 = ax1.twinx()
markers = ['o', 's', '^', 'v', 'D', '*']
linestyles = ['-', '--', '-.', ':', '-', '--']
for (platform, growth), marker, linestyle in zip(growth_trends.items(), markers, linestyles):
    ax2.plot(years, growth, marker=marker, linestyle=linestyle, label=platform)

ax2.set_ylabel('Growth in Market Share (%)', fontsize=12)
ax2.set_xlabel('Years', fontsize=12)
ax2.grid(True, linestyle='--', linewidth=0.5)
ax2.legend(title='Growth Trends', loc='lower left', fontsize=9)

plt.tight_layout()
plt.show()