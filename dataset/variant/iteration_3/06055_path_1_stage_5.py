import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

wheat = np.array([60, 62, 65, 70, 75, 78, 80, 82, 85, 90, 95])
rice = np.array([40, 42, 43, 45, 47, 50, 53, 55, 58, 60, 62])
maize = np.array([30, 32, 34, 36, 39, 42, 45, 48, 52, 56, 60])
soy = np.array([20, 22, 23, 25, 27, 30, 32, 35, 37, 40, 45])

crops_data = [wheat, rice, maize, soy]
crop_labels = ['Wheat', 'Rice', 'Maize', 'Soy']
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']  # Colors shuffled
markers = ['o', 'v', '^', '<']  # New marker styles

bar_width = 0.2
x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(12, 8))
for i, (data, color, label, marker) in enumerate(zip(crops_data, colors, crop_labels, markers)):
    ax.bar(x + i * bar_width, data, width=bar_width, color=color, label=label, edgecolor='black', hatch=marker)

# Updated the x-tick positions and labels
ax.set_xticks(x + bar_width * (len(crops_data) - 1) / 2)
ax.set_xticklabels(years, rotation=45)

# Modifying the legend; placing it outside the plot area
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))  

# Changing grid style
ax.grid(visible=False)  # Removed grid

# Update borders to have a thicker line
ax.spines['top'].set_linestyle('--')
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linestyle('--')

plt.tight_layout()
plt.show()