import matplotlib.pyplot as plt
import numpy as np

# Data representing internet penetration rate (%) and average daily hours spent online
years = np.array([2010, 2012, 2014, 2016, 2018, 2020, 2022])
penetration_rate = np.array([20, 30, 45, 55, 65, 75, 85])
avg_daily_hours_online = np.array([1.5, 2.3, 3.2, 4.0, 4.8, 5.5, 6.1])

# Create a figure and add a subplot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Line plot for internet penetration rate
color1 = 'tab:blue'
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Internet Penetration Rate (%)', fontsize=14, color=color1)
ax1.plot(years, penetration_rate, color=color1, marker='o', markersize=8, 
         linestyle='-', linewidth=2, label='Penetration Rate (%)')
ax1.tick_params(axis='y', labelcolor=color1)

# Create a second y-axis to plot the average daily hours online
ax2 = ax1.twinx()
color2 = 'tab:orange'
ax2.set_ylabel('Average Daily Hours Online', fontsize=14, color=color2)
ax2.plot(years, avg_daily_hours_online, color=color2, marker='s', markersize=8, 
         linestyle='--', linewidth=2, label='Avg Daily Hours Online')
ax2.tick_params(axis='y', labelcolor=color2)

# Title and grid
plt.title('Digital Revolution: Internet Penetration and Online Activity Trends', fontsize=16, fontweight='bold')
ax1.grid(True, linestyle='--', alpha=0.7)

# Add Legends
fig.legend(loc='upper left', bbox_to_anchor=(0.15, 0.85), fontsize=12, frameon=True)

# Automatically adjust the layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()