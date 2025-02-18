import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
televisions = np.array([120, 115, 110, 105, 100, 98, 95, 92, 90, 85, 80])
microwaves = np.array([60, 62, 65, 67, 70, 72, 75, 77, 80, 82, 85])
refrigerators = np.array([85, 85, 88, 90, 93, 95, 98, 100, 103, 105, 108])
washing_machines = np.array([40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90])
air_conditioners = np.array([30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])
laptops = np.array([70, 75, 80, 85, 90, 95, 100, 110, 120, 130, 140])

fig, ax = plt.subplots(figsize=(12, 8))

# Apply a single consistent color to all data groups
consistent_color = 'gray'

ax.plot(years, televisions, color=consistent_color, marker='o', linestyle='-', linewidth=2, markersize=6, label='TVs')
ax.plot(years, microwaves, color=consistent_color, marker='s', linestyle='--', linewidth=2, markersize=6, label='Mwaves')
ax.plot(years, refrigerators, color=consistent_color, marker='^', linestyle='-.', linewidth=2, markersize=6, label='Fridges')
ax.plot(years, washing_machines, color=consistent_color, marker='d', linestyle=':', linewidth=2, markersize=6, label='Washers')
ax.plot(years, air_conditioners, color=consistent_color, marker='x', linestyle='-', linewidth=2, markersize=6, label='ACs')
ax.plot(years, laptops, color=consistent_color, marker='p', linestyle='--', linewidth=2, markersize=6, label='Laptops')

ax.set_title('Tech Adv. Impact on Sales (2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Sales (k units)', fontsize=14)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

ax.legend()

plt.tight_layout()
plt.show()