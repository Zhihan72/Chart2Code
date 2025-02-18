import numpy as np
import matplotlib.pyplot as plt

# Data Preparation:
brightness = np.array([5.1, 5.4, 5.7, 6.0, 6.3, 6.5, 7.0, 7.5, 8.0, 4.2, 4.5, 4.8, 3.1, 3.3,
                       3.9, 2.7, 2.5, 1.0, -1.5, 0.8, -1.0, -2.4, -2.3])
temperature = np.array([3000, 3200, 3500, 3700, 4000, 4300, 5000, 5200, 6000, 7000, 8000,
                        9000, 12000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 
                        50000, 55000, 60000])

# Sort data by brightness in ascending order
sorted_indices = np.argsort(brightness)
sorted_brightness = brightness[sorted_indices]
sorted_temperature = temperature[sorted_indices]

# Plotting the sorted bar chart
fig, ax = plt.subplots(figsize=(12, 7))
ax.bar(range(len(sorted_brightness)), sorted_brightness, color='lightblue', edgecolor='black')

# Adding titles and labels to the plot
ax.set_title('Sorted Bar Chart of Stellar Brightness', fontsize=16, fontweight='bold', wrap=True)
ax.set_xlabel('Star Index (sorted by brightness)', fontsize=12)
ax.set_ylabel('Absolute Magnitude (Brightness)', fontsize=12)
ax.invert_yaxis()

# Display the plot
plt.tight_layout()
plt.show()