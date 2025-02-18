import matplotlib.pyplot as plt
import numpy as np

hours_range = ['0-3', '4-5', '6-7', '8-9', '10-11', '12+']
weekday_sleepers = [5, 15, 40, 80, 30, 10]
weekend_sleepers = [2, 8, 50, 90, 35, 20]
young_adults_sleepers = [3, 12, 45, 85, 25, 15]

x_pos = np.arange(len(hours_range))

fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.25

color = '#1f77b4' 
bars1 = ax.barh(x_pos - bar_width, weekday_sleepers, bar_width, color=color)
bars2 = ax.barh(x_pos, weekend_sleepers, bar_width, color=color)
bars3 = ax.barh(x_pos + bar_width, young_adults_sleepers, bar_width, color=color)

ax.set_yticks(x_pos)

ax.xaxis.grid(True, linestyle='-', color='grey', alpha=0.3)

plt.tight_layout()
plt.show()