import matplotlib.pyplot as plt
import numpy as np

days = ["Thursday", "Wednesday", "Friday", "Monday", "Tuesday", "Saturday", "Sunday"]
pm25_concentrations = np.array([45, 52, 50, 55, 60, 65, 70])
pm25_variability = np.array([6, 4, 5, 5, 7, 8, 7])

fig, ax1 = plt.subplots(figsize=(12, 8))

# Plotting a sorted bar chart
ax1.bar(days, pm25_concentrations, yerr=pm25_variability,
        capsize=5, color='orange', alpha=0.8, edgecolor='green')

ax1.set_ylim(35, 80)
ax1.set_yticks(np.arange(35, 85, 5))
ax1.tick_params(axis='y', labelcolor='orange')

# Remove borders/spines
for spine in ax1.spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()