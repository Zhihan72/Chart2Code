import matplotlib.pyplot as plt
import numpy as np

# Data for the scatter plot
average_age_adulthood = np.array([18, 25, 14, 33, 120, 70])  # in years
average_years_education = np.array([12, 15, 6, 20, 80, 50])  # in years

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create a scatter plot
scatter = ax.scatter(average_age_adulthood, average_years_education, 
                     c=average_years_education, cmap='plasma', s=200, 
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