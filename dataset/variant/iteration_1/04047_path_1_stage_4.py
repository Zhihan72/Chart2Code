import matplotlib.pyplot as plt
import numpy as np

seasons = np.array(['Win', 'Spr', 'Sum', 'Aut'])
pm25_levels = np.array([15, 35, 25, 20])
co_levels = np.array([0.4, 0.7, 0.9, 0.6])
no2_levels = np.array([20, 40, 30, 25])

fig, ax = plt.subplots(figsize=(10, 6))

# Alter stylistic elements randomly
# Changing marker types, line styles, legend position, and grid style
ax.plot(seasons, pm25_levels, marker='D', linestyle='-', color='blue', linewidth=2, label='PM25')
ax.plot(seasons, co_levels, marker='x', linestyle=':', color='red', linewidth=2, label='CO')
ax.plot(seasons, no2_levels, marker='v', linestyle='--', color='green', linewidth=2, label='NO2')

ax.set_title("Air Quality: Greenfield", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Seasons", fontsize=14)
ax.set_ylabel("Levels", fontsize=14)

ax_right = ax.twinx()
ax_right.set_ylabel("CO (mg/m³)", fontsize=14)
ax_right.plot(seasons, co_levels, marker='x', linestyle=':', color='red', linewidth=2)
ax_right.tick_params(axis='y', labelcolor='red')

ax.legend(loc='upper right', fontsize='medium')

# Use a dotted grid line style with higher alpha
ax.grid(True, linestyle=':', alpha=0.7)

plt.tight_layout()
plt.show()