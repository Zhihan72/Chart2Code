import numpy as np
import matplotlib.pyplot as plt

brightness_1 = np.array([5.1, 5.4, 5.7, 6.0, 6.3, 6.5, 7.0, 7.5, 8.0, 4.2, 4.5, 4.8, 3.1, 3.3,
                         3.9, 2.7, 2.5, 1.0, -1.5, 0.8, -1.0, -2.4, -2.3])
temperature_1 = np.array([3000, 3200, 3500, 3700, 4000, 4300, 5000, 5200, 6000, 7000, 8000,
                          9000, 12000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 
                          50000, 55000, 60000])
brightness_2 = np.array([9.0, 8.5, 8.3, 9.4, 10.0, 9.8, 10.5, 9.7, 10.2, 9.9, 8.7, 8.8])
temperature_2 = np.array([1000, 1200, 1500, 1800, 2100, 2400, 2700, 3000, 3300, 3600, 3900, 4200])

# Data Preparation - sorting the data
# Original data set sorted in ascending order
brightness_1_sorted_indices = np.argsort(brightness_1)
brightness_1_sorted = brightness_1[brightness_1_sorted_indices]
temperature_1_sorted = temperature_1[brightness_1_sorted_indices]

# Additional data set sorted in ascending order
brightness_2_sorted_indices = np.argsort(brightness_2)
brightness_2_sorted = brightness_2[brightness_2_sorted_indices]
temperature_2_sorted = temperature_2[brightness_2_sorted_indices]

# Plotting the sorted bar chart
fig, ax = plt.subplots(figsize=(12, 7))

# Bar chart with different colors for different groups
ax.bar(range(len(brightness_1_sorted)), brightness_1_sorted, color='royalblue', alpha=0.75, label='Group 1')
ax.bar(range(len(brightness_2_sorted)), brightness_2_sorted, color='darkorange', alpha=0.75, label='Group 2')

# Adding titles and labels
ax.set_title('Sorted Stellar Brightness Comparison', fontsize=16, fontweight='bold', wrap=True)
ax.set_xlabel('Stars in Sorted Order', fontsize=12)
ax.set_ylabel('Absolute Magnitude (Brightness)', fontsize=12)
ax.invert_yaxis()

# Adding legend
ax.legend()

# Adding grid lines
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Ensuring no overlapping of text or elements
plt.tight_layout()

# Display the plot
plt.show()