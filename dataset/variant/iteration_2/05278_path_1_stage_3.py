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
ax2.plot(months, cumulative_points, color='purple', linestyle=':', marker='x', linewidth=3, label='Cumulative Points')

ax1.plot(months, points_norland, marker='*', linestyle='--', color='teal', linewidth=1.5, label='Norland')
ax1.plot(months, points_sunford, marker='h', linestyle='-.', color='violet', linewidth=1.5, label='Sunford')
ax1.plot(months, points_eastoria, marker='p', linestyle='-', color='navy', linewidth=1.5, label='Eastoria')
ax1.plot(months, points_westreach, marker='<', linestyle=':', color='crimson', linewidth=1.5, label='Westreach')
ax1.plot(months, points_shadowvale, marker='1', linestyle='-', color='darkgoldenrod', linewidth=1.5, label='Shadowvale')

ax1.legend(loc='upper left')
ax1.grid(False)

plt.tight_layout()
plt.show()