import matplotlib.pyplot as plt
import numpy as np

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Manually shuffled data within the original dimensional structure
pm25_conc = np.array([70, 55, 50, 65, 52, 60, 45])
pm25_var = np.array([7, 5, 5, 8, 4, 7, 6])
avg_temp = np.array([25, 22, 22, 26, 24, 21, 23])

fig, ax1 = plt.subplots(figsize=(12, 8))

ax1.errorbar(days, pm25_conc, yerr=pm25_var, fmt='-o',
             ecolor='blue', capsize=5, capthick=2, color='orange', alpha=0.8, label='PM2.5')

ax1.set_title("Air Quality & Weather", fontsize=14)
ax1.set_xlabel("Day", fontsize=12)
ax1.set_ylabel("PM2.5 (µg/m³)", fontsize=12, color='orange')
ax1.set_ylim(35, 80)
ax1.set_yticks(np.arange(35, 85, 5))
ax1.tick_params(axis='y', labelcolor='orange')
ax1.grid(True, linestyle='--', alpha=0.6)

ax2 = ax1.twinx()
ax2.bar(days, avg_temp, color='red', alpha=0.5, width=0.4, label='Avg Temp')
ax2.set_ylabel("Avg Temp (°C)", fontsize=12, color='red')
ax2.set_ylim(20, 30)
ax2.tick_params(axis='y', labelcolor='red')

lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', fontsize=10)

plt.tight_layout()
plt.show()