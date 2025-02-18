import matplotlib.pyplot as plt
import numpy as np

years = ['2017', '2018', '2019', '2020']
categories = ['Adventure', 'Culture', 'Food', 'Nature', 'Shopping']

data = np.array([
    [15, 18, 22, 26],  # Adventure
    [20, 22, 24, 30],  # Culture
    [30, 32, 34, 38],  # Food
    [25, 28, 30, 35],  # Nature
    [10, 12, 15, 18],  # Shopping
])

# Manually defined color scheme, shuffled
colors = ['green', 'blue', 'red', 'orange', 'purple']
# Shuffled colors for categories
shuffled_colors = ['orange', 'purple', 'green', 'red', 'blue']

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.15
x = np.arange(len(years))

for i, category in enumerate(categories):
    ax.bar(x + i * bar_width, data[i], width=bar_width, label=category, color=shuffled_colors[i])

for i in range(len(years)):
    for j in range(len(categories)):
        plt.text(i + j * bar_width, data[j][i] + 0.5, str(data[j][i]), ha='center', va='bottom', fontsize=8, fontweight='bold')

ax.set_xlabel('Year', fontsize=14, fontweight='bold')
ax.set_ylabel('Number of Travelers (in thousands)', fontsize=14, fontweight='bold')
ax.set_title('Global Travel Interests (2017-2020)\nDistribution of Travelers by Activity', fontsize=16, fontweight='bold')
ax.set_xticks(x + 2 * bar_width)
ax.set_xticklabels(years)

ax.legend(title='Categories', loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
ax.grid(visible=True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()