import matplotlib.pyplot as plt
import numpy as np

# Define city zones and days of the week
city_zones = ["Downtown", "Residential", "Commercial", "Industrial", "Parks", "Suburbs", "Tech Hub", "University", "Harbor"]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Network activity data (in gigabytes transfer) over a week (rows: city zones, columns: days)
activity_data = np.array([
    [120, 130, 125, 150, 160, 200, 180],  # Downtown
    [80, 90, 85, 110, 115, 140, 130],     # Residential
    [100, 105, 110, 120, 130, 160, 145],  # Commercial
    [50, 55, 60, 65, 70, 75, 70],         # Industrial
    [40, 45, 50, 55, 60, 80, 75],         # Parks
    [70, 75, 80, 85, 90, 110, 95],        # Suburbs
    [150, 160, 155, 170, 180, 210, 220],  # Tech Hub
    [60, 65, 70, 75, 80, 100, 90],        # University
    [90, 95, 120, 110, 100, 130, 120]     # Harbor
])

# Initialize the figure and create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10), gridspec_kw={'width_ratios': [3, 1]})

# Plot the heatmap on the first subplot (ax1)
heatmap = ax1.imshow(activity_data, cmap='coolwarm', aspect='auto')

# Add labels and title for the heatmap
ax1.set_xticks(np.arange(len(days)))
ax1.set_xticklabels(days)
ax1.set_yticks(np.arange(len(city_zones)))
ax1.set_yticklabels(city_zones)
ax1.set_title('Network Activity in CyberCity Over a Week', fontsize=16, fontweight='bold', pad=20)

# Annotate cells with the data values
for i in range(len(city_zones)):
    for j in range(len(days)):
        ax1.text(j, i, f'{activity_data[i, j]} GB', va='center', ha='center', color='black', fontsize=9)

# Add color bar to the heatmap
cbar = fig.colorbar(heatmap, ax=ax1, orientation='vertical')
cbar.set_label('Data Transferred (GB)', fontsize=12)

# Plot bar charts showing total activity for each zone and each day on the second subplot (ax2)
total_activity_by_zone = activity_data.sum(axis=1)
total_activity_by_day = activity_data.sum(axis=0)

# Subplot for total activity by zone
ax2.barh(np.arange(len(city_zones)), total_activity_by_zone, color='steelblue')
ax2.set_yticks(np.arange(len(city_zones)))
ax2.set_yticklabels(city_zones)
ax2.set_xlabel('Total Data Transferred (GB)', fontsize=12)
ax2.set_title('Total Network Activity by Zone', fontsize=14, fontweight='bold', pad=20)

# Additional subplot for total activity by day
ax2_2 = ax2.twinx()
ax2_2.bar(np.arange(len(days)), total_activity_by_day, alpha=0.7, color='orange', width=0.3, align='center')
ax2_2.set_xticks(np.arange(len(days)))
ax2_2.set_xticklabels(days)
ax2_2.set_ylabel('Total Data Transferred (GB)', fontsize=12)
ax2_2.set_title('Total Network Activity by Day', fontsize=14, fontweight='bold', pad=20)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()