import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch  # Import Patch from matplotlib.patches

# Backstory: We're analyzing the water quality in different city reservoirs over the past month. Each city's reservoir is tested daily for pollutants and assigned a quality score (0-100).

# Data for water quality scores
water_quality_data = {
    'City A': [75, 80, 85, 77, 82, 79, 81, 83, 85, 84, 81, 78, 80, 79, 83, 86, 88, 89, 90, 76, 78, 79, 81, 83, 84, 80, 82, 83, 85, 87],
    'City B': [65, 68, 70, 72, 74, 69, 71, 75, 77, 79, 80, 81, 75, 74, 73, 78, 76, 77, 80, 82, 81, 79, 78, 76, 75, 74, 77, 78, 79, 80],
    'City C': [90, 92, 93, 94, 89, 87, 88, 86, 85, 84, 83, 90, 89, 88, 87, 86, 85, 84, 83, 90, 89, 88, 87, 86, 85, 83, 81, 82, 80, 79],
    'City D': [55, 58, 60, 62, 64, 59, 61, 63, 65, 67, 66, 68, 63, 62, 61, 64, 63, 65, 66, 68, 67, 69, 70, 65, 61, 62, 63, 64, 65, 66],
    'City E': [82, 84, 85, 86, 89, 87, 88, 86, 85, 87, 90, 92, 89, 88, 86, 84, 83, 85, 87, 89, 90, 88, 87, 86, 85, 84, 83, 82, 80, 81]
}

# Prepare data and labels for plotting
city_names = list(water_quality_data.keys())
quality_values = list(water_quality_data.values())

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot a vertical box plot
boxplot = ax.boxplot(quality_values, vert=True, patch_artist=True, notch=True, labels=city_names)

# Customize the appearance of the box plots
colors = ['#77dd77', '#ff6961', '#779ecb', '#fdfd96', '#ffb347']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.5)

# Style other elements of the box plot
plt.setp(boxplot['whiskers'], color='gray', linestyle='--')
plt.setp(boxplot['caps'], color='gray')
plt.setp(boxplot['medians'], color='black')

# Set title and labels
ax.set_title("Comparative Analysis of Water Quality in City Reservoirs Over a Month", fontsize=16, fontweight='bold')
ax.set_ylabel("Water Quality Score (0-100)", fontsize=14)
ax.set_xlabel("Cities", fontsize=14)

# Enable grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Create annotations for notable observations
ax.annotate('Highest Recorded Quality', xy=(3, 94), xytext=(2.5, 96),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=12, fontweight='bold', color='black')

# Add legend for color-coded boxes
legend_elements = [Patch(facecolor=color, label=city) for color, city in zip(colors, city_names)]
ax.legend(handles=legend_elements, title='Cities', loc='upper right')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()