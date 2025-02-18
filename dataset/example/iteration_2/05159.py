import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking the Rise of Different Genres in Podcasts Over a Decade
# Data represents the number of new podcasts released in various genres from 2011 to 2020.

# Define the years and genres
years = np.arange(2011, 2021)
genres = ['True Crime', 'Business', 'Technology', 'Health', 'Sports', 'Comedy']

# Artificial data: Number of new podcasts released each year for each genre
true_crime = [5, 10, 15, 25, 35, 50, 60, 70, 85, 100]
business = [8, 12, 18, 22, 27, 35, 45, 55, 68, 80]
technology = [10, 15, 25, 30, 40, 52, 60, 75, 83, 95]
health = [6, 9, 14, 18, 27, 35, 40, 50, 65, 72]
sports = [4, 8, 12, 20, 28, 35, 42, 50, 60, 68]
comedy = [9, 14, 20, 26, 34, 40, 52, 60, 75, 88]

# Stack the data for different genres
stacked_data = np.array([true_crime, business, technology, health, sports, comedy])

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Define the width of the bars
bar_width = 0.6

# Colors for each genre
colors = ['#FF6347', '#4682B4', '#9ACD32', '#FFD700', '#EE82EE', '#00CED1']

# Plotting stacked bars
bottom = np.zeros(len(years))
for i, genre in enumerate(genres):
    ax.bar(years, stacked_data[i], bar_width, bottom=bottom, color=colors[i], edgecolor='black', label=genre)
    bottom += stacked_data[i]

# Add annotations for significant points
for i, (year, new_podcasts) in enumerate(zip(years, bottom)):
    if i % 2 == 0:  # To reduce clutter, only label every second year
        ax.text(year, new_podcasts + 5, f'{new_podcasts}', ha='center', va='bottom', fontsize=10)

# Title and labels
ax.set_title('Rise of Podcast Genres Over the Decade\n(2011-2020)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of New Podcasts', fontsize=14)

# Setting xticks
ax.set_xticks(years)

# Adding grid for clarity
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Adding legend
ax.legend(title='Podcast Genres', fontsize=12, title_fontsize=14, loc='upper left')

# Ensure the layout is properly adjusted, avoid overlap of elements
plt.tight_layout()

# Show the plot
plt.show()