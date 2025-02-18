import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# An analysis based on temperatures recorded in different wells in an oil field 
# over the course of 12 months has been performed. The objective is to compare 
# the temperature distributions and identify any anomalies or patterns that might 
# influence drilling decisions.

# Data representing monthly temperatures (in °C) at five different wells
well_temps = [
    [35, 36, 38, 40, 42, 45, 43, 41, 44, 37, 36, 35],  # Well A
    [50, 52, 54, 56, 55, 57, 58, 54, 53, 51, 52, 50],  # Well B
    [28, 30, 29, 31, 33, 35, 34, 32, 31, 30, 29, 28],  # Well C
    [45, 46, 47, 48, 49, 50, 49, 48, 47, 46, 45, 44],  # Well D
    [39, 38, 37, 36, 35, 34, 36, 38, 40, 39, 38, 37]   # Well E
]

# Well labels
wells = ['Well A', 'Well B', 'Well C', 'Well D', 'Well E']

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

# Adding annotations for means
for i, temps in enumerate(well_temps):
    mean = np.mean(temps)
    ax.annotate(f'Mean: {mean:.1f}°C', xy=(i+1, mean), xytext=(i+1.2, mean + 1),
                textcoords='data', arrowprops=dict(facecolor='black', arrowstyle='->'),
                fontsize=10, ha='center', va='bottom', color='darkred')

# Customize the plot with titles and labels
ax.set_title("Distribution of Monthly Temperatures in Different Oil Wells\nOver 12 Months Observation Period", 
             fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel("Temperature (°C)", fontsize=12, labelpad=10)
ax.set_xticklabels(wells, fontsize=12)

# Enhance readability with grid lines
ax.grid(True, linestyle='--', alpha=0.6)

# Adding a subtle background
ax.set_facecolor('#f9f9f9')

# Add a legend that corresponds to the color coding for each well
for i, color in enumerate(colors):
    ax.scatter([], [], color=color, label=wells[i])
ax.legend(loc='upper left', fontsize=10, frameon=True, framealpha=1, edgecolor='black')

# Automatically adjust layout for optimal display
plt.tight_layout()

# Show the plot
plt.show()