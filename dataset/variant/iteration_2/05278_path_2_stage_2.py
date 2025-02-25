import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
regions = ['Norland', 'Sunford', 'Eastoria', 'Westreach']

points_norland = np.array([6, 14, 19, 33, 47, 59, 71, 88, 89, 96, 102, 109])
points_sunford = np.array([5, 9, 24, 29, 34, 52, 63, 76, 94, 112, 123, 131])
points_eastoria = np.array([2, 10, 17, 23, 31, 40, 47, 61, 69, 82, 88, 99])
points_westreach = np.array([3, 14, 23, 27, 35, 47, 57, 63, 68, 79, 86, 91])

fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx()

cumulative_points = points_norland + points_sunford + points_eastoria + points_westreach
ax2.plot(months, cumulative_points, color='purple', linestyle='--', marker='x', linewidth=2)

ax1.plot(months, points_norland, marker='o', linestyle='-', color='blue', linewidth=2)
ax1.plot(months, points_sunford, marker='s', linestyle='-', color='green', linewidth=2)
ax1.plot(months, points_eastoria, marker='d', linestyle='-', color='red', linewidth=2)
ax1.plot(months, points_westreach, marker='^', linestyle='-', color='orange', linewidth=2)

ax1.set_xlabel('Months', fontsize=14)
ax1.set_ylabel('Points per Region', fontsize=14)
ax2.set_ylabel('Cumulative Points', fontsize=14)

plt.tight_layout()
plt.show()