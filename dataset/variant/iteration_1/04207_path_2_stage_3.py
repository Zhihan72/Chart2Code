import matplotlib.pyplot as plt
import numpy as np

# Data for the scatter plot
average_age_adulthood = np.array([18, 25, 14, 33, 120, 70])
average_years_education = np.array([12, 15, 6, 20, 80, 50])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Shuffle the colors by reordering the data indices
shuffled_indices = np.array([2, 4, 0, 5, 1, 3])
shuffled_colors = average_years_education[shuffled_indices]  # Use shuffled indices for colors

# Create a scatter plot with shuffled colors
scatter = ax.scatter(average_age_adulthood, average_years_education, 
                     c=shuffled_colors, cmap='plasma', s=200, 
                     edgecolors='black', alpha=0.8)

# Remove titles and labels
ax.set_title('')
ax.set_xlabel('')
ax.set_ylabel('')

# Remove colorbar label
cbar = fig.colorbar(scatter, ax=ax)
cbar.set_label('')

# Hide annotations
for i in range(len(average_age_adulthood)):
    ax.annotate('', (average_age_adulthood[i], average_years_education[i]))

# Keep the grid and ticks
ax.grid(True, linestyle='--', alpha=0.5)
ax.tick_params(axis='both', which='major', labelsize=12)
ax.set_xlim(10, 130)
ax.set_ylim(0, 90)

plt.tight_layout()
plt.show()