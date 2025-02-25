import matplotlib.pyplot as plt
import squarify
import numpy as np

gaming_platforms = {
    "Console Gaming": {
        "PlayStation": 20,
        "Xbox": 35,
        "Nintendo": 25
    },
    "PC Gaming": {
        "Steam": 20,
        "Epic Games": 50,
        "Blizzard": 15
    },
    "Mobile Gaming": {
        "iOS": 45,
        "Android": 30
    }
}

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

labels = []
sizes = []
new_colors = ["#e6194b", "#3cb44b", "#ffe119", "#4363d8", "#f58231", "#911eb4", "#46f0f0", "#f032e6"]
for category, subcategories in gaming_platforms.items():
    for subcategory, size in subcategories.items():
        labels.append(f"{subcategory}\n({size}%)")
        sizes.append(size)

fig, ax1 = plt.subplots(figsize=(14, 9))
squarify.plot(sizes=sizes, label=labels, color=new_colors[:len(labels)], alpha=0.8, ax=ax1, edgecolor='darkblue', linewidth=1.5)
ax1.set_title("Global Market Distribution of Gaming Platforms\nAnd Growth Trends (2015-2022)", fontsize=16, fontweight='bold', pad=20)
ax1.axis('off')

ax2 = ax1.twinx()
marker_styles = ['s', 'D', '^', 'v', 'x', '*', '+', 'p']
line_styles = ['-', '--', '-.', ':', '--', '-.', '-', '-']
for i, (platform, growth) in enumerate(growth_trends.items()):
    ax2.plot(years, growth, marker=marker_styles[i % len(marker_styles)], linestyle=line_styles[i % len(line_styles)], label=platform, markersize=8)

ax2.set_ylabel('Growth in Market Share (%)', fontsize=12)
ax2.set_xlabel('Years', fontsize=12)
ax2.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')
ax2.legend(title='Growth Trends', loc='upper left', bbox_to_anchor=(1.05, 1.05), fontsize=10, borderpad=1, shadow=True)
plt.tight_layout()

plt.show()