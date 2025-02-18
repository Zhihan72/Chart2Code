import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
city1_temps = [-1, 0, 4, 10, 16, 20, 22, 21, 17, 10, 5, 1]
city2_temps = [8, 9, 12, 16, 20, 24, 27, 27, 23, 18, 12, 9]
city3_temps = [12, 13, 15, 19, 22, 25, 28, 28, 26, 20, 15, 13]
city4_temps = [3, 4, 9, 12, 18, 21, 25, 24, 19, 12, 8, 4]
city5_temps = [6, 7, 10, 14, 19, 23, 26, 26, 22, 16, 10, 7]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(months, city1_temps, marker='o', linestyle='-', color='darkgreen', linewidth=2, label='A', alpha=0.9)
ax.plot(months, city2_temps, marker='s', linestyle='--', color='darkred', linewidth=2, label='B', alpha=0.8)
ax.plot(months, city3_temps, marker='^', linestyle='-.', color='darkblue', linewidth=2, label='C', alpha=0.7)
ax.plot(months, city4_temps, marker='d', linestyle=':', color='purple', linewidth=2, label='D', alpha=0.6)
ax.plot(months, city5_temps, marker='x', linestyle='-', color='orange', linewidth=2, label='E', alpha=0.5)

plt.title('Temp Changes in 5 Cities', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Temp (°C)', fontsize=12)

plt.xticks(months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.legend(loc='upper left', fontsize=12)

plt.tight_layout()
plt.show()