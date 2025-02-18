import matplotlib.pyplot as plt
import numpy as np

# Data
activity_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
happiness_scores = np.array([45, 50, 55, 60, 68, 72, 78, 80, 85, 90])
tv_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
tv_happiness_scores = np.array([30, 32, 34, 33, 32, 30, 28, 27, 25, 24])

# Create the figure and axes
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the scatter plots with the same color
common_color = 'darkgreen'
ax.scatter(activity_hours, happiness_scores, color=common_color, label='Workouts', s=100, alpha=0.7)
ax.scatter(tv_hours, tv_happiness_scores, color=common_color, label='Binge Watching', s=100, alpha=0.7)

# Adding titles and labels
ax.set_title('The Link Between Exercise and TV Viewing\n on Joyfulness Weekly', fontsize=16, fontweight='bold')
ax.set_xlabel('Weekly Hours', fontsize=14)
ax.set_ylabel('Joy Index (max 100)', fontsize=14)

# Adding a legend
ax.legend(title='Type of Activity', fontsize=12, loc='upper left')

# Adding grid
ax.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout for better appearance
plt.tight_layout()

# Show the plot
plt.show()