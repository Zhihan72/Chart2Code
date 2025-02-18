import matplotlib.pyplot as plt
import numpy as np

# Step 1: Defining backstory and data
# Title: "Internet Usage by Device Over the Last Decade"
# The chart explores how internet usage has varied across different devices (Desktop, Mobile, Tablet, and Smart TV) 
# from 2011 to 2021.

years = np.arange(2011, 2022)
desktop_usage = [54, 50, 47, 44, 40, 36, 33, 31, 30, 28, 25]  # Percentage
mobile_usage = [20, 25, 30, 35, 40, 45, 50, 52, 55, 57, 60]   # Percentage
tablet_usage = [10, 12, 14, 15, 16, 17, 18, 18, 18, 18, 18]    # Percentage
smart_tv_usage = [2, 3, 4, 5, 6, 8, 10, 12, 14, 17, 20]       # Percentage

# Step 2: Plotting the data
fig, ax = plt.subplots(figsize=(14, 8))

# Bar Width for horizontal bar chart
bar_width = 0.15

# Positions of bars on x-axis for each year and device
r1 = np.arange(len(years))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]

# Plotting the bars
ax.bar(r1, desktop_usage, color='b', width=bar_width, edgecolor='grey', label='Desktop')
ax.bar(r2, mobile_usage, color='r', width=bar_width, edgecolor='grey', label='Mobile')
ax.bar(r3, tablet_usage, color='g', width=bar_width, edgecolor='grey', label='Tablet')
ax.bar(r4, smart_tv_usage, color='y', width=bar_width, edgecolor='grey', label='Smart TV')

# Adding titles and labels
ax.set_title('Internet Usage by Device Over the Last Decade', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Percentage (%)', fontsize=14)
ax.set_xticks([r + bar_width for r in range(len(years))])
ax.set_xticklabels(years, rotation=45)

# Adding legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)

# Adding grid
ax.grid(True, linestyle='--', alpha=0.6, axis='y')

# Adding average lines for each device
average_desktop = np.mean(desktop_usage)
average_mobile = np.mean(mobile_usage)
average_tablet = np.mean(tablet_usage)
average_tv = np.mean(smart_tv_usage)

ax.axhline(average_desktop, color='blue', linestyle='--', linewidth=1)
ax.text(len(years)-0.5, average_desktop+0.5, f'Avg Desktop: {average_desktop:.1f}%', color='blue', fontsize=10)

ax.axhline(average_mobile, color='red', linestyle='--', linewidth=1)
ax.text(len(years)-0.5, average_mobile+0.5, f'Avg Mobile: {average_mobile:.1f}%', color='red', fontsize=10)

ax.axhline(average_tablet, color='green', linestyle='--', linewidth=1)
ax.text(len(years)-0.5, average_tablet+0.5, f'Avg Tablet: {average_tablet:.1f}%', color='green', fontsize=10)

ax.axhline(average_tv, color='yellow', linestyle='--', linewidth=1)
ax.text(len(years)-0.5, average_tv+0.5, f'Avg Smart TV: {average_tv:.1f}%', color='yellow', fontsize=10)

# Improving layout to avoid overlaps
plt.tight_layout()
plt.show()