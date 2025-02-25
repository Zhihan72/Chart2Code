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
ax1.scatter(months, precipitation_sunnyville, color='chocolate', marker='o', s=100, edgecolors='black')
ax1.scatter(months, precipitation_rainytown, color='darkcyan', marker='s', s=100, edgecolors='black')

# Create secondary Y-axis for temperature data
ax2 = ax1.twinx()
ax2.scatter(months, temperature_sunnyville, color='olive', marker='^', s=100, edgecolors='black')
ax2.scatter(months, temperature_rainytown, color='orchid', marker='v', s=100, edgecolors='black')

# Titles and labels
ax1.set_xlabel("Months", fontsize=12)
ax1.set_ylabel("Precipitation (mm)", fontsize=12)
ax2.set_ylabel("Temperature (°C)", fontsize=12)

# Customize ticks
ax1.set_xticks(np.arange(len(months)))
ax1.set_xticklabels(months)
ax1.tick_params(axis='x', rotation=45)

# Show the plot
plt.tight_layout()
plt.show()