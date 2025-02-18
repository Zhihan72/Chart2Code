import matplotlib.pyplot as plt
import numpy as np

# Define regions and years
regions = ['Avalon', 'Mystica', 'Faerun', 'Narnia', 'Wonderland']
years = [2018, 2019, 2020, 2021, 2022]

# Data: Magic Beans Production (in metric tons)
production_data = np.array([
    [12, 15, 14, 16, 18],  # Avalon
    [10, 11, 13, 17, 19],  # Mystica
    [13, 14, 16, 15, 17],  # Faerun
    [9, 13, 12, 14, 15],   # Narnia
    [14, 16, 18, 20, 22]   # Wonderland
])

bar_width = 0.15
x = np.arange(len(years))

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Colors for each region
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

markers = ['o', 's', '^', 'D', 'X']
linestyles = ['-', '--', '-.', ':', '-']
for i, region in enumerate(regions):
    ax.bar(x + i * bar_width, production_data[i], width=bar_width, label=region, color=colors[i], edgecolor='black', hatch=markers[i])

ax.set_title('Race for Magic Beans:\nAnnual Production in Various Regions (2018-2022)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Production of Magic Beans (Metric Tons)', fontsize=14)
ax.set_xticks(x + bar_width * 2)
ax.set_xticklabels(years)
ax.legend(title='Regions', fontsize=12, title_fontsize='13', loc='upper left', frameon=True, facecolor='linen')
ax.grid(axis='x', linestyle=linestyles[0], alpha=0.5)

# Adding different line styles to the grid
ax.yaxis.grid(linestyle=linestyles[1], alpha=0.5)

# Add text annotations on each bar for better insight
for i in range(len(regions)):
    for j in range(len(years)):
        ax.text(x[j] + i * bar_width, production_data[i, j] + 0.3, str(production_data[i, j]), ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()