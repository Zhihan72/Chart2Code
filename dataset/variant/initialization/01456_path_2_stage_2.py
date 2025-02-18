import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2026)
brands = ['EcoChic', 'GreenThreads', 'SustainWear', 'NatureKnits', 'PureTrend']

organic_cotton = np.array([
    [5, 10, 15, 20, 25, 30],
    [4, 8, 12, 16, 20, 24],
    [6, 11, 17, 23, 29, 35],
    [5, 9, 14, 18, 23, 28],
    [3, 7, 11, 15, 19, 23]
])

recycled_polyester = np.array([
    [3, 5, 8, 12, 15, 19],
    [4, 7, 11, 14, 18, 21],
    [2, 6, 9, 13, 17, 22],
    [3, 5, 9, 13, 16, 20],
    [4, 6, 10, 14, 18, 22]
])

hemp = np.array([
    [2, 4, 6, 8, 10, 12],
    [1, 3, 5, 7, 9, 11],
    [3, 5, 8, 11, 14, 17],
    [2, 4, 7, 10, 13, 15],
    [1, 2, 4, 6, 8, 10]
])

fig, ax = plt.subplots(figsize=(14, 9))

bar_width = 0.25
x_indexes = np.arange(len(years))
offset = bar_width * 3

# Define new colors for organic cotton, recycled polyester, and hemp
colors = ['#FF5733', '#33FF57', '#3357FF']  # Change these colors as desired

for i, brand in enumerate(brands):
    ax.bar(x_indexes + i * offset, organic_cotton[i], width=bar_width, label='Organic Cotton' if i == 0 else "", color=colors[0], alpha=0.8)
    ax.bar(x_indexes + i * offset + bar_width, recycled_polyester[i], width=bar_width, label='Recycled Polyester' if i == 0 else "", color=colors[1], alpha=0.8)
    ax.bar(x_indexes + i * offset + bar_width * 2, hemp[i], width=bar_width, label='Hemp' if i == 0 else "", color=colors[2], alpha=0.8)

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Material Usage (Tons)', fontsize=12)
ax.set_title('Adoption of Eco-Friendly Materials in Fashion Brands\n(2020-2025)', fontsize=14, fontweight='bold', pad=20)

ax.set_xticks(x_indexes + 1.5 * bar_width)
ax.set_xticklabels(years)

handles, labels = ax.get_legend_handles_labels()
unique_labels = dict(zip(labels, handles))
ax.legend(unique_labels.values(), unique_labels.keys(), loc='upper left', fontsize=10, bbox_to_anchor=(1, 1), title='Material', ncol=1)

ax.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout(rect=[0, 0, 0.85, 1])

plt.show()