import matplotlib.pyplot as plt
import numpy as np

# Define the years for the chart
years = np.arange(2010, 2021)

# Food production data (in million tonnes)
cereals = [280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480]
fruits = [50, 55, 60, 70, 80, 90, 100, 110, 120, 130, 140]
vegetables = [100, 105, 110, 115, 120, 130, 140, 150, 160, 170, 180]
dairy = [150, 152, 155, 157, 160, 165, 170, 175, 180, 185, 190]
meat = [200, 205, 210, 220, 230, 240, 250, 260, 270, 280, 290]
seafood = [70, 72, 75, 77, 80, 82, 85, 88, 90, 93, 95]

# Stack the data
food_production = np.vstack([cereals, fruits, vegetables, dairy, meat, seafood])

# Use a single color for all food categories
single_color = '#4682B4'

# Initialize the figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the stacked area chart
ax.stackplot(years, food_production, colors=[single_color for _ in range(6)], alpha=0.85)

# Format x-axis
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()