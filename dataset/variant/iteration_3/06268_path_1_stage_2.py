import matplotlib.pyplot as plt
import numpy as np

# Data preparation
years = ['2018', '2019', '2020', '2021']
genres = ['Action', 'Puzzle', 'Sports', 'RPG']

# Units sold (in thousands) for each genre over the years
units_sold = {
    'Action': [150, 180, 200, 230],
    'Puzzle': [90, 100, 110, 120],
    'Sports': [110, 115, 120, 125],
    'RPG': [80, 85, 90, 95]
}

# New colors for each genre
colors = ['#ff9999', '#66ff66', '#6699ff', '#ffcc66']

fig, ax1 = plt.subplots(figsize=(12, 8))

bar_width = 0.15
index = np.arange(len(years))

# Plot each genre's units sold as a group bar plot with new colors
for i, (genre, values) in enumerate(units_sold.items()):
    ax1.bar(index + i * bar_width, values, bar_width, label=genre, color=colors[i], alpha=0.8)

# Add annotations
for i, (genre, values) in enumerate(units_sold.items()):
    for j, value in enumerate(values):
        ax1.annotate(f'{value}k',
                     xy=(index[j] + i * bar_width, value),
                     xytext=(0, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', fontsize=10, fontweight='bold')

ax1.set_xlabel('Years', fontsize=12, weight='bold')
ax1.set_ylabel('Units Sold (Thousands)', fontsize=12, weight='bold')
ax1.set_title('Video Game Sales Distribution by Genre Over Time', fontsize=16, weight='bold', pad=20)
ax1.set_xticks(index + 1.5 * bar_width)
ax1.set_xticklabels(years, fontsize=11, weight='bold')
ax1.legend(title='Genres', fontsize=10, title_fontsize='12', loc='upper left')
ax1.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()