import matplotlib.pyplot as plt
import numpy as np

cities = ['City A', 'City B', 'City C', 'City D', 'City E', 'City F', 'City G']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

rainfall_data = np.array([
    [78, 95, 89, 120, 150, 80, 70, 55, 60, 85, 100, 110],
    [52, 65, 70, 85, 100, 65, 50, 45, 55, 75, 80, 90],
    [85, 90, 95, 105, 120, 90, 80, 60, 70, 95, 110, 130],
    [60, 75, 80, 95, 110, 75, 65, 55, 60, 80, 95, 105],
    [90, 105, 110, 130, 150, 100, 90, 75, 85, 110, 125, 140],
    [60, 85, 75, 80, 100, 105, 85, 60, 65, 90, 95, 105],
    [70, 80, 85, 100, 120, 90, 80, 70, 75, 95, 100, 115]
])

mean_rainfall = np.mean(rainfall_data)
deviations_from_mean = rainfall_data - mean_rainfall

fig, ax = plt.subplots(figsize=(14, 8))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

marker_types = ['o', 's', 'D', '^', 'v', 'p', '*']
line_styles = ['-', '--', '-.', ':', '-', '--', '-.']

for idx, city in enumerate(cities):
    ax.plot(months, deviations_from_mean[idx], 
            color=colors[idx], 
            marker=marker_types[idx], 
            linestyle=line_styles[idx], 
            label=city)

ax.axhline(0, color='gray', linewidth=1.3, linestyle='--')
ax.set_title('Diverging Line Chart: Rainfall Deviation', fontsize=18, fontweight='bold', fontstyle='italic')
ax.set_xlabel('Months', fontsize=14, fontweight='bold')
ax.set_ylabel('Deviation from Mean Rainfall (mm)', fontsize=14, fontweight='bold')
ax.legend(title='Cities', loc='upper left', fontsize=12)

ax.grid(color='gray', linestyle=':', linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

fig.tight_layout()
plt.show()