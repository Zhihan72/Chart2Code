import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

years = np.arange(2000, 2021)
europe = [5, 6, 7, 9, 10, 12, 14, 16, 19, 21, 23, 26, 29, 31, 34, 36, 39, 41, 44, 47, 50]
asia = [1, 2, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 19, 21, 23, 26, 28, 30, 33, 35, 38]
global_target = [20] * len(years)

fig, ax = plt.subplots(figsize=(14, 8))
new_palette = sns.color_palette("Set2", 3)

ax.plot(years, europe, marker='s', linestyle='-', linewidth=2, color=new_palette[0])
ax.plot(years, asia, marker='^', linestyle='-', linewidth=2, color=new_palette[1])
ax.plot(years, global_target, linestyle='--', color='gray')

ax.set_title("Renewable Energy Trends (2000-2020)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Renewable Energy (%)", fontsize=12)

ax2 = ax.twinx()
ax2.set_ylabel('Secondary Metric (Units)', fontsize=12)
ax2.plot(years, [x + 20 for x in asia], linestyle='-', linewidth=1, color='blue', alpha=0.3)

plt.tight_layout()
plt.show()