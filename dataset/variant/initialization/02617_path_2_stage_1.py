import matplotlib.pyplot as plt
import numpy as np

# Data setup for a single group (Wheat yield)
wheat_yield = [2.5, 3.0, 3.2, 2.8, 2.9, 3.5, 3.1, 2.7, 3.3, 2.4]
data = [wheat_yield]

# Create vertical box plot for a single group
fig, ax = plt.subplots(figsize=(7, 5))
boxprops = dict(linestyle='-', linewidth=2, color='darkblue')
medianprops = dict(linestyle='-', linewidth=2.5, color='firebrick')
meanprops = dict(marker='D', markeredgecolor='black', markerfacecolor='green')

# Boxplot customization
boxplot = ax.boxplot(
    data, 
    vert=True, 
    patch_artist=True,  # Ensure boxes are filled
    showmeans=True,
    boxprops=boxprops, 
    medianprops=medianprops, 
    meanprops=meanprops,
    whiskerprops=dict(linewidth=1.5), 
    capprops=dict(linewidth=1.5)
)

# Customize color for the box
for box in boxplot['boxes']:
    box.set_facecolor('#FF9999')

# Setting plot details
ax.set_xticklabels(['Wheat'], fontsize=12)
ax.set_title('Wheat Yield Distribution', fontsize=14, weight='bold', pad=20)
ax.set_ylabel('Yield (tonnes/ha)', fontsize=12)

# Adding gridlines
ax.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust layout for better readability
plt.tight_layout()

# Display the plot
plt.show()