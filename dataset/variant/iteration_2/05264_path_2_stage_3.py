import matplotlib.pyplot as plt
import numpy as np

# Data for months and temperature
months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
city1_temp = np.array([5, 7, 10, 15, 20, 25, 30, 29, 23, 17, 10, 6])
city2_temp = np.array([10, 12, 16, 20, 25, 30, 35, 34, 28, 22, 15, 11])
city3_temp = np.array([0, 2, 8, 12, 17, 22, 27, 26, 21, 15, 8, 3])

# New data for additional cities
city4_temp = np.array([8, 10, 14, 18, 23, 28, 33, 32, 27, 21, 14, 9])
city5_temp = np.array([3, 5, 9, 14, 19, 24, 29, 28, 23, 17, 11, 6])

fig, ax = plt.subplots(figsize=(12, 6))

# Plotting city temperatures
ax.plot(months, city1_temp, marker='o', linestyle='-', color='blue', label='NY')
ax.plot(months, city2_temp, marker='s', linestyle='--', color='green', label='LA')
ax.plot(months, city3_temp, marker='d', linestyle='-.', color='red', label='CHI')
ax.plot(months, city4_temp, marker='^', linestyle='-', color='purple', label='HOU')
ax.plot(months, city5_temp, marker='*', linestyle='--', color='orange', label='MIA')

# Titles, labels, and grid
ax.set_title("Temp Variations in 2023", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Mon", fontsize=12)
ax.set_ylabel("Temp (°C)", fontsize=12)
ax.grid(True, linestyle='--', alpha=0.5)

# Legend and data point annotations
ax.legend(title='City', fontsize=10)
for i in range(len(months)):
    ax.text(months[i], city1_temp[i] + 0.5, f"{city1_temp[i]}°C", ha='center', va='bottom', fontsize=9, color='blue')
    ax.text(months[i], city2_temp[i] + 0.5, f"{city2_temp[i]}°C", ha='center', va='bottom', fontsize=9, color='green')
    ax.text(months[i], city3_temp[i] + 0.5, f"{city3_temp[i]}°C", ha='center', va='bottom', fontsize=9, color='red')
    ax.text(months[i], city4_temp[i] + 0.5, f"{city4_temp[i]}°C", ha='center', va='bottom', fontsize=9, color='purple')
    ax.text(months[i], city5_temp[i] + 0.5, f"{city5_temp[i]}°C", ha='center', va='bottom', fontsize=9, color='orange')

plt.tight_layout()
plt.show()