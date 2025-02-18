import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
la_temps = np.array([14, 15, 17, 19, 22, 24, 27, 27, 26, 22, 18, 15])
ny_temps = np.array([0, 1, 7, 13, 19, 24, 27, 26, 22, 15, 10, 4])
chicago_temps = np.array([-3, 0, 6, 12, 18, 23, 26, 25, 20, 13, 6, -1])

# Added made-up temperature data for San Francisco and Miami
sf_temps = np.array([12, 14, 15, 17, 19, 21, 22, 22, 22, 19, 14, 12])
miami_temps = np.array([20, 21, 22, 24, 26, 28, 29, 29, 28, 26, 23, 21])

fig, ax = plt.subplots(figsize=(12, 8))

# Plot for each city
single_color = 'purple'
ax.plot(months, la_temps, marker='o', linestyle='-', color=single_color, linewidth=2)
ax.plot(months, ny_temps, marker='o', linestyle='-', color=single_color, linewidth=2)
ax.plot(months, chicago_temps, marker='o', linestyle='-', color=single_color, linewidth=2)

# Plotting new data series
ax.plot(months, sf_temps, marker='o', linestyle='-', color=single_color, linewidth=2)
ax.plot(months, miami_temps, marker='o', linestyle='-', color=single_color, linewidth=2)

ax.set_ylim(-5, 30)

plt.tight_layout()
plt.show()