import matplotlib.pyplot as plt
import numpy as np

devices = ['Desktop', 'Mobile', 'Tablet', 'Smart TV']
desktop_usage = [44, 33, 36, 31, 40, 25, 47, 54, 28, 50, 30]
mobile_usage = [60, 25, 52, 30, 40, 45, 50, 35, 55, 57, 20]
tablet_usage = [18, 12, 18, 15, 16, 17, 18, 14, 18, 10, 18]
smart_tv_usage = [17, 14, 8, 10, 3, 4, 2, 5, 20, 6, 12]
years = range(2011, 2022)

desktop_sorted, years_sorted_desk = zip(*sorted(zip(desktop_usage, years), reverse=True))
mobile_sorted, years_sorted_mob = zip(*sorted(zip(mobile_usage, years), reverse=True))
tablet_sorted, years_sorted_tab = zip(*sorted(zip(tablet_usage, years), reverse=True))
tv_sorted, years_sorted_tv = zip(*sorted(zip(smart_tv_usage, years), reverse=True))

fig, ax = plt.subplots(figsize=(14, 8))

ax.bar(years_sorted_desk, desktop_sorted, color='r')
ax.bar(years_sorted_mob, mobile_sorted, color='g')
ax.bar(years_sorted_tab, tablet_sorted, color='y')
ax.bar(years_sorted_tv, tv_sorted, color='b')

ax.set_title('Sorted Web Usage by Device (2011-21)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Usage (%)', fontsize=14)
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years, rotation=45)

plt.tight_layout()
plt.show()