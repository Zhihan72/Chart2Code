import matplotlib.pyplot as plt
import numpy as np

# Data preparation
regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']
popularity_scores = [80, 70, 90, 80, 70]  # Example data for one cuisine

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot a simple vertical bar chart for one type of cuisine
ax.bar(regions, popularity_scores, color='#FF4500', edgecolor='grey', alpha=0.8)

# Titles and labels
ax.set_title("Cuisine Popularity Across Regions in 2023", fontsize=14, fontweight='bold', pad=10)
ax.set_xlabel("Regions", fontsize=12)
ax.set_ylabel("Popularity Score", fontsize=12)

# Customizing y-axis grid and ticks
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.yaxis.set_ticks(np.arange(0, 101, 10))

# Automatically adjust layout to prevent text cutoff
plt.tight_layout()

# Show the plot
plt.show()