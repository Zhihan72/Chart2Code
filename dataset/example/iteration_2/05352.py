import numpy as np
import matplotlib.pyplot as plt

# Define the years for the x-axis
years = np.arange(2000, 2021)

# Data for the market share percentages for renewable energy sources
solar = np.array([1, 1.2, 1.5, 2, 2.8, 3.5, 5, 6.5, 8, 10, 12, 15, 18, 22, 27, 30, 35, 40, 45, 50, 55])
wind = np.array([2, 2, 3, 4, 5, 7, 9, 12, 14, 18, 20, 22, 23, 24, 26, 27, 28, 30, 32, 33, 35])
hydro = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 21.5, 22, 22.5, 23, 23.5, 24, 24, 24.5, 25])
biomass = np.array([1, 1.5, 2, 3, 3.5, 4, 5, 6, 7, 8, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 12.5, 13, 13.5])

# Stack the data for the area chart
energy_data = np.vstack([solar, wind, hydro, biomass])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Define colors for each energy source
colors = ['#ff7f0e', '#1f77b4', '#2ca02c', '#d62728']
labels = ['Solar', 'Wind', 'Hydropower', 'Biomass']

# Create an area chart using stackplot
ax.stackplot(years, energy_data, labels=labels, colors=colors, alpha=0.8)

# Set title and labels with appropriate size adjustments
ax.set_title('The Rise of Renewable Energy:\nMarket Share of Renewable Energy Sources (2000-2020)', fontsize=18, fontweight='bold', ha='center')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Market Share (%)', fontsize=14)

# Add a legend with title for clarity
ax.legend(loc='upper left', fontsize=12, title='Renewable Sources')

# Adding detailed annotations for significant shifts
significant_years = {
    'Solar': 2020,
    'Wind': 2015,
    'Hydropower': 2009,
    'Biomass': 2010
}
annotations = {
    'Solar': 55,
    'Wind': 18,
    'Hydropower': 21,
    'Biomass': 9
}

for source, year in significant_years.items():
    ax.annotate(f"{source}: {annotations[source]}%",
                xy=(year, annotations[source]), 
                xytext=(year - 10, annotations[source] + 10),
                arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
                fontsize=10, fontweight='bold', color='darkred')

# Displaying the grid for better readability
ax.grid(linestyle='--', linewidth=0.7, alpha=0.5)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()