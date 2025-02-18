import matplotlib.pyplot as plt
import numpy as np

city_zones = ["Tech Hub", "Commercial", "University", "Downtown", "Suburbs", "Residential", "Parks", "Industrial"]
days = ["Sun", "Wed", "Mon", "Fri", "Tue", "Sat", "Thu"]

activity_data = np.array([
    [120, 130, 125, 150, 160, 200, 180],
    [80, 90, 85, 110, 115, 140, 130],
    [100, 105, 110, 120, 130, 160, 145],
    [50, 55, 60, 65, 70, 75, 70],
    [40, 45, 50, 55, 60, 80, 75],
    [70, 75, 80, 85, 90, 110, 95],
    [150, 160, 155, 170, 180, 210, 220], 
    [60, 65, 70, 75, 80, 100, 90]
])

fig, ax1 = plt.subplots(figsize=(10, 8))

heatmap = ax1.imshow(activity_data, cmap='coolwarm', aspect='auto')
ax1.set_xticks(np.arange(len(days)))
ax1.set_xticklabels(days)
ax1.set_yticks(np.arange(len(city_zones)))
ax1.set_yticklabels(city_zones)
ax1.set_title('CyberCity Network Usage Overview', fontsize=16, fontweight='bold', pad=20)

for i in range(len(city_zones)):
    for j in range(len(days)):
        ax1.text(j, i, f'{activity_data[i, j]} GB', va='center', ha='center', color='black', fontsize=9)

cbar = fig.colorbar(heatmap, ax=ax1, orientation='vertical')
cbar.set_label('Data Transfer (GB)', fontsize=12)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()