import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
new_york_temps = np.array([14, 0, 8, 2, 18, 23, -1, 21, 26, 13, 6, 25])
los_angeles_temps = np.array([17, 24, 15, 19, 14, 16, 20, 23, 24, 14, 21, 18])
chicago_temps = np.array([20, -2, 6, 24, 4, 25, 13, 17, -5, 11, 22, -1])

fig, ax = plt.subplots(figsize=(12, 7))

# Vary the styling elements like colors, markers, and line styles
ax.plot(months, new_york_temps, marker='D', linestyle='-', color='tab:red', label='New York')
ax.plot(months, los_angeles_temps, marker='*', linestyle=':', color='tab:green', label='Los Angeles')
ax.plot(months, chicago_temps, marker='p', linestyle='--', color='tab:purple', label='Chicago')

# Change the grid style
ax.grid(True, linestyle=':', linewidth=0.8, alpha=0.5)

# Add a legend with altered placement
ax.legend(loc='upper left', fontsize=10, frameon=False)

# Change face color of the plot area
ax.set_facecolor('#f0f0f0')

plt.tight_layout()
plt.show()