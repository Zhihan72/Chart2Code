import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
televisions = np.array([120, 115, 110, 105, 100, 98, 95, 92, 90, 85, 80])
refrigerators = np.array([85, 85, 88, 90, 93, 95, 98, 100, 103, 105, 108])
washing_machines = np.array([40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, televisions, label='TVs', color='blue', marker='s', linestyle='--', linewidth=2, markersize=8)
ax.plot(years, refrigerators, label='Fridges', color='magenta', marker='x', linestyle=':', linewidth=2, markersize=8)
ax.plot(years, washing_machines, label='Washers', color='red', marker='v', linestyle='-', linewidth=2, markersize=8)

ax.set_title('Tech Boom: Appliance Sales Trends (2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Fiscal Year', fontsize=14)
ax.set_ylabel('Units Sold (000s)', fontsize=14)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

ax.legend(title='Device Categories', fontsize=12, title_fontsize=14, loc='upper right')
ax.grid(True, linestyle='-.', color='gray', alpha=0.5)

plt.tight_layout()
plt.show()