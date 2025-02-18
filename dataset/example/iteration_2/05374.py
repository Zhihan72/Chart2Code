import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# In a small town, local artisans are known for creating handcrafted candles. Each artisan has a unique style and preference for different types of wax. 
# This box plot showcases the distribution of candle weights from five different types of wax used by these artisans.

# Types of wax
wax_types = ['Soy Wax', 'Beeswax', 'Paraffin Wax', 'Palm Wax', 'Gel Wax']

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

# Add chart title and labels
ax.set_title('Distribution of Candle Weights by Type of Wax Used\nAmong Local Artisans', fontsize=16, pad=20)
ax.set_xlabel('Weight (grams)', fontsize=12)
ax.set_ylabel('Types of Wax', fontsize=12)
ax.set_yticklabels(wax_types, fontsize=12)

# Customize grid for better readability
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Add a legend to explain notched boxes
plt.figtext(0.15, 0.85, "Notched boxes indicate 95% CI around the median.", fontsize=10)

# Use tight_layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()