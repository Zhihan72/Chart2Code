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

temperature_data = np.array([
    [7, 5, 13, 10, 17, 24, 21, 6, 20, 15, 23, 10],
    [4, 2, 10, 7, 19, 15, 22, 3, 18, 13, 22, 8],
    [10, 8, 15, 12, 20, 28, 25, 9, 24, 18, 27, 12],
    [6, 4, 12, 9, 16, 23, 20, 5, 19, 14, 22, 9],
    [5, 3, 11, 8, 16, 21, 19, 4, 17, 12, 20, 7]
])

# Shuffled colors
color_rainfall = ['#9467bd', '#1f77b4', '#d62728', '#2ca02c', '#ff7f0e']
color_temperature = ['#c5b0d5', '#98df8a', '#ff9896', '#aec7e8', '#ffbb78']

fig, ax1 = plt.subplots(figsize=(14, 8))

bottoms = np.zeros(len(months))
for idx, city in enumerate(cities):
    ax1.bar(months, rainfall_data[idx], bottom=bottoms, color=color_rainfall[idx], alpha=0.7, label=f'{city} Rainfall')
    bottoms += rainfall_data[idx]

ax1.set_title('Annual Rainfall and Temperature Distribution\nAcross Major Cities', fontsize=18, fontweight='bold')
ax1.set_xlabel('Months', fontsize=14)
ax1.set_ylabel('Average Rainfall (mm)', fontsize=14, color='navy')
ax1.yaxis.grid(True, linestyle='--', color='gray', alpha=0.7)
ax1.tick_params(axis='y', labelcolor='navy')
ax1.legend(loc='upper left', title='Cities', bbox_to_anchor=(1.02, 1), borderaxespad=0.)

ax2 = ax1.twinx()
for idx, city in enumerate(cities):
    ax2.plot(months, temperature_data[idx], marker='o', color=color_temperature[idx], linestyle='-', linewidth=2, markersize=6, label=f'{city} Temperature')

ax2.set_ylabel('Average Temperature (°C)', fontsize=14, color='firebrick')
ax2.tick_params(axis='y', labelcolor='firebrick')

fig.tight_layout()
plt.show()