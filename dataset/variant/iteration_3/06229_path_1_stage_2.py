import matplotlib.pyplot as plt
import numpy as np

cities = ['Springfield', 'Shelbyville', 'Ogdenville', 'North Haverbrook', 'Capital City']
years = ['2019', '2020', '2021', '2022', '2023']

# Manually altered gardens_setup data while keeping the structure intact
gardens_setup = np.array([
    [14, 10, 20, 21, 23],
    [11, 11, 14, 19, 20],
    [8, 9, 12, 16, 21],
    [6, 7, 11, 11, 17],
    [15, 17, 22, 21, 24]
])

# Manually altered harvest_yield data while keeping the structure intact
harvest_yield = np.array([
    [1150, 1300, 1550, 1550, 1750],
    [1050, 1200, 1400, 1450, 1550],
    [650, 850, 1050, 1050, 1200],
    [550, 700, 900, 900, 1050],
    [1350, 1450, 1650, 1650, 1750]
])

total_harvest_yield = harvest_yield.sum(axis=1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), constrained_layout=True)

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