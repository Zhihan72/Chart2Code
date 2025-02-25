import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
new_constructions = np.array([2, 4, 5, 8, 7, 10, 12, 15, 18, 20, 25])
green_spaces = np.array([1, 1, 2, 3, 5, 7, 8, 9, 12, 15, 17])
renewable_projects = np.array([0, 1, 1, 2, 3, 4, 6, 8, 9, 10, 12])

fig, ax1 = plt.subplots(figsize=(14, 7))

bar_width = 0.2
index = np.arange(len(years))

bars1 = ax1.bar(index, new_constructions, bar_width, color='lightcoral', edgecolor='black', label='Constructions')
bars2 = ax1.bar(index + bar_width, green_spaces, bar_width, color='lightseagreen', edgecolor='black', label='Green Areas')
bars3 = ax1.bar(index + 2 * bar_width, renewable_projects, bar_width, color='gold', edgecolor='black', label='Renewables')

ax1.set_title("Development & Initiatives (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Count", fontsize=12)
ax1.set_xticks(index + bar_width)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left', fontsize=10, frameon=False)
ax1.grid(axis='y', linestyle='-.', alpha=0.6)

for bars in [bars1, bars2, bars3]:
    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, int(yval), ha='center', fontsize=10, color='navy')

plt.suptitle("Portville: Sustainable Growth", fontsize=14, y=0.97, color='darkred')

plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.show()