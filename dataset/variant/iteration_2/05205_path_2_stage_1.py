import matplotlib.pyplot as plt
import numpy as np

# Define the months
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Define the precipitation data (mm)
precipitation_sunnyville = np.array([78, 52, 43, 32, 34, 20, 15, 22, 42, 61, 74, 85])
precipitation_rainytown = np.array([180, 160, 160, 150, 140, 130, 120, 130, 150, 160, 180, 190])

# Define the temperature data (°C)
temperature_sunnyville = np.array([10, 12, 15, 18, 22, 25, 28, 28, 24, 20, 16, 12])
temperature_rainytown = np.array([5, 6, 9, 12, 16, 20, 22, 21, 18, 13, 9, 6])

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot precipitation data on primary Y-axis
scatter1 = ax1.scatter(months, precipitation_sunnyville, color='darkorange', marker='x', s=120, edgecolors='brown', label='Sunyville Precipitation')
scatter2 = ax1.scatter(months, precipitation_rainytown, color='lightcoral', marker='D', s=120, edgecolors='black', label='Rainytown Precipitation')

# Create secondary Y-axis for temperature data
ax2 = ax1.twinx()
scatter3 = ax2.scatter(months, temperature_sunnyville, color='darkcyan', marker='*', s=120, edgecolors='navy', label='Sunnyville Temperature')
scatter4 = ax2.scatter(months, temperature_rainytown, color='orchid', marker='o', s=120, edgecolors='black', label='Rainytown Temperature')

# Titles and labels
ax1.set_title("Monthly Precipitation and Temperature in Sunnyville versus Rainytown", fontsize=16, fontweight='bold')
ax1.set_xlabel("Months", fontsize=12)
ax1.set_ylabel("Precipitation (mm)", fontsize=12, color='darkorange')
ax2.set_ylabel("Temperature (°C)", fontsize=12, color='darkcyan')

# Grid settings
ax1.grid(True, linestyle='-', color='gray', alpha=0.6)

# Customize ticks for readability
ax1.set_xticks(np.arange(len(months)))
ax1.set_xticklabels(months)
ax1.tick_params(axis='x', colors='black', rotation=30)
ax1.tick_params(axis='y', colors='darkorange')
ax2.tick_params(axis='y', colors='darkcyan')

# Legends
scatter1.set_alpha(0.75)
scatter2.set_alpha(0.75)
scatter3.set_alpha(0.75)
scatter4.set_alpha(0.75)

handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(handles1 + handles2, labels1 + labels2, loc='best', fontsize=10, frameon=True, framealpha=0.9)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()