import matplotlib.pyplot as plt
import numpy as np

seasons = np.array(['Win', 'Spr', 'Sum', 'Aut'])
pm25_levels = np.array([35, 20, 15, 25])
no2_levels = np.array([40, 25, 20, 30])

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(seasons, pm25_levels, marker='o', linestyle='-', color='purple', linewidth=2)
ax.plot(seasons, no2_levels, marker='^', linestyle='-.', color='brown', linewidth=2)

ax.set_title("Air Quality by Season", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Seasons", fontsize=14)
ax.set_ylabel("Levels", fontsize=14)

plt.show()