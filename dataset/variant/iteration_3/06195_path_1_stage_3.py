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

bar_width = 0.12
x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2']

for i, region in enumerate(regions):
    ax.bar(x + i * bar_width, production_data[i], width=bar_width, color=colors[i])

ax.set_xticks(x + bar_width * 3)
ax.set_xticklabels(years)

for i in range(len(regions)):
    for j in range(len(years)):
        ax.text(x[j] + i * bar_width, production_data[i, j] + 0.3, str(production_data[i, j]), ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()