import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
city1_temps = [-1, 0, 4, 10, 16, 20, 22, 21, 17, 10, 5, 1]
city2_temps = [8, 9, 12, 16, 20, 24, 27, 27, 23, 18, 12, 9]
city3_temps = [12, 13, 15, 19, 22, 25, 28, 28, 26, 20, 15, 13]
city4_temps = [5, 6, 8, 12, 17, 21, 24, 23, 19, 14, 9, 6]  # New data series for City 4
city5_temps = [15, 16, 18, 23, 27, 31, 34, 33, 29, 24, 18, 16]  # New data series for City 5

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(months, city1_temps, marker='o', linestyle='-', color='blue', linewidth=2, alpha=0.9, label='City 1')
ax.plot(months, city2_temps, marker='s', linestyle='--', color='green', linewidth=2, alpha=0.8, label='City 2')
ax.plot(months, city3_temps, marker='^', linestyle='-.', color='red', linewidth=2, alpha=0.7, label='City 3')
ax.plot(months, city4_temps, marker='d', linestyle=':', color='purple', linewidth=2, alpha=0.6, label='City 4')
ax.plot(months, city5_temps, marker='*', linestyle='-', color='orange', linewidth=2, alpha=0.5, label='City 5')

plt.title('Yearly Heat Fluctuations in Five Locations', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Time of Year', fontsize=12)
plt.ylabel('Heat Intensity (°C)', fontsize=12)

plt.xticks(months, ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'])

plt.legend()  # Adding legend to differentiate between cities
plt.tight_layout()

plt.show()