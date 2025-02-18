import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# We are analyzing the growth rates of various plant species over the course of a growing season in a botanical garden.
# The garden's research team has recorded the weekly growth rates (in cm) for five different plant species.

# Plant species
species = ['Rose', 'Sunflower', 'Tulip', 'Daisy', 'Lavender']

# Weekly growth rates (in cm)
# Data structured as lists of weekly growth rates for each species
growth_rates = [
    [2.5, 2.7, 2.8, 3.0, 2.6, 3.1, 2.9, 2.8, 3.0, 2.7, 2.5, 3.0, 2.6, 2.8, 3.1],  # Rose
    [3.5, 3.6, 3.7, 3.8, 4.0, 3.9, 4.1, 3.8, 3.7, 3.9, 4.0, 3.8, 3.6, 3.9, 4.1],  # Sunflower
    [1.5, 1.6, 1.7, 1.6, 1.8, 1.7, 1.9, 1.8, 1.6, 1.7, 1.8, 1.9, 1.7, 1.8, 1.9],  # Tulip
    [2.0, 2.1, 2.3, 2.2, 2.4, 2.3, 2.2, 2.5, 2.4, 2.3, 2.5, 2.6, 2.4, 2.5, 2.6],  # Daisy
    [1.2, 1.3, 1.2, 1.4, 1.3, 1.5, 1.3, 1.4, 1.3, 1.5, 1.4, 1.6, 1.5, 1.4, 1.6]   # Lavender
]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create a box plot
box = ax.boxplot(growth_rates, patch_artist=True, notch=True, vert=True, showmeans=True)

# Set colors for each box
colors = ['#ff9999', '#ffcc99', '#99ff99', '#66b3ff', '#c2c2f0']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customize the plot
ax.set_title('Weekly Growth Rates of Various Plant Species in a Botanical Garden', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Plant Species', fontsize=14)
ax.set_ylabel('Weekly Growth Rate (cm)', fontsize=14)
ax.set_xticks(np.arange(1, len(species) + 1))
ax.set_xticklabels(species, rotation=45, ha='right')

# Customize medians and means
for median, mean in zip(box['medians'], box['means']):
    median.set_color('black')
    median.set_linewidth(2)
    mean.set_markerfacecolor('red')
    mean.set_markeredgecolor('red')

# Create a custom legend
median_legend = plt.Line2D([0], [0], color='black', lw=2, label='Median')
mean_legend = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=8, label='Mean')
ax.legend(handles=[median_legend, mean_legend], loc='upper right')

# Add a grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Highlight a notable observation
ax.annotate('Fastest Growth Rate', xy=(2, 4.1), xytext=(1.5, 4.3),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=12, fontweight='bold', color='black')

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()