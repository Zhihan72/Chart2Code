import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])
screen_time_data = {
    '12-13 years': np.array([3.4, 4.5, 3.2, 4.0, 4.2]), 
    '14-15 years': np.array([4.5, 3.5, 3.7, 4.8, 4.3]),
    '16-17 years': np.array([-4.2, -4.7, -5.2, -4.9, -4.0])
}

fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.35

for i, (age_group, data) in enumerate(screen_time_data.items()):
    ax.barh(years if i == 0 else -years, data, bar_width, color=f'C{i}', alpha=0.7)

ax.set_xlabel('Average Screen Time (Hours per Day)', fontsize=12)
ax.set_ylabel('Year', fontsize=12)
ax.set_yticks(years)
ax.set_yticklabels(years)
plt.axvline(0, color='black', linewidth=0.8)
plt.tight_layout()

plt.show()