import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2011, 2021)
apples_vitamin_c = np.array([5, 5.2, 5.3, 5.4, 5.1, 5.5, 5.7, 5.8, 5.6, 5.7])
apples_fiber = np.array([2.5, 2.6, 2.7, 2.6, 2.5, 2.8, 3.0, 3.1, 3.2, 3.3])
oranges_vitamin_c = np.array([50, 52, 53, 55, 54, 56, 57, 58, 59, 60])
oranges_fiber = np.array([2.4, 2.5, 2.5, 2.6, 2.5, 2.7, 2.8, 2.9, 3.0, 3.1])
bananas_vitamin_c = np.array([9, 8.9, 9.1, 9.2, 8.8, 9.3, 9.4, 9.5, 9.6, 9.6])
bananas_fiber = np.array([2.6, 2.7, 2.8, 2.9, 2.8, 3.0, 3.1, 3.2, 3.3, 3.4])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(years, apples_vitamin_c, color='#8B4513', marker='o', linestyle='-', linewidth=2)
ax1.plot(years, oranges_vitamin_c, color='#FF6347', marker='s', linestyle='-', linewidth=2)
ax1.plot(years, bananas_vitamin_c, color='#008000', marker='^', linestyle='-', linewidth=2)

ax2 = ax1.twinx()
ax2.plot(years, apples_fiber, color='#556B2F', marker='o', linestyle='--', linewidth=2)
ax2.plot(years, oranges_fiber, color='#FFD700', marker='s', linestyle='--', linewidth=2)
ax2.plot(years, bananas_fiber, color='#FFA500', marker='^', linestyle='--', linewidth=2)

ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
ax2.yaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()