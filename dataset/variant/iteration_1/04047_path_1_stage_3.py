import matplotlib.pyplot as plt
import numpy as np

seasons = np.array(['Win', 'Spr', 'Sum', 'Aut'])
pm25_levels = np.array([15, 35, 25, 20])
co_levels = np.array([0.4, 0.7, 0.9, 0.6])
no2_levels = np.array([20, 40, 30, 25])

fig, ax = plt.subplots(figsize=(10, 6))

common_color = 'black'

ax.plot(seasons, pm25_levels, marker='o', linestyle='-', color=common_color, linewidth=2, label='PM25')
ax.plot(seasons, co_levels, marker='s', linestyle='--', color=common_color, linewidth=2, label='CO')
ax.plot(seasons, no2_levels, marker='^', linestyle='-.', color=common_color, linewidth=2, label='NO2')

ax.set_title("Air Quality: Greenfield", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Seasons", fontsize=14)
ax.set_ylabel("Levels", fontsize=14)

ax_right = ax.twinx()
ax_right.set_ylabel("CO (mg/m³)", fontsize=14)

ax_right.plot(seasons, co_levels, marker='s', linestyle='--', color=common_color, linewidth=2)
ax_right.tick_params(axis='y', labelcolor=common_color)

ax.legend(loc='upper left', fontsize='medium')

ax.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

plt.show()