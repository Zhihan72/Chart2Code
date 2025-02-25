import matplotlib.pyplot as plt
import numpy as np

# Data construction
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
points_norland = np.array([5, 12, 20, 35, 45, 60, 72, 85, 90, 95, 100, 110])
points_sunford = np.array([4, 10, 25, 30, 35, 50, 65, 75, 95, 110, 125, 130])
points_eastoria = np.array([3, 8, 18, 22, 30, 38, 50, 60, 70, 80, 90, 100])
points_westreach = np.array([2, 15, 22, 28, 36, 48, 56, 62, 70, 80, 85, 90])
points_shadowvale = np.array([1, 5, 10, 20, 28, 35, 45, 55, 60, 68, 75, 85])

fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx()

cumulative_points = points_norland + points_sunford + points_eastoria + points_westreach + points_shadowvale
ax2.plot(months, cumulative_points, color='purple', linestyle='--', marker='x', linewidth=2)

ax1.plot(months, points_norland, marker='o', linestyle='-', color='blue', linewidth=2)
ax1.plot(months, points_sunford, marker='s', linestyle='-', color='green', linewidth=2)
ax1.plot(months, points_eastoria, marker='d', linestyle='-', color='red', linewidth=2)
ax1.plot(months, points_westreach, marker='^', linestyle='-', color='orange', linewidth=2)
ax1.plot(months, points_shadowvale, marker='v', linestyle='-', color='black', linewidth=2)

ax1.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()