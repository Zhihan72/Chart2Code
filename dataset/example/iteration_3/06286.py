import matplotlib.pyplot as plt
import numpy as np

# Backstory: A research team is studying the relationship between the number of hours spent on physical activities per week
# and the corresponding happiness scores from a survey. They want to analyze if there's a trend or correlation.

# Data: Hours spent on physical activities per week and corresponding happiness scores (out of 100)
activity_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
happiness_scores = np.array([45, 50, 55, 60, 68, 72, 78, 80, 85, 90])

# Let's also compare it with another activity; for example, hours spent on watching TV and corresponding happiness scores
tv_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
tv_happiness_scores = np.array([30, 32, 34, 33, 32, 30, 28, 27, 25, 24])

# Create the figure and axes
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the scatter plot for physical activities
ax.scatter(activity_hours, happiness_scores, color='darkblue', label='Physical Activities', s=100, alpha=0.7)

# Plot the scatter plot for watching TV
ax.scatter(tv_hours, tv_happiness_scores, color='darkred', label='Watching TV', s=100, alpha=0.7)

# Adding titles and labels
ax.set_title('Impact of Physical Activities vs. Watching TV on Happiness\n per Week', fontsize=16, fontweight='bold')
ax.set_xlabel('Hours Per Week', fontsize=14)
ax.set_ylabel('Happiness Score (out of 100)', fontsize=14)

# Adding a legend
ax.legend(title='Activity Type', fontsize=12, loc='upper left')

# Adding grid
ax.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout for better appearance
plt.tight_layout()

# Show the plot
plt.show()