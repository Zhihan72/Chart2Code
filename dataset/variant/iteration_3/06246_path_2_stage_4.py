import matplotlib.pyplot as plt
import numpy as np

cities = ['City A', 'City B', 'City C', 'City D', 'City E']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

rainfall_data = np.array([
    [95, 78, 120, 89, 150, 70, 80, 110, 60, 85, 55, 100],
    [65, 52, 85, 70, 100, 50, 45, 75, 90, 80, 55, 65],
    [90, 85, 105, 95, 120, 80, 90, 130, 70, 95, 110, 60],
    [75, 60, 95, 80, 110, 65, 75, 105, 60, 80, 55, 95],
    [105, 90, 130, 110, 150, 90, 100, 140, 85, 110, 75, 125]
])

mean_rainfall = np.mean(rainfall_data, axis=0)
rainfall_dev = rainfall_data - mean_rainfall

color_rainfall = ['#9467bd', '#1f77b4', '#d62728', '#2ca02c', '#ff7f0e']

fig, ax = plt.subplots(figsize=(14, 8))

for idx, deviation in enumerate(rainfall_dev):
    ax.bar(months, deviation, bottom=mean_rainfall, color=color_rainfall[idx], alpha=0.7, label=f'{cities[idx]} Deviation')

ax.set_title('Rainfall Deviation from Avg', fontsize=18, fontweight='bold')
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Deviation (mm)', fontsize=14)
ax.axhline(y=0, color='gray', linewidth=1)
ax.yaxis.grid(True, linestyle='--', color='gray', alpha=0.7)
ax.legend(loc='upper left', title='City', bbox_to_anchor=(1.02, 1), borderaxespad=0.)

fig.tight_layout()
plt.show()