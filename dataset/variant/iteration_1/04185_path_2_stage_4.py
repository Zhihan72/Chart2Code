import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
avg_temp = np.array([3, 5, 10, 14, 18, 22, 25, 24, 20, 15, 8, 4])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.set_title("Urbania: Temp Trends", fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel("Month", fontsize=14, fontstyle='italic')
ax1.set_ylabel("Avg Temp (°C)", fontsize=14, color='tab:green')
ax1.plot(months, avg_temp, color='forestgreen', label='Avg Temp', linestyle='--', marker='o', markersize=8)
ax1.fill_between(months, avg_temp, color='lightgreen', alpha=0.2)
ax1.tick_params(axis='y', labelcolor='tab:green')
ax1.set_ylim(0, 30)

ax1.legend(loc='lower right', fontsize=10, frameon=False)
ax1.grid(True, linestyle='-.', linewidth=0.7, alpha=0.5)

plt.tight_layout()
plt.show()