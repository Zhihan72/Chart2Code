import matplotlib.pyplot as plt
import numpy as np

# Data for Alien Plant Growth (Heights in cm, Diameters in cm)
years = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

xenia_height = np.array([8, 12, 20, 25, 30, 37, 40, 48, 55, 60])
xenia_diameter = np.array([2, 3, 5, 7, 9, 12, 13, 16, 19, 21])

trogar_height = np.array([5, 9, 13, 17, 21, 25, 29, 32, 35, 39])
trogar_diameter = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Initialize the plot with the desired subplot configuration
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 16))

# Scatter plot
ax1.scatter(xenia_height, xenia_diameter, color='red', edgecolor='black', alpha=0.7, s=100, label='Xenia')
ax1.scatter(trogar_height, trogar_diameter, color='green', edgecolor='black', alpha=0.7, s=100, label='Trogar')

# Titles and labels for the first plot
ax1.set_title('Alien Plant Growth', fontsize=14, fontweight='bold')
ax1.set_xlabel('Height (cm)', fontsize=12)
ax1.set_ylabel('Diameter (cm)', fontsize=12)
ax1.legend(title='Types', fontsize=10)
ax1.grid(linestyle='--', alpha=0.7)

# Add annotations for some data points
for i in range(0, len(years), 2):
    ax1.annotate(f'Yr {years[i]}', (xenia_height[i], xenia_diameter[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
    ax1.annotate(f'Yr {years[i]}', (trogar_height[i], trogar_diameter[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

# Bar plot: Comparison of average height and diameter for Xenia and Trogar
average_heights = [np.mean(xenia_height), np.mean(trogar_height)]
average_diameters = [np.mean(xenia_diameter), np.mean(trogar_diameter)]

bar_width = 0.35
index = np.arange(len(average_heights))

ax2.bar(index, average_heights, bar_width, label='Height (cm)', color='r', alpha=0.7)
ax2.bar(index + bar_width, average_diameters, bar_width, label='Diameter (cm)', color='b', alpha=0.7)

# Titles and labels for the second plot
ax2.set_title('Average Size', fontsize=14, fontweight='bold')
ax2.set_xlabel('Types', fontsize=12)
ax2.set_ylabel('Size (cm)', fontsize=12)
ax2.set_xticks(index + bar_width / 2)
ax2.set_xticklabels(['Xenia', 'Trogar'])
ax2.legend()

plt.tight_layout()
plt.show()