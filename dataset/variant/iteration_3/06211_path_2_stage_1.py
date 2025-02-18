import matplotlib.pyplot as plt
import numpy as np

# Number of pages
pages = np.array([120, 200, 320, 400, 150, 220, 300, 50, 180, 290])

# Reader satisfaction ratings (scale of 1-10)
ratings = np.array([7, 8, 9, 6, 7, 8, 9, 5, 7, 9])

# Average reading duration in hours
reading_duration = np.array([8, 12, 18, 22, 9, 13, 17, 5, 10, 15])

# Create subplots
fig, ax1 = plt.subplots(figsize=(12, 8))

# Scatter plot for number of pages vs satisfaction ratings
scatter = ax1.scatter(pages, ratings, color='darkblue', alpha=0.7, s=100, edgecolor='w')

# Adding trendline for number of pages vs satisfaction ratings
coef = np.polyfit(pages, ratings, 1)
poly1d_fn = np.poly1d(coef)
plt.plot(pages, poly1d_fn(pages), color='blue', linestyle='--', linewidth=1)

# Customize primary y-axis
ax1.tick_params(axis='y', labelcolor='darkblue')
ax1.set_xlim(0, 450)
ax1.set_ylim(4, 10)

# Create a secondary y-axis for average reading duration
ax2 = ax1.twinx()
ax2.plot(pages, reading_duration, color='darkgreen', marker='o', linestyle='-', linewidth=2)
ax2.tick_params(axis='y', labelcolor='darkgreen')
ax2.set_ylim(0, 25)

# Grid
ax1.grid(True, linestyle='--', alpha=0.5)

# Display the plot
plt.show()