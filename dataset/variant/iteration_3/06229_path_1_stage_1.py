import matplotlib.pyplot as plt
import numpy as np

cities = ['Springfield', 'Shelbyville', 'Ogdenville', 'North Haverbrook', 'Capital City']
years = ['2019', '2020', '2021', '2022', '2023']

gardens_setup = np.array([
    [12, 15, 19, 20, 24],
    [10, 12, 15, 18, 22],
    [7, 10, 13, 15, 20],
    [5, 8, 10, 12, 16],
    [14, 18, 21, 22, 25]
])

harvest_yield = np.array([
    [1200, 1350, 1500, 1600, 1800],
    [1100, 1225, 1375, 1475, 1600],
    [700, 900, 1000, 1100, 1250],
    [500, 750, 850, 950, 1100],
    [1400, 1500, 1600, 1700, 1800]
])

total_harvest_yield = harvest_yield.sum(axis=1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), constrained_layout=True)

# Subplot 1: Stacked bar chart for gardens setup
bottoms = np.zeros(len(cities))
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
hatches = ['', '//', '\\\\', 'xx', '..']
for i, year in enumerate(years):
    bars = ax1.bar(cities, gardens_setup[:, i], bottom=bottoms, label=year, color=colors[i], hatch=hatches[i % len(hatches)])
    bottoms += gardens_setup[:, i]

    for bar in bars:
        height = bar.get_height()
        if height > 5:
            ax1.annotate(f'{int(height)}',
                         xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2),
                         xytext=(0, 0), textcoords="offset points",
                         ha='center', va='center', fontsize=9, color='white')

ax1.set_title("Community Gardens Setup (2019-2023)", fontsize=13, fontweight='bold', color='brown')
ax1.set_xlabel("Cities", fontsize=11)
ax1.set_ylabel("Number of Gardens Setup", fontsize=11)
ax1.yaxis.grid(True, linestyle='-.', alpha=0.6)
ax1.legend(title="Year", title_fontsize='11', fontsize='9', loc='lower right', frameon=False)

# Subplot 2: Bar chart for total harvest yield
bars = ax2.bar(cities, total_harvest_yield, color='#26a69a', alpha=0.75, edgecolor='blue', linewidth=2, linestyle='dotted')

for bar, yield_amount in zip(bars, total_harvest_yield):
    ax2.annotate(f'{yield_amount} kg',
                 xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                 xytext=(0, 5), textcoords="offset points",
                 ha='center', va='bottom', fontsize=10, color='black')

ax2.set_title("Total Harvest Yield (2019-2023)", fontsize=13, fontweight='bold', color='brown')
ax2.set_xlabel("Cities", fontsize=11)
ax2.set_ylabel("Harvest Yield (kg)", fontsize=11)
ax2.yaxis.grid(False)

fig.suptitle("Community Gardening Initiatives", fontsize=17, fontweight='bold', y=1.02)
plt.show()