import matplotlib.pyplot as plt
import numpy as np

# Data: Monarch Butterfly populations observed at different points in North America
years = np.arange(2010, 2021)
populations = {
    'Canada': [300, 320, 280, 290, 310, 340, 365, 350, 330, 320, 310],
    'USA': [1000, 1050, 990, 975, 1120, 1150, 1100, 1080, 1075, 1050, 1020],
    'Mexico': [250, 270, 240, 245, 260, 290, 300, 290, 285, 280, 270]
}

# Setup the plot
plt.figure(figsize=(14, 8))

# Colors for each region line
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Plot data with annotations for each region
for (region, pops), color in zip(populations.items(), colors):
    plt.plot(years, pops, '-o', color=color, linewidth=2, markersize=6, alpha=0.8)
    
    # Annotate for key data points for each region
    midpoint_index = len(years) // 2
    key_points = [(years[0], pops[0]), (years[midpoint_index], pops[midpoint_index]), (years[-1], pops[-1])]
    for (year, pop) in key_points:
        plt.annotate(f'{pop}k', xy=(year, pop), xytext=(5, -15 if pop < max(pops) else 5), 
                     textcoords='offset points', arrowprops=dict(arrowstyle='->', color=color), 
                     fontsize=10, color=color, ha='center')

# Set titles and labels
plt.title('Migration Patterns of Monarch Butterflies (2010-2020)\nObserved Populations in North America', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Observed Populations (in thousands)', fontsize=12)

# Ensure tight layout for readability
plt.tight_layout()

# Show the plot
plt.show()