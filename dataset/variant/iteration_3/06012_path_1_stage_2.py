import numpy as np
import matplotlib.pyplot as plt

# Original Data Preparation
brightness = np.array([5.1, 5.4, 5.7, 6.0, 6.3, 6.5, 7.0, 7.5, 8.0, 4.2, 4.5, 4.8, 3.1, 3.3,
                       3.9, 2.7, 2.5, 1.0, -1.5, 0.8, -1.0, -2.4, -2.3])
temperature = np.array([3000, 3200, 3500, 3700, 4000, 4300, 5000, 5200, 6000, 7000, 8000,
                        9000, 12000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 
                        50000, 55000, 60000])

# Additional Made-up Data
new_brightness = np.array([6.8, 7.8, 2.3, 1.6, 0.5, -1.2, 0.0, -3.0])
new_temperature = np.array([3600, 4800, 33000, 37000, 22000, 31000, 26000, 38000])

# Combine original and new data
combined_brightness = np.concatenate((brightness, new_brightness))
combined_temperature = np.concatenate((temperature, new_temperature))

# Sort combined data by brightness
sorted_indices = np.argsort(combined_brightness)
sorted_brightness = combined_brightness[sorted_indices]
sorted_temperature = combined_temperature[sorted_indices]

# Plot the sorted bar chart
fig, ax = plt.subplots(figsize=(14, 8))
ax.bar(range(len(sorted_brightness)), sorted_brightness, color='lightblue', edgecolor='black')

# Add titles and labels
ax.set_title('Sorted Bar Chart of Stellar Brightness with Additional Data', fontsize=16, fontweight='bold', wrap=True)
ax.set_xlabel('Star Index (sorted by brightness)', fontsize=12)
ax.set_ylabel('Absolute Magnitude (Brightness)', fontsize=12)
ax.invert_yaxis()

plt.tight_layout()
plt.show()