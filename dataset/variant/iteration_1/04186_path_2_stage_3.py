import matplotlib.pyplot as plt
import numpy as np

# Data
device_labels = ['Desktop', 'Mobile', 'Tablet', 'Smart TV', 'Smartwatch']
usage_data = {
    'Desktop': [54, 50, 47, 44, 40, 36, 33, 31, 30, 28, 25],
    'Mobile': [20, 25, 30, 35, 40, 45, 50, 52, 55, 57, 60],
    'Tablet': [10, 12, 14, 15, 16, 17, 18, 18, 18, 18, 18],
    'Smart TV': [2, 3, 4, 5, 6, 8, 10, 12, 14, 17, 20],
    'Smartwatch': [1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 18]
}

# Calculate the total usage for each category
total_usage = {device: sum(usage) for device, usage in usage_data.items()}

# Sort devices based on total usage
sorted_devices = sorted(total_usage.items(), key=lambda x: x[1], reverse=True)

fig, ax = plt.subplots(figsize=(10, 6))

colors = ['b', 'r', 'g', 'y', 'm']
bars = ax.bar([device[0] for device in sorted_devices], [device[1] for device in sorted_devices], 
              color=colors[:len(sorted_devices)], edgecolor='grey')

# Sorting the legend to match the sorted bars
ax.legend(bars, [device[0] for device in sorted_devices], loc='upper left')

ax.set_ylabel('Total Usage Over Years')
ax.set_xlabel('Device Type')
ax.set_title('Total Device Usage Sorted Bar Chart')
ax.grid(True, linestyle='--', alpha=0.6, axis='y')

plt.tight_layout()
plt.show()