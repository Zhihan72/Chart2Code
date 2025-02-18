import matplotlib.pyplot as plt
import numpy as np

seasons = np.array(['Winter', 'Spring', 'Summer', 'Autumn'])
pm25_levels = np.array([35, 20, 15, 25])
co_levels = np.array([0.9, 0.6, 0.4, 0.7])
no2_levels = np.array([40, 25, 20, 30])

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(seasons, pm25_levels, marker='o', linestyle='-', color='purple', linewidth=2)
ax.plot(seasons, co_levels, marker='s', linestyle='--', color='orange', linewidth=2)
ax.plot(seasons, no2_levels, marker='^', linestyle='-.', color='brown', linewidth=2)

ax.set_title("Seasonal Air Quality Analysis in Greenfield (Last Decade)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Seasons", fontsize=14)
ax.set_ylabel("Pollutant Levels", fontsize=14)

ax_right = ax.twinx()
ax_right.set_ylabel("CO Levels (mg/m³)", fontsize=14)
ax_right.plot(seasons, co_levels, marker='s', linestyle='--', color='orange', linewidth=2)
ax_right.tick_params(axis='y', labelcolor='orange')

plt.show()