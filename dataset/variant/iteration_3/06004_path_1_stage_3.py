import matplotlib.pyplot as plt
import numpy as np

months = np.array([
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 
    'August', 'September', 'October', 'November', 'December'])

water_levels = np.array([1.5, 1.7, 1.8, 2.0, 2.1, 2.2, 2.5, 2.3, 2.1, 1.9, 1.6, 1.4])
temperatures = np.array([2, 3, 8, 15, 20, 25, 28, 27, 22, 16, 9, 4])

fig, ax1 = plt.subplots(figsize=(14, 8))

# Updated water levels plot
ax1.plot(months, water_levels, color='blue', marker='^', linestyle='-', linewidth=1, markersize=10)
ax1.tick_params(axis='y', colors='blue')
ax1.set_ylim(0, 3)
ax1.grid(axis='y', linestyle='-.', alpha=0.7)

# Updated temperatures plot
ax2 = ax1.twinx()
ax2.plot(months, temperatures, color='red', marker='x', linestyle='--', linewidth=3, markersize=12)
ax2.tick_params(axis='y', colors='red')
ax2.set_ylim(0, 30)

# Added legend
ax1.set_xlabel('Months')
ax1.set_ylabel('Water Levels', color='blue')
ax2.set_ylabel('Temperature (°C)', color='red')

# Stylize legend
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, ['Water Levels', 'Temperature'], loc='upper left', bbox_to_anchor=(0, 1), frameon=False)

plt.tight_layout()
plt.show()