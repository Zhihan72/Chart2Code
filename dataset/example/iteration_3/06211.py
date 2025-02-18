import matplotlib.pyplot as plt
import numpy as np

# Backstory and Data:
# The chart visualizes the correlation between the number of pages in a book and the satisfaction rating given by readers. 
# Additionally, a secondary y-axis shows the average reading duration for each book. The data is derived from a survey of readers in a book club.

# Number of pages
pages = np.array([120, 200, 320, 400, 150, 220, 300, 50, 180, 290])

# Reader satisfaction ratings (scale of 1-10)
ratings = np.array([7, 8, 9, 6, 7, 8, 9, 5, 7, 9])

# Average reading duration in hours
reading_duration = np.array([8, 12, 18, 22, 9, 13, 17, 5, 10, 15])

# Create subplots
fig, ax1 = plt.subplots(figsize=(12, 8))

# Scatter plot for number of pages vs satisfaction ratings
scatter = ax1.scatter(pages, ratings, color='darkblue', label='Satisfaction Rating', alpha=0.7, s=100, edgecolor='w')

# Adding trendline for number of pages vs satisfaction ratings
coef = np.polyfit(pages, ratings, 1)
poly1d_fn = np.poly1d(coef)
plt.plot(pages, poly1d_fn(pages), color='blue', linestyle='--', linewidth=1, label='Rating Trendline')

# Customize primary y-axis and labels
ax1.set_xlabel('Number of Pages in Book', fontsize=12)
ax1.set_ylabel('Satisfaction Rating (1-10)', color='darkblue', fontsize=12)
ax1.tick_params(axis='y', labelcolor='darkblue')
ax1.set_xlim(0, 450)
ax1.set_ylim(4, 10)

# Create a secondary y-axis for average reading duration
ax2 = ax1.twinx()
ax2.plot(pages, reading_duration, color='darkgreen', marker='o', linestyle='-', linewidth=2, label='Reading Duration')
ax2.set_ylabel('Average Reading Duration (hours)', color='darkgreen', fontsize=12)
ax2.tick_params(axis='y', labelcolor='darkgreen')
ax2.set_ylim(0, 25)

# Title and Grid
plt.title('Correlation between Book Length, Reader Satisfaction, and Reading Duration',
          fontsize=14, fontweight='bold', pad=20)
ax1.grid(True, linestyle='--', alpha=0.5)

# Legends
fig.tight_layout()
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='best')

# Display the plot
plt.show()