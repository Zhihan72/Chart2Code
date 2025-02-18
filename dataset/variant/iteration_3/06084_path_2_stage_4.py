import matplotlib.pyplot as plt
import numpy as np

divisions = ['NA', 'Eur', 'Asia', 'Afr', 'Aus', 'SA']
years = [2018, 2019, 2020, 2021, 2022]

production = np.array([
    [20, 19, 22, 25, 26],
    [18, 21, 20, 24, 25],
    [15, 13, 16, 21, 23],
    [12, 17, 18, 19, 19],
    [10, 14, 15, 15, 17],
    [8, 10, 12, 14, 14],
])

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.15
color = 'skyblue'

for i, year in enumerate(years):
    bar_positions = np.arange(len(divisions)) + i * bar_width
    ax.bar(bar_positions, production[:, i], bar_width, color=color)

ax.set_title("SolarPower Annual Prod. by Region (2018-2022)", fontsize=16, fontweight='bold')
ax.set_xlabel("Regions", fontsize=14)
ax.set_ylabel("Prod. (GW)", fontsize=14)

ax.set_xticks(np.arange(len(divisions)) + 2 * bar_width)
ax.set_xticklabels(divisions, rotation=45, ha='right', fontsize=12)

plt.tight_layout()
plt.show()