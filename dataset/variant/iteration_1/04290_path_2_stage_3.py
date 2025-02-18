import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])
brands = ["CrunchyBites", "FruitMunch", "ChocoDelight", "NuttyCrave"]

sales_north = np.array([
    [150, 170, 180, 200, 210],
    [120, 140, 160, 170, 180],
    [130, 160, 190, 210, 220],
    [90, 100, 120, 130, 140]
])

sales_east = np.array([
    [160, 180, 190, 210, 230],
    [130, 150, 170, 180, 190],
    [150, 180, 200, 220, 240],
    [100, 110, 130, 140, 160]
])

sales_west = np.array([
    [140, 160, 170, 190, 200],
    [110, 130, 150, 160, 170],
    [120, 150, 180, 200, 210],
    [80, 90, 110, 120, 130]
])

fig, axes = plt.subplots(3, 1, figsize=(10, 15), sharex=True)

# Changed color set
new_colors = ['#8b008b', '#deb887', '#4682b4', '#9acd32']

for ax, sales in zip(axes, [sales_north, sales_east, sales_west]):
    bar_width = 0.2
    index = np.arange(len(years))
    
    for i, color in enumerate(new_colors):
        ax.bar(index + (i * bar_width), sales[i], bar_width, color=color)
    
    ax.set_ylabel('Sales (in \'000 units)')

axes[-1].set_xlabel('Year')
axes[-1].set_xticks(index + bar_width * 1.5)
axes[-1].set_xticklabels(years, rotation=45)

plt.tight_layout()
plt.show()