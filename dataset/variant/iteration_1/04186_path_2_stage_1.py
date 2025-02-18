import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2011, 2022)
desktop_usage = [54, 50, 47, 44, 40, 36, 33, 31, 30, 28, 25]
mobile_usage = [20, 25, 30, 35, 40, 45, 50, 52, 55, 57, 60]
tablet_usage = [10, 12, 14, 15, 16, 17, 18, 18, 18, 18, 18]
smart_tv_usage = [2, 3, 4, 5, 6, 8, 10, 12, 14, 17, 20]

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.15

r1 = np.arange(len(years))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]

ax.bar(r1, desktop_usage, color='b', width=bar_width, edgecolor='grey')
ax.bar(r2, mobile_usage, color='r', width=bar_width, edgecolor='grey')
ax.bar(r3, tablet_usage, color='g', width=bar_width, edgecolor='grey')
ax.bar(r4, smart_tv_usage, color='y', width=bar_width, edgecolor='grey')

ax.set_xticks([r + bar_width for r in range(len(years))])
ax.set_xticklabels([])  # Remove x-axis labels
ax.set_yticklabels([])  # Remove y-axis labels

ax.legend([],[], loc='upper left')

ax.grid(True, linestyle='--', alpha=0.6, axis='y')

# Average lines are retained but texts are removed
average_desktop = np.mean(desktop_usage)
average_mobile = np.mean(mobile_usage)
average_tablet = np.mean(tablet_usage)
average_tv = np.mean(smart_tv_usage)

ax.axhline(average_desktop, color='blue', linestyle='--', linewidth=1)
ax.axhline(average_mobile, color='red', linestyle='--', linewidth=1)
ax.axhline(average_tablet, color='green', linestyle='--', linewidth=1)
ax.axhline(average_tv, color='yellow', linestyle='--', linewidth=1)

plt.tight_layout()
plt.show()