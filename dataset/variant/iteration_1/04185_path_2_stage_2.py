import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
avg_temp = np.array([3, 5, 10, 14, 18, 22, 25, 24, 20, 15, 8, 4])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.set_title("Climate Trends in Urbania: Temperature Patterns", fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel("Month", fontsize=14, fontstyle='italic')
ax1.set_ylabel("Average Temperature (°C)", fontsize=14, color='tab:blue')
ax1.plot(months, avg_temp, color='tab:blue', label='Average Temperature', linestyle='--', marker='o', markersize=8)
ax1.fill_between(months, avg_temp, color='blue', alpha=0.2)
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.set_ylim(0, 30)

# Modified legend position and font size
ax1.legend(loc='lower right', fontsize=10, frameon=False)

# Changed grid style
ax1.grid(True, linestyle='-.', linewidth=0.7, alpha=0.5)

# Removed the annotation for a cleaner look

plt.tight_layout()
plt.show()