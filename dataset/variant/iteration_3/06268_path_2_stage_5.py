import matplotlib.pyplot as plt
import numpy as np

years = ['2018', '2019', '2020', '2021']
genres = ['Act', 'Adv', 'Puz', 'Spt', 'RPG']

units_sold = {
    'Act': [120, 130, 200, 230],
    'Adv': [150, 180, 140, 95],
    'Puz': [110, 100, 110, 125],
    'Spt': [80, 115, 120, 150],
    'RPG': [90, 85, 90, 120]
}

# Changed the color set to a new one
new_colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231']
linestyles = ['-', '--', '-.', ':', '-']
markers = ['o', 's', 'D', '^', '*']

fig, ax = plt.subplots(figsize=(12, 8))

for i, (genre, values) in enumerate(units_sold.items()):
    adjusted_values = np.array(values) - np.mean(values)
    ax.plot(years, adjusted_values, label=genre, color=new_colors[i],
            linestyle=linestyles[i], marker=markers[i], markersize=8)

ax.set_xlabel('Yr', fontsize=12, weight='bold')
ax.set_ylabel('Dev from Mean (Thousands)', fontsize=12, weight='bold')
ax.set_title('Game Sales by Genre', fontsize=16, weight='bold', pad=20)

ax.legend(title='Genre', fontsize=9, title_fontsize='11', loc='upper left')
ax.grid(axis='y', linestyle=':', alpha=0.5)

plt.tight_layout()
plt.show()