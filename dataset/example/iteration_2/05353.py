import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking the Global Mean Temperature Change Over the Last Century
# Here's a detailed analysis on how the average temperature has changed globally during each decade from 1920 to 2020.

# Decades from 1920 to 2020
decades = np.arange(1920, 2030, 10)

# Mean temperature change in Celsius for each decade (artificial data)
temp_changes = [0.0, 0.1, 0.15, 0.2, 0.25, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2]

# Initialize the plot
plt.figure(figsize=(14, 8))

# Plotting the Global Mean Temperature Change trend
plt.plot(decades, temp_changes, marker='o', linestyle='-', color='r', linewidth=2, label='Temperature Change')

# Filling the area under the line plot for better visual emphasis
plt.fill_between(decades, temp_changes, color='r', alpha=0.2)

# Adding labels for each data point
for i in range(len(decades)):
    plt.text(decades[i], temp_changes[i]+0.02, f'{temp_changes[i]:.2f}°C', ha='center', fontsize=10)

# Adding title and labels
plt.title('Global Mean Temperature Change Over the Last Century', fontsize=18, fontweight='bold')
plt.xlabel('Decade', fontsize=14)
plt.ylabel('Temperature Change (℃)', fontsize=14)

# Customizing the grid
plt.grid(True, linestyle='--', alpha=0.7)

# Adding a legend
plt.legend(loc='upper left', fontsize=12)

# Custom x-axis ticks
plt.xticks(decades, rotation=45)

# Automatically adjust the layout to prevent text overlapping
plt.tight_layout()

# Display the plot
plt.show()