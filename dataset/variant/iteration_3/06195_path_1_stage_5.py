import matplotlib.pyplot as plt
import numpy as np

regions = ['Avalon', 'Mystica', 'Faerun', 'Narnia', 'Wonderland', 'Elvandar', 'Middle Earth']
years = [2018, 2019, 2020, 2021, 2022]

production_data = np.array([
    [12, 15, 14, 16, 18],
    [10, 11, 13, 17, 19],
    [13, 14, 16, 15, 17],
    [9, 13, 12, 14, 15],
    [14, 16, 18, 20, 22],
    [11, 13, 14, 18, 21],
    [8, 12, 15, 19, 20]
])

bar_height = 0.12
y = np.arange(len(years))

fig, ax = plt.subplots(figsize=(12, 8))

single_color = '#66b3ff'

for i, region in enumerate(regions):
    ax.barh(y + i * bar_height, production_data[i], height=bar_height, color=single_color)

ax.set_yticks(y + bar_height * 3)
ax.set_yticklabels(years)

for i in range(len(regions)):
    for j in range(len(years)):
        ax.text(production_data[i, j] + 0.3, y[j] + i * bar_height, str(production_data[i, j]), ha='left', va='center', fontsize=10)

plt.tight_layout()
plt.show()