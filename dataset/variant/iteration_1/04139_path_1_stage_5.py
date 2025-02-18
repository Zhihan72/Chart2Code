import matplotlib.pyplot as plt
import numpy as np

city_zones = ["Downtown", "Residential", "Commercial", "Industrial", "Parks", "Suburbs", "Tech Hub", "University", "Harbor"]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

activity_data = np.array([
    [120, 130, 125, 150, 160, 200, 180], 
    [80, 90, 85, 110, 115, 140, 130],     
    [100, 105, 110, 120, 130, 160, 145],  
    [50, 55, 60, 65, 70, 75, 70],         
    [40, 45, 50, 55, 60, 80, 75],         
    [70, 75, 80, 85, 90, 110, 95],        
    [150, 160, 155, 170, 180, 210, 220],  
    [60, 65, 70, 75, 80, 100, 90],        
    [90, 95, 120, 110, 100, 130, 120]    
])

# Initialize the figure and create subplots
fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(20, 10), gridspec_kw={'width_ratios': [1, 3]})

# Calculate total activities
total_activity_by_zone = activity_data.sum(axis=1)
total_activity_by_day = activity_data.sum(axis=0)

# Sort data in descending order
sorted_indices_zone = np.argsort(total_activity_by_zone)
sorted_total_activity_by_zone = total_activity_by_zone[sorted_indices_zone]

sorted_indices_day = np.argsort(total_activity_by_day)
sorted_total_activity_by_day = total_activity_by_day[sorted_indices_day]

# Subplot for sorted total activity by zone
ax2.barh(np.arange(len(city_zones)), sorted_total_activity_by_zone, color='tomato', linestyle='--', edgecolor='black')
ax2.set_yticks(np.arange(len(city_zones)))
ax2.set_yticklabels(np.array(city_zones)[sorted_indices_zone])
ax2.grid(True, linestyle=':', linewidth=0.5)

# Additional subplot for sorted total activity by day
ax2_2 = ax2.twinx()
ax2_2.bar(np.arange(len(days)), sorted_total_activity_by_day, alpha=0.7, color='cyan', width=0.3, align='center', hatch='/')
ax2_2.set_xticks(np.arange(len(days)))
ax2_2.set_xticklabels(np.array(days)[sorted_indices_day])
ax2_2.grid(linestyle='-.', linewidth=0.5)

# Plot the heatmap on the second subplot (ax1)
heatmap = ax1.imshow(activity_data, cmap='viridis', aspect='auto')

# Add labels and title for the heatmap
ax1.set_xticks(np.arange(len(days)))
ax1.set_yticks(np.arange(len(city_zones)))
ax1.set_xticklabels(days)
ax1.set_yticklabels(city_zones)
ax1.grid(False)  # Removed grid for clarity on the heatmap

# Annotate cells with the data values
for i in range(len(city_zones)):
    for j in range(len(days)):
        ax1.text(j, i, f'{activity_data[i, j]}', va='center', ha='center', color='white', fontsize=9)

# Add color bar to the heatmap
cbar = fig.colorbar(heatmap, ax=ax1, orientation='vertical')
cbar.set_label('Activity Level')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()