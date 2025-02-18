import matplotlib.pyplot as plt
import numpy as np

# Define city names and months
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
months = ['January', 'February', 'March', 'April', 'May', 'June']

# Data representing monthly CO2 emissions (in metric tons) for each city
ny_emissions = [180, 190, 200, 210, 220, 230]
la_emissions = [170, 180, 190, 195, 205, 215]
chicago_emissions = [160, 170, 180, 190, 185, 195]
houston_emissions = [200, 205, 210, 215, 225, 230]
phoenix_emissions = [150, 155, 160, 165, 170, 180]

# Setup the figure and axis
fig, axs = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})

# Colors for each city
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plot the base bar chart for each city
for i, city in enumerate(cities):
    axs[0].bar(city, ny_emissions[i], color=colors[i], label=city)

# Title and labels for the bar chart
axs[0].set_title('Monthly CO2 Emissions for January in Major US Cities', fontsize=16, fontweight='bold')
axs[0].set_xlabel('City', fontsize=14)
axs[0].set_ylabel('CO2 Emissions in January (metric tons)', fontsize=14)
axs[0].legend(title='Cities')

# Adding grid lines to the y-axis
axs[0].yaxis.grid(True, linestyle='--', alpha=0.7)

# Calculate the total emissions for each city
total_emissions = [sum(ny_emissions), sum(la_emissions), sum(chicago_emissions), sum(houston_emissions), sum(phoenix_emissions)]

# Plot the total emissions as a horizontal bar chart
axs[1].barh(cities, total_emissions, color=colors, edgecolor='black')

# Title and labels for the total emissions bar chart
axs[1].set_title('Total CO2 Emissions by City Over Six Months', fontsize=16, fontweight='bold')
axs[1].set_xlabel('Total CO2 Emissions (metric tons)', fontsize=14)
axs[1].set_ylabel('Cities', fontsize=14)

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()