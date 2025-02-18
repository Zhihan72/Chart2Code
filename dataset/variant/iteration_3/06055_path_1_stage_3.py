import matplotlib.pyplot as plt
import numpy as np

# Define years for the x-axis
years = np.arange(2010, 2021)

# Define yield data for each crop
wheat = np.array([60, 62, 65, 70, 75, 78, 80, 82, 85, 90, 95])
rice = np.array([40, 42, 43, 45, 47, 50, 53, 55, 58, 60, 62])
maize = np.array([30, 32, 34, 36, 39, 42, 45, 48, 52, 56, 60])
soy = np.array([20, 22, 23, 25, 27, 30, 32, 35, 37, 40, 45])

# Prepare a list of crops for iteration
crops_data = [wheat, rice, maize, soy]
crop_labels = ['Wheat', 'Rice', 'Maize', 'Soy']
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Bar chart settings
bar_width = 0.2
x = np.arange(len(years))  # The label locations

# Plotting the grouped bar chart
fig, ax = plt.subplots(figsize=(12, 8))
for i, (data, color, label) in enumerate(zip(crops_data, colors, crop_labels)):
    ax.bar(x + i * bar_width, data, width=bar_width, color=color, label=label)

# Modify the x-axis ticks and labels
ax.set_xticks(x + bar_width * (len(crops_data) - 1) / 2)
ax.set_xticklabels(years, rotation=45)

# Add legend
ax.legend()

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()