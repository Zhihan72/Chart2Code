import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

north_region = np.array([50, 60, 70, 85, 95, 105, 130, 145, 160, 180, 200])
south_region = np.array([20, 25, 35, 50, 65, 75, 90, 100, 115, 130, 150])

total_capacity = north_region + south_region

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(years, north_region, marker='o', linestyle='-', color='green', linewidth=2)
ax1.plot(years, south_region, marker='^', linestyle='-.', color='blue', linewidth=2)

ax2 = ax1.twinx()
ax2.plot(years, total_capacity, marker='D', linestyle='-', color='purple', linewidth=2)

ax1.set_title('WindCo Annual Wind Farm Installation Capacity (2010-2020)', fontsize=18, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14, labelpad=15)
ax1.set_ylabel('Installation Capacity (MW) per Region', fontsize=14, labelpad=15)
ax2.set_ylabel('Total Installation Capacity (MW)', fontsize=14, labelpad=15)

ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

annotations = {
    2015: ("North Region Expansion", north_region[5]),
    2020: ("South Region Major Installation", south_region[10]),
}

for year, (text, y_value) in annotations.items():
    ax1.annotate(text, xy=(year, y_value), xytext=(year, y_value + 20),
                 arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, ha='center')

plt.tight_layout()
plt.show()