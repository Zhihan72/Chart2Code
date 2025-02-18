import matplotlib.pyplot as plt
import numpy as np

# Backstory: The chart represents the projected growth of exports of different types of fruits from a country over a decade (2023-2033).
# The country has been focusing on increasing fruit exports to boost its agricultural sector.

# Define the years and the types of fruits
years = np.arange(2023, 2034)
types_of_fruits = ['Apples', 'Bananas', 'Cherries', 'Dragonfruits', 'Elderberries']

# Contextual data for the projection of fruit exports
apples = [100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300]
bananas = [80, 85, 90, 95, 100, 110, 115, 120, 130, 140, 150]
cherries = [40, 50, 60, 70, 80, 90, 100, 110, 120, 125, 130]
dragonfruits = [10, 20, 25, 30, 35, 45, 50, 55, 60, 70, 80]
elderberries = [5, 10, 20, 25, 30, 40, 45, 50, 55, 65, 75]

# Combine data into a list of numpy arrays for convenience
export_data = [np.array(apples), np.array(bananas), np.array(cherries), np.array(dragonfruits), np.array(elderberries)]

# Create a figure for the line chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot line chart for each type of fruit
for fruit, data in zip(types_of_fruits, export_data):
    ax.plot(years, data, marker='o', label=fruit)

# Title and labels
ax.set_title('Projected Growth of Fruit Exports (2023-2033)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Export Volume (in thousands of tons)', fontsize=12)

# Set x-ticks to avoid overlap and rotate them
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Add grid and legend
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(title='Types of Fruits', fontsize=10, title_fontsize=11)

# Automatically adjust the layout to prevent overlaps
plt.tight_layout()

# Show the plot
plt.show()