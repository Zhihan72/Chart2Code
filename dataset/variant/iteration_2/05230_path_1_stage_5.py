import matplotlib.pyplot as plt
import numpy as np

# Data for popularity (percentage)
languages = ['Python', 'JavaScript', 'Java', 'C++']
popularity = [30, 25, 20, 15]

# Sorting languages by popularity in descending order
languages_sorted, popularity_sorted = zip(*sorted(zip(popularity, languages), reverse=True))

# Choose a single color
single_color = '#3776AB'

# Create the figure and axis objects
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the sorted bar chart for popularity
ax1.barh(languages_sorted, popularity_sorted, color=single_color, height=0.6)

# Add a secondary y-axis for the line plot
ax2 = ax1.twinx()

# Set axis limits to improve visualization
ax1.set_xlim(0, 35)
ax2.set_ylim(2022, 2028)

# Automatically adjust layout
plt.tight_layout()

# Show plot
plt.show()