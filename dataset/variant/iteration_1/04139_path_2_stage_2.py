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

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10), gridspec_kw={'width_ratios': [3, 1]})

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

total_activity_by_zone = activity_data.sum(axis=1)
total_activity_by_day = activity_data.sum(axis=0)

# Sort total activity by zone in descending order
sorted_indices_zones = np.argsort(total_activity_by_zone)[::-1]
sorted_zones = [city_zones[i] for i in sorted_indices_zones]
sorted_activity_by_zone = total_activity_by_zone[sorted_indices_zones]

# Plot sorted bar chart for zones
ax2.barh(np.arange(len(sorted_zones)), sorted_activity_by_zone, color='steelblue')
ax2.set_yticks(np.arange(len(sorted_zones)))
ax2.set_yticklabels(sorted_zones)
ax2.set_xlabel('Total Data (GB)', fontsize=12)
ax2.set_title('Network Activity by Zone Overview', fontsize=14, fontweight='bold', pad=20)

# Sort total activity by day in descending order
sorted_indices_days = np.argsort(total_activity_by_day)[::-1]
sorted_days = [days[i] for i in sorted_indices_days]
sorted_activity_by_day = total_activity_by_day[sorted_indices_days]

# Plot sorted bar chart for days
ax2_2 = ax2.twinx()
ax2_2.bar(np.arange(len(sorted_days)), sorted_activity_by_day, alpha=0.7, color='orange', width=0.3, align='center')
ax2_2.set_xticks(np.arange(len(sorted_days)))
ax2_2.set_xticklabels(sorted_days)
ax2_2.set_ylabel('Daily Data (GB)', fontsize=12)
ax2_2.set_title('Daily Network Activity Overview', fontsize=14, fontweight='bold', pad=20)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()