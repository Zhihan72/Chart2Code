import matplotlib.pyplot as plt
import numpy as np

# Decades from 1920 to 2020
decades = np.arange(1920, 2030, 10)

# Mean temperature change in Celsius for each decade (artificial data)
temp_changes = [0.0, 0.1, 0.15, 0.2, 0.25, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2]

# Initialize the plot
plt.figure(figsize=(14, 8))

# Plotting the Global Mean Temperature Change trend
plt.plot(decades, temp_changes, marker='o', linestyle='-', color='r', linewidth=2)

# Filling the area under the line plot
plt.fill_between(decades, temp_changes, color='r', alpha=0.2)

# Custom x-axis ticks
plt.xticks(decades, rotation=45)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()