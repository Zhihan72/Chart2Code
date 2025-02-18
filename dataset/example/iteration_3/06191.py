import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the categories of architectural styles and their scores for each city
categories = ['Historical Buildings', 'Modern Skyscrapers', 'Parks and Open Spaces', 'Public Transportation', 'Cultural Venues']
city_scores = {
    'New York': [9, 10, 8, 9, 7],
    'Paris': [10, 7, 8, 8, 9],
    'Tokyo': [8, 9, 7, 10, 7],
    'London': [9, 8, 9, 8, 10],
    'Dubai': [6, 10, 7, 8, 5]
}

# Industry average scores for comparison
global_averages = [8, 9, 8, 9, 8]

num_vars = len(categories)
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Styling colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Initialize subplot layout
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Function to plot radar chart for each city
def add_city_radar(city_name, color):
    scores = city_scores[city_name]
    scores += scores[:1]
    ax.plot(angles, scores, linewidth=2, linestyle='solid', label=city_name, color=color)
    ax.fill(angles, scores, color=color, alpha=0.25)

# Plotting radars for cities
for city, color in zip(city_scores.keys(), colors):
    add_city_radar(city, color)

# Add category labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, weight='bold')

# Set radial axis limits
ax.set_ylim(0, 10)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=10)

# Add title
plt.title('Cityscape Attributes Across Global Metropolises', size=15, weight='bold', ha='center', va='top', position=(0.5, 1.1))

# Plot the global average
global_averages += global_averages[:1]
ax.plot(angles, global_averages, linewidth=2, linestyle='dashed', color='grey', label='Global Average')

# Add legend
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.2), fontsize=10, title='Cities')

# Automatically adjust layout to prevent text overlapping
plt.tight_layout()

# Show plot
plt.show()