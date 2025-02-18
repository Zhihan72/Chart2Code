import matplotlib.pyplot as plt
import numpy as np

# Data representing monthly temperatures (in °C) at five different wells
well_temps = [
    [35, 36, 38, 40, 42, 45, 43, 41, 44, 37, 36, 35],  # Well A
    [50, 52, 54, 56, 55, 57, 58, 54, 53, 51, 52, 50],  # Well B
    [28, 30, 29, 31, 33, 35, 34, 32, 31, 30, 29, 28],  # Well C
    [45, 46, 47, 48, 49, 50, 49, 48, 47, 46, 45, 44],  # Well D
    [39, 38, 37, 36, 35, 34, 36, 38, 40, 39, 38, 37]   # Well E
]

# Creating the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create a vertical boxplot with the given data
bp = ax.boxplot(well_temps, patch_artist=True, notch=False, vert=True,
                boxprops=dict(color='black', linewidth=1.5),
                medianprops=dict(color='red', linewidth=2),
                whiskerprops=dict(color='black'),
                capprops=dict(color='black'),
                flierprops=dict(marker='o', color='blue', alpha=0.5))

# Setting colors for each well's boxplot
colors = ['#ADD8E6', '#90EE90', '#FFC0CB', '#FA8072', '#87CEFA']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Remove text labels and titles
ax.set_xticklabels([])

# Enhance readability with grid lines
ax.grid(True, linestyle='--', alpha=0.6)

# Adding a subtle background
ax.set_facecolor('#f9f9f9')

# Remove legend since there are no labels
# plt.legend() call is removed

# Automatically adjust layout for optimal display
plt.tight_layout()

# Show the plot
plt.show()