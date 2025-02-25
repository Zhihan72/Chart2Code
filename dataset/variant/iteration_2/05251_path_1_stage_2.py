import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

# Manually shuffled population data for each fictional city
city_a = [170, 155, 200, 165, 150, 185, 180, 195, 160, 190, 175]
city_b = [145, 110, 150, 120, 130, 140, 100, 105, 155, 160, 150]
city_c = [95, 82, 85, 88, 90, 92, 80, 105, 98, 120, 110]
city_d = [240, 205, 215, 230, 200, 245, 260, 270, 275, 290, 280]
city_e = [80, 65, 70, 90, 60, 95, 100, 110, 120, 130, 140]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, city_a, marker='o', linestyle='-', linewidth=2, color='#1f77b4')
ax.plot(years, city_b, marker='s', linestyle='--', linewidth=2, color='#ff7f0e')
ax.plot(years, city_c, marker='^', linestyle='-.', linewidth=2, color='#2ca02c')
ax.plot(years, city_d, marker='d', linestyle=':', linewidth=2, color='#d62728')
ax.plot(years, city_e, marker='x', linestyle='-', linewidth=2, color='#9467bd')

ax.set_yticks(range(50, 301, 25))
ax.set_xticks(years)
ax.tick_params(axis='x', rotation=45)
ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()