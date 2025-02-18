import matplotlib.pyplot as plt
import numpy as np

# Define yield data in kilograms for a single group, combining all vegetables
combined_yield = [45, 50, 55, 47, 52, 60, 58, 54, 49, 53, 
                  30, 28, 32, 25, 31, 29, 27, 30, 28, 35,
                  40, 42, 45, 38, 47, 44, 39, 41, 43, 40,
                  20, 22, 19, 23, 21, 18, 24, 22, 20, 25]

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(8, 10))

# Create a vertical box plot for the combined data
box = ax.boxplot(combined_yield, vert=True, patch_artist=True,
                 flierprops=dict(marker='o', color='red', alpha=0.5),
                 boxprops=dict(color='darkblue', linewidth=1.5),
                 whiskerprops=dict(color='blue', linestyle='--'),
                 capprops=dict(color='blue'),
                 medianprops=dict(color='orange', linewidth=2),
                 notch=True)

# Set color for the single box
colors = ['skyblue']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add grid for better readability
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Add titles and axis labels
ax.set_title("Combined Yield Distribution of All Vegetables", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Vegetable Yield Type", fontsize=14)
ax.set_ylabel("Yield (kg)", fontsize=14)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()