import matplotlib.pyplot as plt
import numpy as np

days = np.array(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
children_steps = np.array([15000, 16000, 15500, 15000, 14800, 17000, 18000])
adults_steps = np.array([10000, 10500, 10200, 9800, 9500, 11000, 11500])

fig, ax = plt.subplots(figsize=(12, 8))

same_color = '#FF5733'
ax.plot(days, children_steps, marker='o', linestyle='-', linewidth=2, color=same_color)
ax.plot(days, adults_steps, marker='s', linestyle='--', linewidth=2, color=same_color)

ax.set_title("Daily Step Count Trend: A Comparison Across Age Groups", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Day of the Week", fontsize=14)
ax.set_ylabel("Average Steps per Day", fontsize=14)

plt.tight_layout()
plt.show()