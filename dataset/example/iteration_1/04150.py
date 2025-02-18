import matplotlib.pyplot as plt
import numpy as np

# Backstory: Study on the spread of seasonal flu cases across different cities
# during different months of the year.
cities = ['City A', 'City B', 'City C', 'City D']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Data: Monthly flu cases reported in various cities
flu_cases_data = {
    'City A': [30, 25, 40, 35, 50, 60, 45, 55, 65, 70, 75, 80],
    'City B': [20, 18, 25, 28, 30, 35, 40, 45, 50, 55, 60, 65],
    'City C': [15, 10, 20, 25, 30, 35, 40, 45, 55, 60, 70, 75],
    'City D': [10, 5, 8, 12, 18, 20, 25, 30, 40, 50, 55, 60]
}

# Prepare the data for the box plot
data_for_box = [flu_cases_data[city] for city in cities]

# Setup the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Create the box plot
box = ax.boxplot(data_for_box, patch_artist=True, notch=True, vert=True,
                 boxprops=dict(facecolor='#D3D3D3', color='black'),
                 whiskerprops=dict(color='black'),
                 capprops=dict(color='black'),
                 medianprops=dict(color='red'),
                 flierprops=dict(markerfacecolor='blue', marker='o', markersize=5, alpha=0.6))

# Set the titles and labels
ax.set_title('Seasonal Flu Cases Distribution\n Across Different Cities (2023)', fontsize=16, fontweight='bold')
ax.set_xlabel('Cities', fontsize=12)
ax.set_ylabel('Number of Flu Cases', fontsize=12)

# Set custom x-ticks
ax.set_xticks(np.arange(1, len(cities) + 1))
ax.set_xticklabels(cities, fontsize=11)

# Add grid lines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add a line plot on a secondary y-axis to show total flu cases per month
total_flu_cases_per_month = [sum(month) for month in zip(*data_for_box)]

ax2 = ax.twinx()
ax2.plot(months, total_flu_cases_per_month, color='blue', marker='o', linestyle='-', linewidth=2, markersize=6, label='Total Flu Cases')
ax2.set_ylabel('Total Flu Cases', fontsize=12, color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

# Adding a legend and customizing it
handles = [plt.Line2D([0], [0], color='red', lw=2, label='Median'),
           plt.Line2D([0], [0], marker='o', color='w', label='Outliers', 
                      markerfacecolor='blue', markersize=6),
           plt.Line2D([0], [0], color='blue', lw=2, label='Total Flu Cases')]
ax.legend(handles=handles, loc='upper left', fontsize=10)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()