import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

city_a = [170, 155, 200, 165, 150, 185, 180, 195, 160, 190, 175]
city_b = [145, 110, 150, 120, 130, 140, 100, 105, 155, 160, 150]
city_c = [95, 82, 85, 88, 90, 92, 80, 105, 98, 120, 110]
city_d = [240, 205, 215, 230, 200, 245, 260, 270, 275, 290, 280]
city_e = [80, 65, 70, 90, 60, 95, 100, 110, 120, 130, 140]

fig, ax = plt.subplots(figsize=(14, 8))

# Altered stylistic elements and marker types
ax.plot(years, city_a, marker='v', linestyle='--', linewidth=3, color='#ff00ff', label='City A')
ax.plot(years, city_b, marker='<', linestyle='-', linewidth=1, color='#00ffff', label='City B')
ax.plot(years, city_c, marker='>', linestyle='-', linewidth=2, color='#ffff00', label='City C')
ax.plot(years, city_d, marker='p', linestyle='-.', linewidth=2, color='#3333ff', label='City D')
ax.plot(years, city_e, marker='*', linestyle=':', linewidth=2, color='#ff9933', label='City E')

ax.set_yticks(range(50, 301, 25))
ax.set_xticks(years)
ax.tick_params(axis='x', rotation=45)

ax.grid(True, linestyle='-', alpha=0.3)  # Altered grid style

# Added legend
ax.legend(loc='upper left', frameon=False)

plt.tight_layout()
plt.show()