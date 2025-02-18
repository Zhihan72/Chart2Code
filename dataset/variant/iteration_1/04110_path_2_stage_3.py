import matplotlib.pyplot as plt
import numpy as np

years = ['2017', '2018', '2019', '2020']
categories = ['Adventure', 'Culture', 'Food', 'Nature']

data = np.array([
    [15, 18, 22, 26],  # Adventure
    [20, 22, 24, 30],  # Culture
    [30, 32, 34, 38],  # Food
    [25, 28, 30, 35],  # Nature
])

total_travelers = np.sum(data, axis=1)
sorted_indices = np.argsort(total_travelers)[::-1]  # Sort in descending order

sorted_categories = [categories[i] for i in sorted_indices]
sorted_colors = ['blue', 'green', 'orange', 'red']  # Adjusted to match the reduced data
sorted_data = data[sorted_indices]

fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.5
x = np.arange(len(categories))

for i, (category, travelers, color) in enumerate(zip(sorted_categories, sorted_data, sorted_colors)):
    ax.bar(x[i], total_travelers[i], color=color, label=category)

    plt.text(x[i], total_travelers[i] + 2, str(total_travelers[i]), ha='center', va='center', fontsize=10, fontweight='bold')

ax.set_xlabel('Activity', fontsize=14, fontweight='bold')
ax.set_ylabel('Total Travelers (in thousands)', fontsize=14, fontweight='bold')
ax.set_title('Sorted Global Travel Interests (2017-2020)\nTotal Travelers by Activity', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(sorted_categories)

ax.legend(title='Categories', loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
ax.grid(visible=True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()