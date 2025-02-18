import numpy as np
import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Original data series
morning_traffic = [5, 6, 7, 8, 9, 4, 3]
afternoon_traffic = [9, 10, 11, 12, 13, 8, 7]
evening_traffic = [15, 16, 17, 18, 19, 14, 10]
night_traffic = [3, 2, 2, 3, 4, 6, 8]

# Added data series
early_morning_traffic = [2, 3, 3, 4, 5, 1, 1]

fig, ax = plt.subplots(figsize=(12, 8))

# Plotting data
ax.plot(days, morning_traffic, label="Morn (6-12)", color='darkred', marker='o', linewidth=2)
ax.plot(days, afternoon_traffic, label="Aftn (12-6)", color='navy', marker='s', linewidth=2)
ax.plot(days, evening_traffic, label="Eve (18-24)", color='olivedrab', marker='^', linewidth=2)
ax.plot(days, night_traffic, label="Nt (24-6)", color='gold', marker='d', linewidth=2)
ax.plot(days, early_morning_traffic, label="Early Morn (4-6)", color='purple', marker='x', linewidth=2)

ax.set_xlabel('Days', fontsize=12)
ax.set_ylabel('Traffic (k)', fontsize=12)
ax.set_title('Weekly Traffic Trends', fontsize=16, fontweight='bold')

ax.set_xticks(range(len(days)), days)
ax.grid(True, linestyle='--', alpha=0.6)
plt.xticks(rotation=45)
ax.legend(loc='upper left', fontsize=10)
plt.tight_layout()

plt.show()