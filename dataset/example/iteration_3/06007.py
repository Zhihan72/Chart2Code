import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking the popularity of various fictional TV series genres over the years on a streaming platform.
# The genres tracked are Drama, Comedy, Sci-Fi, Horror, and Fantasy.

# Defining years and viewership data for each genre (in millions)
years = np.arange(2015, 2026)

drama_viewership = np.array([30, 35, 40, 50, 55, 60, 70, 75, 80, 85, 90])
comedy_viewership = np.array([20, 25, 30, 35, 40, 46, 50, 55, 60, 65, 70])
scifi_viewership = np.array([15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65])
horror_viewership = np.array([10, 12, 14, 18, 22, 26, 30, 35, 40, 45, 50])
fantasy_viewership = np.array([18, 22, 25, 27, 30, 33, 35, 40, 45, 50, 55])

# Create the figure and axis objects
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each genre's viewership data
ax.plot(years, drama_viewership, '-o', label='Drama', color='blue', linewidth=2, markersize=6)
ax.plot(years, comedy_viewership, '-s', label='Comedy', color='orange', linewidth=2, markersize=6)
ax.plot(years, scifi_viewership, '-^', label='Sci-Fi', color='green', linewidth=2, markersize=6)
ax.plot(years, horror_viewership, '-d', label='Horror', color='red', linewidth=2, markersize=6)
ax.plot(years, fantasy_viewership, '-p', label='Fantasy', color='purple', linewidth=2, markersize=6)

# Adding titles, labels, and grid
ax.set_title("Streaming Trends Over the Years\nPopularity of Various TV Series Genres (in Millions)", fontsize=16, pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Viewership (in Millions)", fontsize=12)

# Formatting the x-axis and y-axis ticks
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, fontsize=10)
ax.yaxis.set_tick_params(labelsize=10)

# Adding legend
ax.legend(title='Genres', fontsize=10, loc='upper left', ncol=1, fancybox=True, shadow=True)

# Highlighting significant points
ax.annotate('Peak in Drama',
            xy=(2025, 90), xytext=(2020, 60),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, ha='center')
ax.annotate('Rise in Sci-Fi Popularity',
            xy=(2025, 65), xytext=(2018, 15),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, ha='center')

# Grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Adjusting layout
plt.tight_layout()

# Display the plot
plt.show()