import matplotlib.pyplot as plt
import numpy as np

# Data for months and temperature
months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
city1_temp = np.array([5, 7, 10, 15, 20, 25, 30, 29, 23, 17, 10, 6])
city2_temp = np.array([10, 12, 16, 20, 25, 30, 35, 34, 28, 22, 15, 11])
city3_temp = np.array([0, 2, 8, 12, 17, 22, 27, 26, 21, 15, 8, 3])

fig, ax = plt.subplots(figsize=(12, 6))

color = 'b'

# Plotting city temperatures
ax.plot(months, city1_temp, marker='o', linestyle='-', color=color, label='NY')
ax.plot(months, city2_temp, marker='s', linestyle='--', color=color, label='LA')
ax.plot(months, city3_temp, marker='d', linestyle='-.', color=color, label='CHI')

# Titles, labels, and grid
ax.set_title("Temp Variations in 2023", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Mon", fontsize=12)
ax.set_ylabel("Temp (°C)", fontsize=12)
ax.grid(True, linestyle='--', alpha=0.5)

# Legend and data point annotations
ax.legend(title='City', fontsize=10)
for i in range(len(months)):
    ax.text(months[i], city1_temp[i] + 0.5, f"{city1_temp[i]}°C", ha='center', va='bottom', fontsize=9, color=color)
    ax.text(months[i], city2_temp[i] + 0.5, f"{city2_temp[i]}°C", ha='center', va='bottom', fontsize=9, color=color)
    ax.text(months[i], city3_temp[i] + 0.5, f"{city3_temp[i]}°C", ha='center', va='bottom', fontsize=9, color=color)

plt.tight_layout()
plt.show()