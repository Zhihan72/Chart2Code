import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
age_groups = ['18-25', '26-35', '36-45', '46-60', '60+']
consumption = np.array([
    [100, 150, 120, 180, 140, 200, 160, 220, 180, 240, 200],
    [90, 110, 130, 100, 150, 170, 120, 190, 130, 210, 230],
    [70, 90, 80, 110, 100, 130, 120, 140, 110, 150, 160],
    [50, 70, 60, 90, 80, 110, 100, 120, 90, 130, 140],
    [30, 40, 35, 50, 45, 60, 55, 65, 50, 70, 75]
])

new_colors = ['#32CD32', '#4682B4', '#FF4500', '#FFD700', '#8A2BE2']

fig, ax = plt.subplots(figsize=(10, 6))

midpoint_consumption = consumption.sum(axis=0) / 2

for i, age_group in enumerate(age_groups):
    pos_vals = np.where(consumption[i] >= midpoint_consumption, consumption[i] - midpoint_consumption, 0)
    neg_vals = np.where(consumption[i] < midpoint_consumption, midpoint_consumption - consumption[i], 0)
    ax.bar(years, pos_vals, bottom=midpoint_consumption, color=new_colors[i], label=f'{age_group}', hatch=None)
    ax.bar(years, -neg_vals, bottom=midpoint_consumption, color=new_colors[i], edgecolor='black', label=f'{age_group}', linestyle='-')

ax.set_title('Coffee Consumption Trends (2010-2020)', fontsize=14, weight='normal', pad=15)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Deviation from Midpoint', fontsize=12)

ax.legend(title='Age Group', loc='upper right', fontsize=10)
ax.grid(False)
ax.spines['top'].set_visible(True)
ax.spines['right'].set_visible(True)
ax.spines['bottom'].set_linewidth(1)
ax.spines['left'].set_linewidth(1.5)
plt.axhline(0, color='gray', linewidth=1)
plt.tight_layout()
plt.show()