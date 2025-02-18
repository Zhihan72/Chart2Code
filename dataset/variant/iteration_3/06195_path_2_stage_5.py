import matplotlib.pyplot as plt
import numpy as np

regions = ['Avalon', 'Mystica', 'Faerun', 'Narnia', 'Wonderland']
years = [2018, 2019, 2020, 2021, 2022]

production_data = np.array([
    [18, 12, 14, 15, 16],
    [13, 10, 19, 17, 11],
    [16, 17, 14, 13, 15],
    [12, 9, 15, 14, 13],
    [22, 16, 20, 14, 18]
])

bar_height = 0.15
y = np.arange(len(years))
fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ff9999']
markers = ['o', 's', '^', 'D', 'X']
linestyles = ['-', '--', '-.', ':', '-']
for i, region in enumerate(regions):
    ax.barh(y + i * bar_height, production_data[i], height=bar_height, label=region, color=colors[i], edgecolor='black', hatch=markers[i])

ax.set_title('Magic Beans Production (2018-22)', fontsize=18, fontweight='bold', pad=20)
ax.set_ylabel('Year', fontsize=14)
ax.set_xlabel('Production (Tons)', fontsize=14)
ax.set_yticks(y + bar_height * 2)
ax.set_yticklabels(years)
ax.legend(title='Region', fontsize=12, title_fontsize='13', loc='upper left', frameon=True, facecolor='linen')
ax.grid(axis='y', linestyle=linestyles[0], alpha=0.5)
ax.xaxis.grid(linestyle=linestyles[1], alpha=0.5)

for i in range(len(regions)):
    for j in range(len(years)):
        ax.text(production_data[i, j] + 0.3, y[j] + i * bar_height, str(production_data[i, j]), va='center', ha='left', fontsize=10)

plt.tight_layout()
plt.show()