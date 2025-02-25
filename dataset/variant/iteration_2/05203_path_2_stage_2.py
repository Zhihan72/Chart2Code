import matplotlib.pyplot as plt
import numpy as np

# Define city names
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

# Total CO2 emissions for each city over six months
total_emissions = [1230, 1155, 1080, 1285, 980]

# Colors for each city
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Setup the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the total emissions as a horizontal bar chart
ax.barh(cities, total_emissions, color=colors, edgecolor='black')

# Title and labels for the total emissions bar chart
ax.set_title('Total CO2 Emissions by City Over Six Months', fontsize=16, fontweight='bold')
ax.set_xlabel('Total CO2 Emissions (metric tons)', fontsize=14)
ax.set_ylabel('Cities', fontsize=14)

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()