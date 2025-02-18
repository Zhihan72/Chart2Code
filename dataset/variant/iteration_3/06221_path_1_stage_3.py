import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
genres = ["Fiction", "Non-Fiction", "Science Fiction", "Fantasy", "Mystery"]

sales_data = np.array([
    [150, 160, 170, 185, 200, 195, 210, 220, 230, 245, 260],
    [100, 115, 130, 140, 150, 165, 170, 180, 190, 200, 210],
    [75, 80, 90, 95, 110, 120, 130, 140, 150, 160, 170],
    [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],
    [40, 45, 50, 60, 70, 80, 90, 100, 110, 120, 130],
])

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.15
x_indices = np.arange(len(years))
colors = ['green', 'gold', 'orangered', 'dodgerblue', 'purple']

for idx, genre in enumerate(genres):
    ax.bar(x_indices + idx * bar_width, sales_data[idx], width=bar_width, color=colors[idx], alpha=0.85)

ax.set_xticks(x_indices + bar_width * 2)
ax.set_xticklabels(years, rotation=45)

plt.show()