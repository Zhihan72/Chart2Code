import matplotlib.pyplot as plt
import numpy as np

# Types of wax - shuffled labels
wax_types = ['Palm Wax', 'Gel Wax', 'Paraffin Wax', 'Soy Wax', 'Beeswax']

# Artificial data representing candle weights (in grams) for each wax type
soy_wax_weights = [150, 155, 160, 162, 170, 175, 180, 165, 172, 160]
beeswax_weights = [140, 145, 148, 150, 155, 150, 158, 155, 160, 148]
paraffin_weights = [130, 135, 138, 140, 145, 148, 150, 144, 142, 135]
palm_wax_weights = [160, 165, 170, 168, 175, 180, 185, 178, 170, 165]
gel_wax_weights = [120, 125, 130, 128, 135, 132, 138, 130, 132, 128]

# Combine all data into a list
data = [soy_wax_weights, beeswax_weights, paraffin_weights, palm_wax_weights, gel_wax_weights]

# Define custom colors for each box
colors = ['#FFD700', '#FF6347', '#8A2BE2', '#FF4500', '#20B2AA']

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot box plots with custom properties
bp = ax.boxplot(data, vert=False, patch_artist=True, notch=True,
                boxprops=dict(linewidth=1.5),
                whiskerprops=dict(linewidth=1.5),
                capprops=dict(linewidth=1.5),
                medianprops=dict(color='black', linewidth=2),
                flierprops=dict(marker='o', color='black', alpha=0.5))

# Set individual box colors
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Alter chart title and labels
ax.set_title('Variety in Artisan Candle Weights across Wax Types', fontsize=16, pad=20)
ax.set_xlabel('Mass (g)', fontsize=12)
ax.set_ylabel('Wax Categories', fontsize=12)
ax.set_yticklabels(wax_types, fontsize=12)

# Customize grid for better readability
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Add a legend to explain notched boxes
plt.figtext(0.15, 0.85, "95% confidence interval for median displayed.", fontsize=10)

# Use tight_layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()