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

colors = ['#FF6347', '#FFD700', '#90EE90', '#1E90FF', '#9370DB']

fig, ax = plt.subplots(figsize=(12, 8))

midpoint_consumption = consumption.sum(axis=0) / 2

for i, age_group in enumerate(age_groups):
    pos_vals = np.where(consumption[i] >= midpoint_consumption, consumption[i] - midpoint_consumption, 0)
    neg_vals = np.where(consumption[i] < midpoint_consumption, midpoint_consumption - consumption[i], 0)
    ax.bar(years, pos_vals, bottom=midpoint_consumption, color=colors[i], label=f'{age_group}+')
    ax.bar(years, -neg_vals, bottom=midpoint_consumption, color=colors[i], label=f'{age_group}-', hatch='//')

ax.set_title('Coffee Consumption Trends (2010-2020)', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Deviation from Midpoint', fontsize=14)

ax.legend(title='Age Group', loc='upper left', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.6)
plt.axhline(0, color='black', linewidth=0.8)
plt.tight_layout()
plt.show()