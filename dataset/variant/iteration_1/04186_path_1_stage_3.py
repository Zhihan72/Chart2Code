import matplotlib.pyplot as plt
import numpy as np

# Original data
devices = ['Desktop', 'Mobile', 'Tablet', 'Smart TV']
desktop_usage = [54, 50, 47, 44, 40, 36, 33, 31, 30, 28, 25]
mobile_usage = [20, 25, 30, 35, 40, 45, 50, 52, 55, 57, 60]
tablet_usage = [10, 12, 14, 15, 16, 17, 18, 18, 18, 18, 18]
smart_tv_usage = [2, 3, 4, 5, 6, 8, 10, 12, 14, 17, 20]

# Sort the usage and associated years in descending order
desktop_sorted, years_sorted_desk = zip(*sorted(zip(desktop_usage, years), reverse=True))
mobile_sorted, years_sorted_mob = zip(*sorted(zip(mobile_usage, years), reverse=True))
tablet_sorted, years_sorted_tab = zip(*sorted(zip(tablet_usage, years), reverse=True))
tv_sorted, years_sorted_tv = zip(*sorted(zip(smart_tv_usage, years), reverse=True))

fig, ax = plt.subplots(figsize=(14, 8))

# Plot each sorted usage data
ax.bar(years_sorted_desk, desktop_sorted, color='r', label='Desktop')
ax.bar(years_sorted_mob, mobile_sorted, color='g', label='Mobile')
ax.bar(years_sorted_tab, tablet_sorted, color='y', label='Tablet')
ax.bar(years_sorted_tv, tv_sorted, color='b', label='Smart TV')

ax.set_title('Sorted Web Usage by Device (2011-21)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Usage (%)', fontsize=14)
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years, rotation=45)

ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
ax.grid(True, linestyle='--', alpha=0.6, axis='y')

plt.tight_layout()
plt.show()