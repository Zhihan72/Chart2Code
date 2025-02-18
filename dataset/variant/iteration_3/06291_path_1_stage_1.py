import matplotlib.pyplot as plt
import numpy as np

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
colors = ['#FF9999', '#66B2FF', '#99FF99', '#71C7EC']  # Changed last color

# Plot the stacked area chart
ax.stackplot(years, vr_data, labels=vr_categories, colors=colors, alpha=0.8)

# Set titles and labels
ax.set_title('Growth of VR Content Consumption Over Years\n(2015-2025)', fontsize=15, fontweight='light', pad=15)
ax.set_xlabel('Year', fontsize=11)
ax.set_ylabel('Consumption (Million Hours)', fontsize=11)

# Format x-axis for readability
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=30, ha='center')

# Modify the legend style and location 
ax.legend(title='VR Categories', loc='lower left', fontsize=9, fancybox=True, framealpha=0.5)

# Modify grid style
ax.grid(color='blue', linestyle='-', linewidth=0.6, axis='both', alpha=0.5)

# Add annotations
annotations = {
    2022: 'Fitness rise during pandemic',
    2018: 'Growth in Games',
    2025: 'Educational surge'
}

for year, annotation in annotations.items():
    ax.annotate(annotation, xy=(year, vr_data[:, years.tolist().index(year)].sum()), 
                xytext=(year, vr_data[:, years.tolist().index(year)].sum() + 5),
                arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=8, ha='left')

# Subplot for total consumption: use different line style and marker
ax2 = ax.twinx()
total_consumption = vr_data.sum(axis=0)
ax2.plot(years, total_consumption, label='Total Consumption', color='purple', linestyle=':', marker='s', markersize=6, linewidth=1.2)
ax2.fill_between(years, total_consumption, color='purple', alpha=0.07)

# Set secondary y-axis label
ax2.set_ylabel('Total Consumption (Million Hours)', fontsize=11)

# Adjust layout
plt.tight_layout(rect=[0, 0, 0.87, 1])

# Show the plot
plt.show()