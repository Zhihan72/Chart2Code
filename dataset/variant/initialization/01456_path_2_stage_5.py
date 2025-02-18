import matplotlib.pyplot as plt
import numpy as np

# Data for years and brands
years = np.arange(2020, 2026)
brands = ['Eco', 'Threads', 'Wear', 'Knits', 'Trend']

# Altered data arrays
organic_cotton = np.array([
    [20, 25, 5, 30, 10, 15],  # Altered by swapping elements
    [4, 16, 12, 24, 20, 8],
    [29, 17, 23, 35, 6, 11],
    [5, 23, 28, 14, 18, 9],
    [3, 11, 19, 15, 7, 23]
])

recycled_polyester = np.array([
    [15, 3, 8, 19, 12, 5],
    [18, 14, 7, 11, 4, 21],
    [22, 13, 17, 6, 9, 2],
    [9, 20, 5, 3, 13, 16],
    [6, 10, 4, 22, 18, 14]
])

hemp = np.array([
    [8, 2, 12, 6, 10, 4],
    [1, 7, 11, 9, 5, 3],
    [17, 3, 8, 14, 11, 5],
    [10, 2, 15, 7, 4, 13],
    [4, 8, 6, 10, 2, 1]
])

fig, ax = plt.subplots(figsize=(14, 9))
bar_width = 0.25
x_indexes = np.arange(len(years))
offset = bar_width * 3
colors = ['#FF33A1', '#33FFA5', '#A533FF']

for i, brand in enumerate(brands):
    ax.bar(x_indexes + i * offset, organic_cotton[i], width=bar_width, label='Organic Cotton' if i == 0 else "", color=colors[0], alpha=0.8, edgecolor='black', linestyle='dotted')
    ax.bar(x_indexes + i * offset + bar_width, recycled_polyester[i], width=bar_width, label='Recycled Polyester' if i == 0 else "", color=colors[1], alpha=0.8, edgecolor='black', linestyle='dashdot')
    ax.bar(x_indexes + i * offset + bar_width * 2, hemp[i], width=bar_width, label='Hemp' if i == 0 else "", color=colors[2], alpha=0.8, edgecolor='black', linestyle='solid')

ax.set_xlabel('Year', fontsize=14, fontweight='bold')
ax.set_ylabel('Usage (in Tons)', fontsize=14, fontweight='bold')
ax.set_title('Eco Materials Adoption Trend (2020-2025)', fontsize=16, fontweight='bold', pad=25)
ax.set_xticks(x_indexes + 1.5 * bar_width)
ax.set_xticklabels(years)
handles, labels = ax.get_legend_handles_labels()
unique_labels = dict(zip(labels, handles))
ax.legend(unique_labels.values(), unique_labels.keys(), loc='best', fontsize=12, title='Materials', title_fontsize='14', shadow=True, fancybox=True)
ax.grid(axis='y', linestyle='-.', linewidth=0.8, color='grey', alpha=0.6)
plt.tight_layout(rect=[0, 0, 0.85, 1])
plt.show()