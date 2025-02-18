import matplotlib.pyplot as plt
import numpy as np

# Backstory and Data:
# This chart shows the distribution of different interest categories among a group of global travelers.
# The data represents the number of travelers interested in different activities such as Adventure, Culture, Food, Nature, and Shopping over recent years.

# Categories and corresponding number of travelers (in thousands) across four years
years = ['2017', '2018', '2019', '2020']
categories = ['Adventure', 'Culture', 'Food', 'Nature', 'Shopping']

# Number of travelers (in thousands) interested in each category per year
data = np.array([
    [15, 18, 22, 26],  # Adventure
    [20, 22, 24, 30],  # Culture
    [30, 32, 34, 38],  # Food
    [25, 28, 30, 35],  # Nature
    [10, 12, 15, 18],  # Shopping
])

# Generating Bar Chart
fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.15
x = np.arange(len(years))  # Label locations

# Creating bars for each category for multiple years
for i, category in enumerate(categories):
    ax.bar(x + i * bar_width, data[i], width=bar_width, label=category)

# Adding annotations to the bars
for i in range(len(years)):
    for j in range(len(categories)):
        plt.text(i + j * bar_width, data[j][i] + 0.5, str(data[j][i]), ha='center', va='bottom', fontsize=8, fontweight='bold')

# Customizing labels and titles
ax.set_xlabel('Year', fontsize=14, fontweight='bold')
ax.set_ylabel('Number of Travelers (in thousands)', fontsize=14, fontweight='bold')
ax.set_title('Global Travel Interests (2017-2020)\nDistribution of Travelers by Activity', fontsize=16, fontweight='bold')
ax.set_xticks(x + 2 * bar_width)
ax.set_xticklabels(years)

# Adding Legend
ax.legend(title='Categories', loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)

# Adding a grid
ax.grid(visible=True, linestyle='--', alpha=0.5)

# Adjusting layout to prevent overlapping text
plt.tight_layout()

# Display the chart
plt.show()