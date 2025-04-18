import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
city1_temps = [-1, 0, 4, 10, 16, 20, 22, 21, 17, 10, 5, 1]
city2_temps = [8, 9, 12, 16, 20, 24, 27, 27, 23, 18, 12, 9]
city3_temps = [12, 13, 15, 19, 22, 25, 28, 28, 26, 20, 15, 13]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(months, city1_temps, marker='o', linestyle='-', color='blue', linewidth=2, alpha=0.9)
ax.plot(months, city2_temps, marker='s', linestyle='--', color='green', linewidth=2, alpha=0.8)
ax.plot(months, city3_temps, marker='^', linestyle='-.', color='red', linewidth=2, alpha=0.7)

plt.title('Yearly Heat Fluctuations in Three Locations', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Time of Year', fontsize=12)
plt.ylabel('Heat Intensity (°C)', fontsize=12)

plt.xticks(months, ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'])

plt.tight_layout()

plt.show()