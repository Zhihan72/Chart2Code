import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2022)
startups_founded = [50, 55, 60, 85, 120, 135, 150, 170, 200, 220]
startups_founded_region2 = [30, 40, 50, 65, 80, 100, 120, 130, 150, 180]

years_sorted_indices = np.argsort(startups_founded)
startups_founded_sorted = np.array(startups_founded)[years_sorted_indices]
years_sorted = np.array(years)[years_sorted_indices]

years_sorted_indices_region2 = np.argsort(startups_founded_region2)
startups_founded_region2_sorted = np.array(startups_founded_region2)[years_sorted_indices_region2]
years_sorted_region2 = np.array(years)[years_sorted_indices_region2]

years_line = np.arange(2012, 2022)
employees = [1000, 1100, 1050, 1300, 1400, 1600, 1750, 1800, 2100, 2300]
revenue = [400, 500, 600, 850, 900, 1100, 1300, 1500, 1900, 2500]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 2]})

ax1.bar(years_sorted - 0.2, startups_founded_sorted, width=0.4, color=plt.cm.tab20c(0), edgecolor='black')
ax1.bar(years_sorted_region2 + 0.2, startups_founded_region2_sorted, width=0.4, color=plt.cm.tab20c(4), edgecolor='black')

ax1.set_title('Growth of Tech Startups (Sorted)', fontsize=18, weight='bold', loc='left', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Number of Startups Founded', fontsize=14)

for bar, value in zip(ax1.patches, list(startups_founded_sorted) + list(startups_founded_region2_sorted)):
    ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 3, f'{value}', ha='center', va='bottom', fontsize=12)

ax2.plot(years_line, employees, marker='o', color='skyblue', markerfacecolor='blue', markersize=9, linewidth=3)
ax2.plot(years_line, revenue, marker='s', color='orange', markerfacecolor='red', markersize=9, linewidth=3, linestyle='--')

ax2.set_title('Tech Industry Employment & Revenue', fontsize=18, weight='bold', loc='left', pad=20)
ax2.set_xlabel('Year', fontsize=14)
ax2.set_ylabel('Number of Employees / Revenue ($1000s)', fontsize=14)
ax2.set_xlim(2011, 2022)
ax2.set_ylim(500, 2700)

fig.tight_layout(pad=3.0)
fig.suptitle('Tech Startups, Employment, and Revenue Trends (2012-2021)', fontsize=20, weight='bold')
plt.show()