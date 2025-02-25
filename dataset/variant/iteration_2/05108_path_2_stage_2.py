import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
age_groups = ['18-25', '26-35', '36-45', '46-60', '60+']
consumption = np.array([
    [110, 130, 125, 170, 185, 215, 205, 255, 275, 295, 305], # 18-25
    [85, 120, 90, 115, 135, 160, 180, 175, 215, 225, 255],  # 26-35
    [75, 85, 95, 95, 115, 130, 125, 145, 155, 165, 180],    # 36-45
    [55, 50, 75, 85, 85, 95, 105, 115, 135, 125, 155],      # 46-60
    [35, 30, 45, 50, 55, 60, 50, 70, 75, 70, 85]            # 60+
])

colors = ['#FF6347', '#FFD700', '#90EE90', '#1E90FF', '#9370DB']

fig, ax = plt.subplots(1, 1, figsize=(12, 8))

bar_width = 0.15
indices = np.arange(len(years))

for i, age_group in enumerate(age_groups):
    ax.bar(indices + i * bar_width, consumption[i], width=bar_width, color=colors[i], label=f'{age_group} years')

ax.set_title('Decadal Trends in Coffee Consumption\nin the Town of Coffeeburg (2010-2020)', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Years', fontsize=14)
ax.set_ylabel('Cups of Coffee Consumed (in thousands)', fontsize=14)
ax.set_xticks(indices + bar_width * (len(age_groups) - 1) / 2)
ax.set_xticklabels(years)

ax.legend(title='Age Groups', loc='upper left', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()