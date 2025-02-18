import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
avg_temp = np.array([3, 5, 10, 14, 18, 22, 25, 24, 20, 15, 8, 4])
cumulative_rainfall = np.array([50, 80, 120, 160, 210, 270, 350, 430, 500, 570, 620, 680])
avg_sunshine_hours = np.array([50, 70, 120, 150, 220, 260, 300, 310, 250, 160, 90, 60])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.set_title("Weather Metrics in Urbania", fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel("Month", fontsize=14)
ax1.set_ylabel("Avg Temp (°C)", fontsize=14, color='tab:orange')
ax1.plot(months, avg_temp, color='tab:orange', label='Avg Temp', linewidth=2)
ax1.fill_between(months, avg_temp, color='orange', alpha=0.3)
ax1.tick_params(axis='y', labelcolor='tab:orange')
ax1.set_ylim(0, 30)

ax2 = ax1.twinx()
ax2.set_ylabel("Cum. Rain (mm)", fontsize=14, color='tab:blue')
ax2.plot(months, cumulative_rainfall, color='tab:blue', label='Cum. Rain', linewidth=2)
ax2.fill_between(months, cumulative_rainfall, color='blue', alpha=0.3)
ax2.tick_params(axis='y', labelcolor='tab:blue')
ax2.set_ylim(0, 700)

ax3 = ax1.twinx()
ax3.spines.right.set_position(("outward", 60))
ax3.set_ylabel("Avg Sunshine Hrs", fontsize=14, color='tab:green')
ax3.plot(months, avg_sunshine_hours, color='tab:green', label='Avg Sunshine Hrs', linewidth=2)
ax3.fill_between(months, avg_sunshine_hours, color='green', alpha=0.3)
ax3.tick_params(axis='y', labelcolor='tab:green')
ax3.set_ylim(0, 350)

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
ax1.legend(lines + lines2 + lines3, labels + labels2 + labels3, loc='upper left', fontsize=12)

ax1.grid(True, linestyle='--', alpha=0.6)

ax1.annotate('Temp Rise', xy=('Jul', 25), xytext=('Apr', 27),
             arrowprops=dict(facecolor='red', arrowstyle='->'), fontsize=10, color='darkred')
ax2.annotate('Rainfall Peak', xy=('Aug', 430), xytext=('Jun', 520),
             arrowprops=dict(facecolor='purple', arrowstyle='->'), fontsize=10, color='purple')

plt.tight_layout()
plt.show()