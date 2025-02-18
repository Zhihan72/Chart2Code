import matplotlib.pyplot as plt
import numpy as np

gadgets = ['Handphones', 'Computers', 'Wrist Devices', 'Portable Screens', 'Game Stations', 'Headsets']
years = ['Yr 2018', 'Yr 2019', 'Yr 2020', 'Yr 2021', 'Yr 2022', 'Yr 2023']

data = np.array([
    [35, 33, 30, 28, 25, 22],
    [25, 26, 27, 26, 25, 24],
    [10, 12, 15, 18, 20, 22],
    [20, 18, 17, 15, 14, 13],
    [10, 11, 11, 13, 16, 19],
    [5, 7, 9, 11, 12, 15]
])

# Aggregate the smart devices and calculate gaming growth rate
smart_devices = data[0] + data[2] + data[3]
gaming_growth_rate = np.diff(data[4], prepend=data[4][0]) / data[4][0] * 100

# Prepare data for sorting
sorted_indices = np.argsort(data[:, -1])  # Sort based on the last year's data
sorted_data = data[sorted_indices]
sorted_gadgets = [gadgets[i] for i in sorted_indices]
colors = ['#4c72b0', '#55a868', '#c44e52', '#8172b3', '#ccb974', '#ffa07a']
sorted_colors = [colors[i] for i in sorted_indices]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), constrained_layout=True)

# Plot the sorted bar chart
for i, (color, gadget_data) in enumerate(zip(sorted_colors, sorted_data)):
    ax1.bar(years, gadget_data, label=sorted_gadgets[i], color=color, edgecolor='black')

# Set chart details for the sorted bar chart
ax1.set_title('Gadget Share Changes in Tech (Sorted by 2023)\n(2018-2023)', fontsize=14)
ax1.set_xlabel('Annual Period')
ax1.set_ylabel('Share Percentage (%)')
ax1.legend()

# Plot for smart devices and gaming growth rate remains unchanged
ax2.plot(years, smart_devices, marker='o', color='#1f77b4')
ax2.set_title('Overall Device Share & Growth in Gaming\n(2018-2023)', fontsize=14)
ax2.set_xlabel('Annual Period')
ax2.set_ylabel('Overall Share (%)', color='#1f77b4')
ax2.tick_params(axis='y', labelcolor='#1f77b4')

ax3 = ax2.twinx()
ax3.plot(years, gaming_growth_rate, marker='x', color='#ff7f0e', linestyle='--')
ax3.set_ylabel('Rate of Growth (%)', color='#ff7f0e')
ax3.tick_params(axis='y', labelcolor='#ff7f0e')

plt.show()