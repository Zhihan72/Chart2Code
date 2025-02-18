import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
new_constructions = np.array([2, 4, 5, 8, 7, 10, 12, 15, 18, 20, 25])
green_spaces = np.array([1, 1, 2, 3, 5, 7, 8, 9, 12, 15, 17])
renewable_projects = np.array([0, 1, 1, 2, 3, 4, 6, 8, 9, 10, 12])

fig, ax1 = plt.subplots(figsize=(14, 7))

bar_height = 0.2
index = np.arange(len(years))

# Adjusted the code to plot horizontal bars
bars1 = ax1.barh(index, new_constructions, bar_height, color='gold', edgecolor='black', label='Constructions')
bars2 = ax1.barh(index + bar_height, green_spaces, bar_height, color='lightcoral', edgecolor='black', label='Green Areas')
bars3 = ax1.barh(index + 2 * bar_height, renewable_projects, bar_height, color='lightseagreen', edgecolor='black', label='Renewables')

ax1.set_title("Development & Initiatives (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax1.set_ylabel("Year", fontsize=12)
ax1.set_xlabel("Count", fontsize=12)
ax1.set_yticks(index + bar_height)
ax1.set_yticklabels(years)
ax1.legend(loc='upper left', fontsize=10, frameon=False)
ax1.grid(axis='x', linestyle='-.', alpha=0.6)

# Adjusted text annotation for horizontal bars
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        xval = bar.get_width()
        ax1.text(xval + 0.5, bar.get_y() + bar.get_height() / 2, int(xval), va='center', fontsize=10, color='navy')

plt.suptitle("Portville: Sustainable Growth", fontsize=14, y=0.97, color='darkred')

plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.show()