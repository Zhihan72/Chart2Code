import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart represents the energy production from various renewable sources in the city of GreenVille over a decade (2010-2020).
# The aim is to showcase the cumulative growth and contribution of solar, wind, and hydro energy to the city's energy grid each year.

# Data for energy production (in gigawatt hours, GWh) over the years for different renewable sources
years = np.arange(2010, 2021)  # From 2010 to 2020

# Energy production data for each renewable source
solar_energy = [30, 40, 50, 60, 70, 90, 110, 130, 160, 190, 220]  # Solar energy production
wind_energy = [20, 30, 35, 50, 65, 80, 95, 110, 125, 140, 155]    # Wind energy production
hydro_energy = [50, 55, 60, 70, 75, 80, 85, 90, 95, 100, 105]     # Hydro energy production

# Stack the data for area plotting
energy_data = np.vstack([solar_energy, wind_energy, hydro_energy])

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))

# Define colors for each energy source
colors = ['#ffa07a', '#20b2aa', '#b0c4de']

ax.stackplot(years, energy_data, labels=['Solar Energy', 'Wind Energy', 'Hydro Energy'],
             colors=colors, alpha=0.85)

# Adding title and labels with line breaks for better readability
ax.set_title('GreenVille Renewable Energy Revolution:\nCumulative Growth of Energy Production (2010-2020)', fontsize=18, fontweight='bold', loc='center')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Production (GWh)', fontsize=14)

# Adding grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Adding a legend with a title
ax.legend(loc='upper left', title='Renewable Sources', fontsize=12, title_fontsize='13')

# Automatically adjust layout to prevent overlapping
plt.xticks(years, rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()

# Add annotations for key points
ax.annotate('Rapid adoption of solar energy', xy=(2014, 130), xytext=(2012, 150),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

ax.annotate('Steady growth in hydro energy', xy=(2020, 105), xytext=(2017, 115),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

# Second plot: Line chart showing the proportion of each energy source in 2020
fig, ax2 = plt.subplots(figsize=(8, 6))

# Calculate proportions
total_2020_energy = np.sum(np.array([solar_energy[-1], wind_energy[-1], hydro_energy[-1]]))
proportions = [solar_energy[-1]/total_2020_energy, wind_energy[-1]/total_2020_energy, hydro_energy[-1]/total_2020_energy]

ax2.bar(['Solar Energy', 'Wind Energy', 'Hydro Energy'], proportions, color=colors, alpha=0.85)

# Adding title and labels
ax2.set_title('Proportional Contribution of Renewable Sources in 2020', fontsize=16, fontweight='bold')
ax2.set_xlabel('Renewable Source', fontsize=14)
ax2.set_ylabel('Proportion of Total Production', fontsize=14)

# Display the plot
plt.tight_layout()
plt.show()