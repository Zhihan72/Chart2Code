import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1970, 2021, 5)
atlantic_exploration = [10, 15, 18, 25, 30, 40, 55, 65, 80, 90, 105]
pacific_exploration = [8, 12, 20, 30, 40, 55, 70, 85, 100, 115, 130]
arctic_exploration = [3, 4, 7, 10, 12, 18, 25, 30, 40, 50, 60]

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, atlantic_exploration, pacific_exploration, arctic_exploration,
             colors=['#ff7f0e', '#2ca02c', '#d62728'], alpha=0.75)

plt.xticks(years, rotation=30)
ax.grid(True, linestyle='-', linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

line1 = ax.plot(years, atlantic_exploration, 'o-', label='Atlantic', linestyle=':', marker='s', markersize=6)[0]
line2 = ax.plot(years, pacific_exploration, '*-', label='Pacific', linestyle='--', marker='d', markersize=6)[0]
line3 = ax.plot(years, arctic_exploration, 's-', label='Arctic', linestyle='-.', marker='^', markersize=6)[0]

ax.legend(loc='upper left', fontsize=10, fancybox=True, shadow=True)

plt.tight_layout()
plt.show()