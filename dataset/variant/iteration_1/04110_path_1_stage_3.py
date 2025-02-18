import matplotlib.pyplot as plt
import numpy as np

# Categories and corresponding number of travelers (in thousands) across four years
years = ['2017', '2018', '2019', '2020']
categories = ['Adventure', 'Culture', 'Food', 'Nature']

# Number of travelers (in thousands) interested in each category per year
data = np.array([
    [15, 18, 22, 26],  # Adventure
    [20, 22, 24, 30],  # Culture
    [30, 32, 34, 38],  # Food
    [25, 28, 30, 35],  # Nature
])

fig, ax = plt.subplots(figsize=(12, 8))

bar_height = 0.15
y = np.arange(len(years))

# Use a single color, e.g., 'blue', for all bars
color = 'blue'

# Creating horizontal bars for each category over multiple years
for i, category in enumerate(categories):
    ax.barh(y + i * bar_height, data[i], height=bar_height, label=category, color=color)

# Adding annotations to the bars
for i in range(len(years)):
    for j in range(len(categories)):
        plt.text(data[j][i] + 0.5, i + j * bar_height, str(data[j][i]), va='center', ha='left', fontsize=8, fontweight='bold')

# Customizing labels and titles
ax.set_ylabel('Year', fontsize=14, fontweight='bold')
ax.set_xlabel('Number of Travelers (in thousands)', fontsize=14, fontweight='bold')
ax.set_title('Global Travel Interests (2017-2020)\nDistribution of Travelers by Activity', fontsize=16, fontweight='bold')
ax.set_yticks(y + 1.5 * bar_height)
ax.set_yticklabels(years)

# Adding Legend
ax.legend(title='Categories', loc='upper right', fontsize=12)

# Adding a grid
ax.grid(visible=True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()