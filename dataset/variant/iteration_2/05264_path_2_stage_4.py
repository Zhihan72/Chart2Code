import matplotlib.pyplot as plt
import numpy as np

# Data for months and temperature
months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
city1_temp = np.array([5, 7, 10, 15, 20, 25, 30, 29, 23, 17, 10, 6])
city2_temp = np.array([10, 12, 16, 20, 25, 30, 35, 34, 28, 22, 15, 11])
city3_temp = np.array([0, 2, 8, 12, 17, 22, 27, 26, 21, 15, 8, 3])
city4_temp = np.array([8, 10, 14, 18, 23, 28, 33, 32, 27, 21, 14, 9])
city5_temp = np.array([3, 5, 9, 14, 19, 24, 29, 28, 23, 17, 11, 6])

fig, ax = plt.subplots(figsize=(12, 6))

# Plotting city temperatures with altered styles
ax.plot(months, city1_temp, marker='x', linestyle='-.', color='navy', label='NY')
ax.plot(months, city2_temp, marker='v', linestyle='-', color='lime', label='LA')
ax.plot(months, city3_temp, marker='h', linestyle=':', color='darkred', label='CHI')
ax.plot(months, city4_temp, marker='p', linestyle='--', color='violet', label='HOU')
ax.plot(months, city5_temp, marker='P', linestyle='-', color='darkorange', label='MIA')

# Titles, labels, and enhanced grid
ax.set_title("Temperature Variations in 2023", fontsize=18, fontweight='bold', pad=15)
ax.set_xlabel("Month", fontsize=14)
ax.set_ylabel("Temperature (°C)", fontsize=14)
ax.grid(True, linestyle=':', linewidth=0.7, color='gray')

# Legend with altered style
ax.legend(title='City', fontsize=11, title_fontsize='13', loc='upper left', shadow=True)

# Enhanced data point annotations
for i in range(len(months)):
    ax.text(months[i], city1_temp[i] + 0.2, f"{city1_temp[i]}°", ha='center', va='bottom', fontsize=9, color='navy')
    ax.text(months[i], city2_temp[i] + 0.2, f"{city2_temp[i]}°", ha='center', va='bottom', fontsize=9, color='lime')
    ax.text(months[i], city3_temp[i] + 0.2, f"{city3_temp[i]}°", ha='center', va='bottom', fontsize=9, color='darkred')
    ax.text(months[i], city4_temp[i] + 0.2, f"{city4_temp[i]}°", ha='center', va='bottom', fontsize=9, color='violet')
    ax.text(months[i], city5_temp[i] + 0.2, f"{city5_temp[i]}°", ha='center', va='bottom', fontsize=9, color='darkorange')

plt.tight_layout()
plt.show()