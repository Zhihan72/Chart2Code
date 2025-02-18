import matplotlib.pyplot as plt
import numpy as np

# Backstory: The study of "Gourmet Ice Cream Taste Tests" across four seasons by a culinary magazine.
# The data represents scores given by a panel of judges rating various new ice cream flavors introduced in each season.

# Artificially constructed data for ice cream scores in different seasons
spring_scores = [8.2, 8.9, 9.1, 7.8, 8.7, 9.3, 7.5, 8.5, 8.8, 9.0, 8.3, 7.9]
summer_scores = [6.5, 6.8, 7.0, 6.4, 6.1, 7.2, 6.6, 6.9, 6.7, 7.1, 6.3, 6.0]
autumn_scores = [8.8, 8.1, 8.5, 8.4, 8.7, 9.0, 8.3, 8.6, 8.9, 9.1, 8.2, 8.0]
winter_scores = [7.0, 7.3, 7.5, 7.8, 6.9, 7.4, 7.1, 7.2, 7.6, 7.9, 7.7, 7.0]

# Combine data into a list for plotting
scores_data = [spring_scores, summer_scores, autumn_scores, winter_scores]

# Calculate the median of each season's scores for the scatter plot
median_values = [np.median(season) for season in scores_data]

# Labels for each season
season_labels = ['Spring', 'Summer', 'Autumn', 'Winter']

# Setup the figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Create the box plot
bplot = ax.boxplot(scores_data, vert=True, patch_artist=True, labels=season_labels, notch=True,
                   boxprops=dict(facecolor='lightpink', color='purple', linewidth=1.5),
                   whiskerprops=dict(color='purple', linewidth=1.5),
                   capprops=dict(color='purple', linewidth=1.5),
                   medianprops=dict(color='darkred', linewidth=2),
                   flierprops=dict(marker='o', markerfacecolor='red', markersize=6, linestyle='none', markeredgecolor='purple'))

# Overlay a scatter plot for median values
ax.scatter(range(1, 5), median_values, color='blue', s=100, zorder=3, label='Median Score')

# Adding the title and axis labels
ax.set_title('Gourmet Ice Cream Taste Tests Across Seasons', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Seasons', fontsize=12, labelpad=10)
ax.set_ylabel('Scores Given by Judges', fontsize=12, labelpad=10)

# Annotation for visual insight
ax.text(1, 9.5, 'Spring\nHighest Scores', fontsize=10, color='green', ha='center')
ax.text(2, 7.5, 'Summer\nLowest Scores', fontsize=10, color='darkred', ha='center')
ax.text(3, 9.5, 'Autumn\nExcellent Flavors', fontsize=10, color='goldenrod', ha='center')
ax.text(4, 8.3, 'Winter\nAverage Scores', fontsize=10, color='navy', ha='center')

# Add legend for the scatter plot
ax.legend(loc='upper right', fontsize=10)

# Enhance grid for better readability
ax.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.6)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()