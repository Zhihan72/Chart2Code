import matplotlib.pyplot as plt
import numpy as np

# Data representing average daily hours spent online
years = np.array([2010, 2012, 2014, 2016, 2018, 2020, 2022])
avg_daily_hours_online = np.array([1.5, 2.3, 3.2, 4.0, 4.8, 5.5, 6.1])

# Create a figure and add a subplot
fig, ax = plt.subplots(figsize=(10, 6))

# Single plot for average daily hours online
color = 'tab:blue'
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Average Daily Hours Online', fontsize=14, color=color)
ax.plot(years, avg_daily_hours_online, color=color, marker='s', markersize=8, 
        linestyle='--', linewidth=2, label='Avg Daily Hours Online')
ax.tick_params(axis='y', labelcolor=color)

# Title and grid
plt.title('Digital Revolution: Online Activity Trends', fontsize=16, fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.7)

# Add Legend
ax.legend(loc='upper left', fontsize=12, frameon=True)

# Automatically adjust the layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()