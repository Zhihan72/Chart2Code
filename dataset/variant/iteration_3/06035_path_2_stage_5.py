import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])

screen_time_data = {
    '12-13': np.array([3.4, 3.2, 4.2, 4.0, 4.5]),
    '14-15': np.array([4.3, 3.7, 3.5, 4.8, 4.5]),
    '16-17': np.array([4.7, 5.2, 4.0, 4.2, 4.9])
}

mid_value = np.mean([data for data in screen_time_data.values()])

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.5
for i, year in enumerate(years):
    data = []
    base_value = 0
    
    for age_group in screen_time_data:
        positive_value = screen_time_data[age_group][i] - mid_value
        data.append(positive_value)
        
    ax.barh(year, data, height=bar_width, left=base_value,
            label=age_group)

ax.set_xlabel('Deviation (Hours)', fontsize=12)
ax.set_title('Teen Screen Time (2018-22)', fontsize=14, fontweight='bold')
ax.set_yticks(years)
ax.set_yticklabels(years)
ax.legend(title='Age', loc='best', fancybox=True, shadow=True, frameon=False)

ax.grid(True, which='major', linestyle='-', linewidth=0.75, alpha=0.6)

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.tight_layout()

plt.show()