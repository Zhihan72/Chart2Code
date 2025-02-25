import matplotlib.pyplot as plt
import numpy as np

# Data preparation with additional made-up data series
regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']
cuisine1_popularity = [80, 70, 90, 80, 70]  # Original cuisine example
cuisine2_popularity = [65, 75, 85, 75, 65]  # Additional cuisine example
cuisine3_popularity = [70, 60, 95, 85, 80]  # Another additional cuisine

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot vertical bar charts for multiple cuisines
bar_width = 0.25
x_labels = np.arange(len(regions))

# Plotting each cuisine with an offset
ax.bar(x_labels - bar_width, cuisine1_popularity, width=bar_width, color='darkblue', edgecolor='black', alpha=0.6, label='Cuisine 1', linestyle='-.')
ax.bar(x_labels, cuisine2_popularity, width=bar_width, color='forestgreen', edgecolor='black', alpha=0.6, label='Cuisine 2', linestyle='-.')
ax.bar(x_labels + bar_width, cuisine3_popularity, width=bar_width, color='indianred', edgecolor='black', alpha=0.6, label='Cuisine 3', linestyle='-.')

# Customizing y-axis grid and ticks
ax.grid(axis='y', linestyle='-.', alpha=0.4)
ax.yaxis.set_ticks(np.arange(0, 101, 20))

# Add labels, legend, and title
ax.set_xlabel('Regions')
ax.set_ylabel('Popularity Scores')
ax.set_title('Cuisine Popularity by Region')
ax.set_xticks(x_labels)
ax.set_xticklabels(regions)
ax.legend()

# Automatically adjust layout to prevent text cutoff
plt.tight_layout()

# Show the plot
plt.show()