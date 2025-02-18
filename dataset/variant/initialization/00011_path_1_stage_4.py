import matplotlib.pyplot as plt
import numpy as np

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
pm25_concentrations = np.array([55, 60, 52, 45, 50, 65, 70])
pm25_variability = np.array([5, 7, 4, 6, 5, 8, 7])

fig, ax1 = plt.subplots(figsize=(12, 8))

# Updated colors for the error bars and line
ax1.errorbar(days, pm25_concentrations, yerr=pm25_variability, fmt='-o',
             ecolor='green', capsize=5, capthick=2, color='orange', alpha=0.8)

ax1.set_ylim(35, 80)
ax1.set_yticks(np.arange(35, 85, 5))
ax1.tick_params(axis='y', labelcolor='orange')

# Remove borders/spines
for spine in ax1.spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()