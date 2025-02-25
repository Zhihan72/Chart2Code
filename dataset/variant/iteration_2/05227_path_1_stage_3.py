import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2022)
startups_founded = [50, 55, 60, 85, 120, 135, 150, 170, 200, 220]

# Sorting the data for the bar chart
sorted_indices = np.argsort(startups_founded)
years_sorted = years[sorted_indices]
startups_founded_sorted = np.array(startups_founded)[sorted_indices]

years_line = np.arange(2012, 2022)
employees = [1000, 1100, 1050, 1300, 1400, 1600, 1750, 1800, 2100, 2300]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 2]})

# Sorted bar chart
ax1.bar(years_sorted, startups_founded_sorted, color='blue', edgecolor='black')
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
ax1.set_xlim(2011, 2022)

# Line chart remains unchanged
ax2.plot(years_line, employees, marker='o', color='blue', markerfacecolor='blue', markersize=9, linewidth=3)
ax2.yaxis.grid(True, linestyle='--', alpha=0.7)
ax2.set_xlim(2011, 2022)
ax2.set_ylim(900, 2500)

fig.tight_layout(pad=3.0)

plt.show()