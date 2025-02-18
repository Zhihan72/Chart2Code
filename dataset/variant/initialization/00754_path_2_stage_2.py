import numpy as np
import matplotlib.pyplot as plt

# Define cities and plant types
cities = ['NY', 'LDN', 'TYO']
plant_types = ['Tree', 'Shrub', 'Flower']
years = np.array(['2018', '2019', '2020', '2021', '2022'])

# Data: Number of plants planted
data = np.array([
    [[30, 25, 40], [35, 28, 38], [38, 30, 35], [40, 32, 32], [42, 34, 30]],
    [[20, 18, 22], [22, 20, 24], [24, 22, 26], [26, 24, 28], [28, 26, 30]],
    [[15, 10, 12], [16, 11, 14], [18, 13, 16], [20, 15, 18], [22, 17, 20]],
])

# Process data for diverging bar chart
data_pos = data[:2]  # First two plant types as positive values
data_neg = data[2:]  # Third plant type as negative for divergence

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Colors for plant types
colors = ['#8bc34a', '#ff9800', '#e91e63']

# Plot each city's data
for i, city in enumerate(cities):
    for plant_idx in range(len(data) - 1):  # Positive stacks
        ax.barh(-np.arange(len(years)) + i*len(years), data_pos[plant_idx, :, i],
                left=np.sum(data_pos[:plant_idx, :, i], axis=0), color=colors[plant_idx],
                label=plant_types[plant_idx] if i == 0 else "")
    
    ax.barh(-np.arange(len(years)) + i*len(years), -data_neg[0, :, i], color=colors[2],
            label=plant_types[2] if i == 0 else "")  # Negative stack

# Combine years and cities for labels
ytick_labels = [f"{year} - {city}" for city in cities for year in years]
ytick_positions = -np.arange(len(ytick_labels))

# Axes labels and customization
ax.set_yticks(ytick_positions)
ax.set_yticklabels(ytick_labels, fontsize=10)
ax.set_xticks(np.arange(-100, 101, 20))
ax.set_xlabel('Number of Plants')
ax.set_ylabel('Year - City')
ax.legend(title='Plants', loc='upper right', bbox_to_anchor=(1.2, 1))

# Title
ax.set_title('Urban Greenery \nDiverging Plant Analysis', pad=20, fontsize=14, weight='bold')

# Display plot
plt.tight_layout()
plt.show()