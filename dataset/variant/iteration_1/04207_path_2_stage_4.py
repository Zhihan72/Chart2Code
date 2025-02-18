import matplotlib.pyplot as plt
import numpy as np

# Data for the scatter plot
average_age_adulthood = np.array([18, 25, 14, 33, 120, 70])
average_years_education = np.array([12, 15, 6, 20, 80, 50])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Shuffle the colors by reordering the data indices
shuffled_indices = np.array([2, 4, 0, 5, 1, 3])
shuffled_colors = average_years_education[shuffled_indices]

# Create a scatter plot with shuffled colors
ax.scatter(average_age_adulthood, average_years_education, 
           c=shuffled_colors, cmap='plasma', s=200, 
           edgecolors='black', alpha=0.8)

# Remove grid
ax.grid(False)

# Remove border
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Remove colorbar
# Removed the colorbar creation code

# Adjust x and y limits without ticks
ax.set_xlim(10, 130)
ax.set_ylim(0, 90)
ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

plt.tight_layout()
plt.show()