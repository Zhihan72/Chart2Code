import matplotlib.pyplot as plt
import numpy as np

# Months
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Avg temperature (°C)
avg_temp = np.array([3, 5, 10, 14, 18, 22, 25, 24, 20, 15, 8, 4])

# Cumulative rainfall (mm)
cumulative_rainfall = np.array([50, 80, 120, 160, 210, 270, 350, 430, 500, 570, 620, 680])

# Plotting
fig, ax1 = plt.subplots(figsize=(14, 8))

# Temperature plot
ax1.set_title("Temp & Rain in Urbania", fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel("Month", fontsize=14)
ax1.set_ylabel("Avg Temp (°C)", fontsize=14, color='tab:orange')
ax1.plot(months, avg_temp, color='tab:orange', label='Avg Temp', linewidth=2)
ax1.fill_between(months, avg_temp, color='orange', alpha=0.3)
ax1.tick_params(axis='y', labelcolor='tab:orange')
ax1.set_ylim(0, 30)

# Rainfall plot
ax2 = ax1.twinx()
ax2.set_ylabel("Cum. Rain (mm)", fontsize=14, color='tab:blue')
ax2.plot(months, cumulative_rainfall, color='tab:blue', label='Cum. Rain', linewidth=2)
ax2.fill_between(months, cumulative_rainfall, color='blue', alpha=0.3)
ax2.tick_params(axis='y', labelcolor='tab:blue')
ax2.set_ylim(0, 700)

# Legends
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left', fontsize=12)

# Grid
ax1.grid(True, linestyle='--', alpha=0.6)

# Annotation
ax1.annotate('Temp Rise', xy=('Jul', 25), xytext=('Apr', 27),
             arrowprops=dict(facecolor='red', arrowstyle='->'), fontsize=10, color='darkred')

ax2.annotate('Rainfall Peak', xy=('Aug', 430), xytext=('Jun', 520),
             arrowprops=dict(facecolor='purple', arrowstyle='->'), fontsize=10, color='purple')

plt.tight_layout()
plt.show()