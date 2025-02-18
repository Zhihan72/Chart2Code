import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
city1_temps = [-1, 0, 4, 10, 16, 20, 22, 21, 17, 10, 5, 1]
city2_temps = [8, 9, 12, 16, 20, 24, 27, 27, 23, 18, 12, 9]
city3_temps = [12, 13, 15, 19, 22, 25, 28, 28, 26, 20, 15, 13]
city4_temps = [3, 4, 9, 12, 18, 21, 25, 24, 19, 12, 8, 4]
city5_temps = [6, 7, 10, 14, 19, 23, 26, 26, 22, 16, 10, 7]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(months, city1_temps, marker='v', linestyle='--', color='green', linewidth=1.5, label='City A', alpha=0.7)
ax.plot(months, city2_temps, marker='x', linestyle='-', color='red', linewidth=1.5, label='City B', alpha=0.9)
ax.plot(months, city3_temps, marker='o', linestyle=':', color='blue', linewidth=1.5, label='City C', alpha=0.5)
ax.plot(months, city4_temps, marker='^', linestyle='-.', color='pink', linewidth=1.5, label='City D', alpha=0.8)
ax.plot(months, city5_temps, marker='d', linestyle='-', color='magenta', linewidth=1.5, label='City E', alpha=0.6)

plt.title('Temperature Variations in Cities', fontsize=18, fontweight='bold', pad=25)
plt.xlabel('Month', fontsize=13)
plt.ylabel('Temperature (°C)', fontsize=13)

plt.xticks(months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

plt.grid(False)  # Grid removed for stylistic change

plt.legend(loc='lower right', fontsize=10, frameon=False)

ax.spines['top'].set_visible(False)  # Removes the top border
ax.spines['right'].set_visible(False)  # Removes the right border

plt.tight_layout()
plt.show()