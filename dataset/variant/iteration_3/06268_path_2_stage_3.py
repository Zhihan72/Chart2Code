import matplotlib.pyplot as plt
import numpy as np

years = ['2018', '2019', '2020', '2021']
genres = ['Action', 'Adventure', 'Puzzle', 'Sports', 'RPG']

units_sold = {
    'Action': [120, 130, 200, 230],
    'Adventure': [150, 180, 140, 95],
    'Puzzle': [110, 100, 110, 125],
    'Sports': [80, 115, 120, 150],
    'RPG': [90, 85, 90, 120]
}

# Different colors for each genre
colors = ['#66b3ff', '#ff6666', '#99ff99', '#c2c2f0', '#ffcc99']

# Different linestyle patterns for each genre
linestyles = ['-', '--', '-.', ':', '-']

# Different marker types for each genre
markers = ['o', 's', 'D', '^', '*']

baseline = np.zeros(len(years))
fig, ax = plt.subplots(figsize=(12, 8))

for i, (genre, values) in enumerate(units_sold.items()):
    adjusted_values = np.array(values) - np.mean(values)
    ax.plot(years, adjusted_values, label=genre, color=colors[i],
            linestyle=linestyles[i], marker=markers[i], markersize=8)

ax.set_xlabel('Years', fontsize=12, weight='bold')
ax.set_ylabel('Deviation from Mean (Thousands)', fontsize=12, weight='bold')
ax.set_title('Diverging Video Game Sales by Genre Over Years', fontsize=16, weight='bold', pad=20)

# Randomly altered legend position and fontsize
ax.legend(title='Genres', fontsize=9, title_fontsize='11', loc='upper left')

# Randomly altered grid style
ax.grid(axis='y', linestyle=':', alpha=0.5)

plt.tight_layout()
plt.show()