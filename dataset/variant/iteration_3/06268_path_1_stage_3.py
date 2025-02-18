import matplotlib.pyplot as plt
import numpy as np

years = ['2020', '2021', '2018', '2019']
genres = ['Puzzle', 'Action', 'RPG', 'Sports']

units_sold = {
    'Puzzle': [90, 100, 110, 120],
    'Action': [150, 180, 200, 230],
    'RPG': [80, 85, 90, 95],
    'Sports': [110, 115, 120, 125]
}

colors = ['#66ff66', '#ff9999', '#ffcc66', '#6699ff']

fig, ax1 = plt.subplots(figsize=(12, 8))

bar_width = 0.15
index = np.arange(len(years))

for i, (genre, values) in enumerate(units_sold.items()):
    ax1.bar(index + i * bar_width, values, bar_width, label=genre, color=colors[i], alpha=0.8)

for i, (genre, values) in enumerate(units_sold.items()):
    for j, value in enumerate(values):
        ax1.annotate(f'{value}k',
                     xy=(index[j] + i * bar_width, value),
                     xytext=(0, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', fontsize=10, fontweight='bold')

ax1.set_xlabel('Timeline', fontsize=12, weight='bold')
ax1.set_ylabel('Thousands of Units Sold', fontsize=12, weight='bold')
ax1.set_title('Distribution of Game Sales by Gender', fontsize=16, weight='bold', pad=20)
ax1.set_xticks(index + 1.5 * bar_width)
ax1.set_xticklabels(years, fontsize=11, weight='bold')
ax1.legend(title='Types', fontsize=10, title_fontsize='12', loc='upper left')
ax1.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()