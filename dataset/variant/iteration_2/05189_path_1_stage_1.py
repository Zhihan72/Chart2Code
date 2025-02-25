import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
weekday_riders = np.array([30, 35, 40, 45, 50, 55, 60, 70, 80, 85, 90, 95])
weekend_riders = np.array([60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170])

fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.plot(months, weekday_riders, marker='o', linestyle='-', color='blue', linewidth=2, label='Weekday')
ax1.plot(months, weekend_riders, marker='s', linestyle='--', color='green', linewidth=2, label='Weekend')

ax1.set_title('Cyclist Participation', fontsize=16, weight='bold', pad=20)
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Riders', fontsize=12)

ax1.set_xticks(months)
ax1.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], fontsize=10, rotation=45)

ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax1.legend(loc='upper left', fontsize=10)

ax1.annotate('Peak', xy=(8, 70), xytext=(6, 50),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1), fontsize=10, color='darkblue')
ax1.annotate('Surge', xy=(12, 170), xytext=(10, 150),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1), fontsize=10, color='darkgreen')

plt.tight_layout()
plt.show()