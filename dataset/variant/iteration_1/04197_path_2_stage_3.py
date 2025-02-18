import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
new_york_temps = np.array([14, 0, 8, 2, 18, 23, -1, 21, 26, 13, 6, 25])
los_angeles_temps = np.array([17, 24, 15, 19, 14, 16, 20, 23, 24, 14, 21, 18])
chicago_temps = np.array([20, -2, 6, 24, 4, 25, 13, 17, -5, 11, 22, -1])

fig, ax = plt.subplots(figsize=(12, 7))

uniform_color = 'tab:blue'

ax.plot(months, new_york_temps, marker='o', linestyle='-', color=uniform_color)
ax.plot(months, los_angeles_temps, marker='^', linestyle='--', color=uniform_color)
ax.plot(months, chicago_temps, marker='s', linestyle='-.', color=uniform_color)

ax.grid(True, linestyle='--', alpha=0.7)
ax.set_facecolor('#f9f9f9')

plt.tight_layout()
plt.show()