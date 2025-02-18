import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
temperatures = np.array([7, 22, 10, 14, 5, 25, 18, 24, 20, 15, 10, 6])
rainfall = np.array([60, 50, 65, 70, 75, 55, 45, 70, 55, 50, 70, 65])

fig, ax1 = plt.subplots(figsize=(14, 8))

color_temp = 'DarkOrange'
ax1.plot(months, temperatures, color=color_temp, marker='o', markersize=8, linestyle='-', linewidth=2)
ax1.tick_params(axis='y', labelcolor=color_temp, labelleft=False)  # Remove y-axis labels

ax2 = ax1.twinx()
color_rain = 'MediumSeaGreen'
ax2.plot(months, rainfall, color=color_rain, marker='s', markersize=8, linestyle='-', linewidth=2)
ax2.tick_params(axis='y', labelcolor=color_rain, labelright=False)  # Remove y-axis labels

ax1.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)  # Remove x-axis labels

plt.show()