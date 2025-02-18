import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
city_a = [150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200]
city_b = [100, 105, 110, 120, 130, 140, 150, 160, 155, 150, 145]
city_c = [80, 82, 85, 88, 90, 92, 95, 98, 105, 110, 120]
city_e = [60, 65, 70, 80, 90, 95, 100, 110, 120, 130, 140]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, city_a, marker='o', linestyle='-', linewidth=2, color='#1f77b4')
ax.plot(years, city_b, marker='s', linestyle='--', linewidth=2, color='#1f77b4')
ax.plot(years, city_c, marker='^', linestyle='-.', linewidth=2, color='#1f77b4')
ax.plot(years, city_e, marker='x', linestyle='-', linewidth=2, color='#1f77b4')

# Removed title and labels
# ax.set_title('Population Growth in Fictional Cities (2010-2020)', fontsize=18, fontweight='bold', pad=20)
# ax.set_xlabel('Year', fontsize=15)
# ax.set_ylabel('Population (in thousands)', fontsize=15)

ax.set_yticks(range(50, 301, 25))
ax.set_xticks(years)
ax.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()