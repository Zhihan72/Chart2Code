import matplotlib.pyplot as plt
import numpy as np

years = ['2018', '2019', '2020', '2021']
genres = ['Action', 'Adventure', 'Puzzle', 'Sports', 'RPG']

# Randomly altered units sold (in thousands) for each genre over the years
units_sold = {
    'Action': [120, 130, 200, 230],
    'Adventure': [150, 180, 140, 95],
    'Puzzle': [110, 100, 110, 125],
    'Sports': [80, 115, 120, 150],
    'RPG': [90, 85, 90, 120]
}

colors = ['#ff6666', '#ffcc99', '#99ff99', '#66b3ff', '#c2c2f0']

baseline = np.zeros(len(years))

fig, ax = plt.subplots(figsize=(12, 8))

for i, (genre, values) in enumerate(units_sold.items()):
    adjusted_values = np.array(values) - np.mean(values)
    ax.bar(years, adjusted_values, label=genre, color=colors[i], alpha=0.8, bottom=baseline)
    baseline += adjusted_values

ax.set_xlabel('Years', fontsize=12, weight='bold')
ax.set_ylabel('Deviation from Mean (Thousands)', fontsize=12, weight='bold')
ax.set_title('Diverging Video Game Sales by Genre Over Years', fontsize=16, weight='bold', pad=20)
ax.legend(title='Genres', fontsize=10, title_fontsize='12', loc='upper right')

ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()