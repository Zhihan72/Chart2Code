import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2011, 2021)
apples_vitamin_c = np.array([5, 5.2, 5.3, 5.4, 5.1, 5.5, 5.7, 5.8, 5.6, 5.7])
apples_fiber = np.array([2.5, 2.6, 2.7, 2.6, 2.5, 2.8, 3.0, 3.1, 3.2, 3.3])
oranges_vitamin_c = np.array([50, 52, 53, 55, 54, 56, 57, 58, 59, 60])
oranges_fiber = np.array([2.4, 2.5, 2.5, 2.6, 2.5, 2.7, 2.8, 2.9, 3.0, 3.1])
bananas_vitamin_c = np.array([9, 8.9, 9.1, 9.2, 8.8, 9.3, 9.4, 9.5, 9.6, 9.6])
bananas_fiber = np.array([2.6, 2.7, 2.8, 2.9, 2.8, 3.0, 3.1, 3.2, 3.3, 3.4])
grapes_vitamin_c = np.array([7, 7.1, 7.2, 7.3, 7.1, 7.4, 7.5, 7.6, 7.7, 7.8])
grapes_fiber = np.array([1.5, 1.6, 1.7, 1.6, 1.5, 1.8, 1.9, 2.0, 2.1, 2.2])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(years, apples_vitamin_c, color='#8B0000', marker='x', linestyle='-', linewidth=2, label='Apples Vitamin C')
ax1.plot(years, oranges_vitamin_c, color='#FF4500', marker='d', linestyle='-.', linewidth=2, label='Oranges Vitamin C')
ax1.plot(years, bananas_vitamin_c, color='#006400', marker='v', linestyle=':', linewidth=2, label='Bananas Vitamin C')
ax1.plot(years, grapes_vitamin_c, color='#800080', marker='o', linestyle='--', linewidth=2, label='Grapes Vitamin C')

ax2 = ax1.twinx()
ax2.plot(years, apples_fiber, color='#2F4F4F', marker='p', linestyle='--', linewidth=1.5, label='Apples Fiber')
ax2.plot(years, oranges_fiber, color='#DAA520', marker='*', linestyle='-', linewidth=1.5, label='Oranges Fiber')
ax2.plot(years, bananas_fiber, color='#FFD700', marker='h', linestyle='-.', linewidth=1.5, label='Bananas Fiber')
ax2.plot(years, grapes_fiber, color='#4B0082', marker='s', linestyle=':', linewidth=1.5, label='Grapes Fiber')

ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=30)
ax1.yaxis.grid(True, linestyle='-', alpha=0.5)
ax2.yaxis.grid(False)

# Add legends to the plots
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()