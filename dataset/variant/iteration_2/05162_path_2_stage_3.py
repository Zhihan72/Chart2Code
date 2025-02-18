import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

north_region = np.array([50, 60, 70, 85, 95, 105, 130, 145, 160, 180, 200])
central_region = np.array([30, 45, 65, 80, 100, 110, 135, 150, 170, 190, 210])

total_capacity = north_region + central_region

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(years, north_region, marker='o', linestyle='-', color='green', linewidth=2)
ax1.plot(years, central_region, marker='s', linestyle='--', color='red', linewidth=2)

ax2 = ax1.twinx()
ax2.plot(years, total_capacity, marker='D', linestyle='-', color='orange', linewidth=2)

ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

annotations = {
    2015: ("North Region Expansion", north_region[5]),
    2018: ("Central Region New Projects", central_region[8]),
}

for year, (text, y_value) in annotations.items():
    ax1.annotate(text, xy=(year, y_value), xytext=(year, y_value + 20),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, ha='center')

ax1.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()