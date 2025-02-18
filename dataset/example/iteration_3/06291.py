import matplotlib.pyplot as plt
import numpy as np

# Backstory: 
# Imagine we're showcasing the growth of different types of virtual reality (VR) content over the years. 
# Our chart will depict the consumption trends of various VR content categories: Games, Educational, Social, and Fitness. 

# Define the years for the chart
years = np.arange(2015, 2026)

# Define the VR content categories
vr_categories = ["Games", "Educational", "Social", "Fitness"]

# VR content consumption data (in million hours)
vr_data = np.array([
    [5, 10, 15, 22, 30, 38, 50, 65, 80, 98, 120],  # Games
    [1, 2, 3, 5, 8, 12, 18, 25, 33, 43, 55],  # Educational
    [3, 5, 7, 10, 15, 20, 27, 35, 45, 58, 72],  # Social
    [1, 1.5, 2, 4, 7, 11, 16, 22, 29, 37, 46]   # Fitness
])

# Initialize the figure and axes
fig, ax = plt.subplots(figsize=(14, 8))

# Define a color map
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']

# Plot the stacked area chart
ax.stackplot(years, vr_data, labels=vr_categories, colors=colors, alpha=0.85)

# Set titles and labels with appropriate descriptions
ax.set_title('Growth of VR Content Consumption Over Years\n(2015-2025)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Consumption (Million Hours)', fontsize=12)

# Format x-axis for better readability
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Add legend outside of the plot
ax.legend(title='VR Content Categories', loc='upper left', fontsize=10, bbox_to_anchor=(1.05, 1), frameon=False)

# Add grid lines for better readability
ax.grid(color='gray', linestyle='--', linewidth=0.5, axis='y', alpha=0.7)

# Add annotations for key data points
annotations = {
    2022: 'Fitness sees growth amid pandemic',
    2018: 'Rapid growth in Games',
    2025: 'Educational content surges'
}

for year, annotation in annotations.items():
    ax.annotate(annotation, xy=(year, vr_data[:, years.tolist().index(year)].sum()), 
                xytext=(year, vr_data[:, years.tolist().index(year)].sum() + 7),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9, ha='center')

# Adding a subplot with another type of chart: Line plot of total consumption
ax2 = ax.twinx()
total_consumption = vr_data.sum(axis=0)
ax2.plot(years, total_consumption, label='Total Consumption', color='black', linestyle='-.', marker='o', linewidth=1.5)
ax2.fill_between(years, total_consumption, color='black', alpha=0.1)

# Set secondary y-axis label for the total consumption
ax2.set_ylabel('Total Consumption (Million Hours)', fontsize=12)

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Show the plot
plt.show()