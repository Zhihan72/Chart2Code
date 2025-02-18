import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# This chart explores the food production trends of a fictional land "Agroland" over the decade from 2010 to 2020.
# The categories include Cereals, Fruits, Vegetables, and Dairy.

# Define the years for the chart
years = np.arange(2010, 2021)

# Define the food categories
food_categories = ["Cereals", "Fruits", "Vegetables", "Dairy"]

# Food production data (in million tonnes)
cereals = [280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480]
fruits = [50, 55, 60, 70, 80, 90, 100, 110, 120, 130, 140]
vegetables = [100, 105, 110, 115, 120, 130, 140, 150, 160, 170, 180]
dairy = [150, 152, 155, 157, 160, 165, 170, 175, 180, 185, 190]

# Stack the data
food_production = np.vstack([cereals, fruits, vegetables, dairy])

# Define the colors for each food category
colors = ['#FFD700', '#FF6347', '#32CD32', '#4682B4']

# Initialize the figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the stacked area chart
ax.stackplot(years, food_production, labels=food_categories, colors=colors, alpha=0.85)

# Set titles and labels
ax.set_title('Food Production Trends in Agroland\n2010-2020', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Production (Million Tonnes)', fontsize=12)

# Format x-axis for better readability
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Add legend outside of the plot
ax.legend(title='Food Categories', loc='upper left', fontsize=10, bbox_to_anchor=(1.05, 1), frameon=False)

# Add grid lines to the y-axis for better readability
ax.grid(color='gray', linestyle='--', linewidth=0.5, axis='y', alpha=0.7)

# Adjust layout to prevent overlap and ensure visibility
plt.tight_layout()

# Show the plot
plt.show()