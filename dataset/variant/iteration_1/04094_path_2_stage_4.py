import numpy as np
import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Data series
morning_traffic = [5, 6, 7, 8, 9, 4, 3]
afternoon_traffic = [9, 10, 11, 12, 13, 8, 7]
evening_traffic = [15, 16, 17, 18, 19, 14, 10]
night_traffic = [3, 2, 2, 3, 4, 6, 8]
early_morning_traffic = [2, 3, 3, 4, 5, 1, 1]

fig, ax = plt.subplots(figsize=(12, 8))

# Plotting data with varied styles
ax.plot(days, morning_traffic, label="Morning", color='mediumslateblue', marker='v', linestyle='-', linewidth=3)
ax.plot(days, afternoon_traffic, label="Afternoon", color='seagreen', marker='p', linestyle='--', linewidth=3)
ax.plot(days, evening_traffic, label="Evening", color='coral', marker='*', linestyle='-.', linewidth=3)
ax.plot(days, night_traffic, label="Night", color='teal', marker='+', linestyle=':', linewidth=3)
ax.plot(days, early_morning_traffic, label="Early Morning", color='darkorange', marker='1', linestyle='-', linewidth=3)

ax.set_xlabel('Days', fontsize=12, fontweight='light')
ax.set_ylabel('Traffic (k)', fontsize=12, fontweight='light')
ax.set_title('Weekly Traffic Trends', fontsize=18, fontweight='heavy')

ax.set_xticks(range(len(days)))
ax.set_xticklabels(days)
ax.xaxis.grid(True, linestyle='-', alpha=0.3, linewidth=0.5)
ax.yaxis.grid(False)
plt.xticks(rotation=20)
ax.legend(loc='lower center', fontsize=9)
plt.tight_layout()

plt.show()