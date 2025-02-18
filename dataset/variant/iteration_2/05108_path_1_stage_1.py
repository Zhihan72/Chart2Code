import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
age_groups = ['18-25', '26-35', '36-45', '46-60', '60+']
consumption = np.array([
    [100, 150, 120, 180, 140, 200, 160, 220, 180, 240, 200], # Random mix of original values for 18-25
    [90, 110, 130, 100, 150, 170, 120, 190, 130, 210, 230],  # Random mix of original values for 26-35
    [70, 90, 80, 110, 100, 130, 120, 140, 110, 150, 160],    # Random mix of original values for 36-45
    [50, 70, 60, 90, 80, 110, 100, 120, 90, 130, 140],       # Random mix of original values for 46-60
    [30, 40, 35, 50, 45, 60, 55, 65, 50, 70, 75]             # Random mix of original values for 60+
])

colors = ['#FF6347', '#FFD700', '#90EE90', '#1E90FF', '#9370DB']

fig, ax = plt.subplots(1, 1, figsize=(12, 8))

bottom_vals = np.zeros_like(consumption[0])
for i, age_group in enumerate(age_groups):
    ax.bar(years, consumption[i], bottom=bottom_vals, color=colors[i], label=f'{age_group} years')
    bottom_vals += consumption[i]

cumulative_consumption = consumption.sum(axis=0)
ax.plot(years, cumulative_consumption, color='black', marker='o', linestyle='-', linewidth=2, markersize=6, label='Total Consumption')

ax.set_title('Decadal Trends in Coffee Consumption\nin the Town of Coffeeburg (2010-2020)', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Years', fontsize=14)
ax.set_ylabel('Cups of Coffee Consumed (in thousands)', fontsize=14)

ax.legend(title='Age Groups', loc='upper left', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()