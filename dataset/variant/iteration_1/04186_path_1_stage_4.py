import matplotlib.pyplot as plt
import numpy as np

# Original data with manually shuffled usage
devices = ['Desktop', 'Mobile', 'Tablet', 'Smart TV']
desktop_usage = [44, 33, 36, 31, 40, 25, 47, 54, 28, 50, 30]
mobile_usage = [60, 25, 52, 30, 40, 45, 50, 35, 55, 57, 20]
tablet_usage = [18, 12, 18, 15, 16, 17, 18, 14, 18, 10, 18]
smart_tv_usage = [17, 14, 8, 10, 3, 4, 2, 5, 20, 6, 12]
years = range(2011, 2022)

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