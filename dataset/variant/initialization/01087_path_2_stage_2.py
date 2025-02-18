import matplotlib.pyplot as plt
import numpy as np

# Years from 2005 to 2025
years = np.arange(2005, 2026)

# Percentage adoption data for each technology
e_learning_platforms = np.array([
    10, 12, 15, 18, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 78, 80, 82, 84, 86
])
virtual_classrooms = np.array([
    -5, -6, -8, -10, -12, -15, -18, -20, -25, -28, -32, -35, -38, -40, -42, -45, -50, -52, -54, -55, -57
])
educational_apps = np.array([
    2, 3, 5, 7, 9, 11, 15, 18, 22, 27, 30, 35, 40, 43, 47, 50, 53, 55, 58, 60, 63
])

# Create the figure and axes
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each diverging stacked bar
ax.bar(years, e_learning_platforms, label='E-Learning Platforms', color='#ff9999', alpha=0.8)
ax.bar(years, educational_apps, bottom=e_learning_platforms, label='Educational Apps', color='#ffcc99', alpha=0.8)
ax.bar(years, virtual_classrooms, label='Virtual Classrooms', color='#66b3ff', alpha=0.8)

# Title and labels
ax.set_title('Diverging Adoption of Digital Education Tools (2005-2025)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Percentage Adoption (%)', fontsize=14)

# X and Y axis configuration
ax.set_xticks(years[::2])
ax.set_xticklabels(years[::2], rotation=45)

# Add grid lines and legend
ax.grid(alpha=0.3, linestyle='--')
ax.legend(loc='upper left', fontsize=12, title='Digital Tools')

# Horizontal line at zero
ax.axhline(0, color='black', linewidth=0.8)

# Use tight layout to prevent overlapping
plt.tight_layout()

# Show plot
plt.show()