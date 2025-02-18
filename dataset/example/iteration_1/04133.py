import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart represents the growth in urban green spaces in three major cities across different continents over a decade. This is a hypothetical study to analyze the sustainability efforts in different regions. The cities chosen are New York, Tokyo, and Berlin. The main focus is on the linear growth trend, which shows the increase in urban green spaces (measured in square kilometers).

# Define the years for the data collection
years = np.array([2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024, 2026])

# Define the data representing the green space (in square kilometers) for each city across the time frame
new_york_green_spaces = np.array([30, 32, 35, 38, 42, 46, 51, 55, 60])
tokyo_green_spaces = np.array([25, 27, 29, 32, 35, 39, 43, 47, 52])
berlin_green_spaces = np.array([20, 23, 26, 30, 34, 38, 42, 47, 50])

# Setup the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the lines for each city
ax.plot(years, new_york_green_spaces, marker='o', linestyle='-', color='green', linewidth=2, label='New York')
ax.plot(years, tokyo_green_spaces, marker='s', linestyle='--', color='blue', linewidth=2, label='Tokyo')
ax.plot(years, berlin_green_spaces, marker='^', linestyle='-.', color='red', linewidth=2, label='Berlin')

# Add titles and labels
ax.set_title('Growth in Urban Green Spaces (2010-2026)\nA Comparative Study Across New York, Tokyo, and Berlin', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Urban Green Spaces (sq km)', fontsize=12)

# Add a legend
ax.legend(loc='upper left', fontsize=10)

# Customize grid
ax.grid(True, linestyle='--', alpha=0.6)

# Add annotation for significant milestones
milestones = {
    2016: 'Sustainability Initiatives Boost',
    2020: 'Green Policy Implementation',
    2024: 'Urban Greening Projects'
}
for year, milestone in milestones.items():
    ax.annotate(milestone, 
                xy=(year, new_york_green_spaces[np.where(years == year)[0][0]]), 
                xytext=(10, -30), 
                textcoords='offset points',
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.3'),
                fontsize=10,
                color='darkred')

# Adjust layout to fit annotations and avoid overlapping
plt.tight_layout()

# Display the plot
plt.show()