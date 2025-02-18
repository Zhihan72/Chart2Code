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
colors = ['#d62728', '#2ca02c', '#ff7f0e', '#1f77b4', '#8c564b', '#e377c2', '#bcbd22']

for idx, city in enumerate(cities):
    ax.bar(months, deviations_from_mean[idx], color=colors[idx], label=city)

ax.axhline(0, color='black',linewidth=1.3)
ax.set_title('Diverging Bar Chart: Rainfall Deviation from Mean',fontsize=18, fontweight='bold')
ax.set_xlabel('Months', fontsize=14)
ax.set_ylabel('Deviation from Mean Rainfall (mm)', fontsize=14)
ax.legend(title='Cities')

fig.tight_layout()
plt.show()