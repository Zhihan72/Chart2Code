import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Book genres
genres = ["Fiction", "Non-Fiction", "Science Fiction", "Fantasy", "Mystery"]

# Shuffled annual book sales data (in thousands)
sales_data = np.array([
    [200, 260, 230, 150, 210, 160, 185, 220, 245, 170, 195],  # Fiction
    [120, 100, 165, 130, 115, 210, 180, 150, 140, 190, 170],  # Non-Fiction
    [130, 75, 95, 140, 90, 80, 160, 110, 120, 170, 150],      # Science Fiction
    [150, 60, 130, 80, 90, 50, 100, 110, 120, 70, 140],       # Fantasy
    [60, 130, 120, 40, 70, 100, 110, 90, 45, 50, 80],         # Mystery
])

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.15
x_indices = np.arange(len(years))

colors = ['dodgerblue', 'orangered', 'green', 'purple', 'gold']

for idx, genre in enumerate(genres):
    ax.bar(x_indices + idx * bar_width, sales_data[idx], width=bar_width, label=genre, color=colors[idx], alpha=0.85)

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Book Sales (in thousands)', fontsize=12)
ax.set_title('Randomized Book Sales Performance by Genre (2010-2020)', fontsize=16, fontweight='bold')

ax.set_xticks(x_indices + bar_width * 2)
ax.set_xticklabels(years, rotation=45)

for i in range(len(years)):
    for j in range(len(genres)):
        ax.text(i + j * bar_width, sales_data[j][i] + 1, str(sales_data[j][i]), ha='center', va='bottom', fontsize=9)

ax.legend(title='Book Genres', loc='upper left', fontsize=10)

ax.yaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()