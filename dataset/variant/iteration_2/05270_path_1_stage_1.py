import matplotlib.pyplot as plt
import numpy as np

# Data for energy production (in gigawatt hours, GWh) over the years for different renewable sources
years = np.arange(2010, 2021)

# Altered energy production data for each renewable source, preserving original structure
solar_energy = [30, 70, 40, 110, 90, 60, 160, 50, 220, 190, 130]
wind_energy = [65, 20, 30, 50, 140, 35, 110, 95, 80, 125, 155]
hydro_energy = [50, 60, 70, 100, 105, 55, 90, 85, 95, 80, 75]

# Stack the data for area plotting
energy_data = np.vstack([solar_energy, wind_energy, hydro_energy])

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#ffa07a', '#20b2aa', '#b0c4de']

ax.stackplot(years, energy_data, labels=['Solar Energy', 'Wind Energy', 'Hydro Energy'],
             colors=colors, alpha=0.85)

ax.set_title('GreenVille Renewable Energy Revolution:\nCumulative Growth of Energy Production (2010-2020)', fontsize=18, fontweight='bold', loc='center')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Production (GWh)', fontsize=14)

ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(loc='upper left', title='Renewable Sources', fontsize=12, title_fontsize='13')

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

# Calculate proportions with altered data
total_2020_energy = np.sum(np.array([solar_energy[-1], wind_energy[-1], hydro_energy[-1]]))
proportions = [solar_energy[-1]/total_2020_energy, wind_energy[-1]/total_2020_energy, hydro_energy[-1]/total_2020_energy]

ax2.bar(['Solar Energy', 'Wind Energy', 'Hydro Energy'], proportions, color=colors, alpha=0.85)

ax2.set_title('Proportional Contribution of Renewable Sources in 2020', fontsize=16, fontweight='bold')
ax2.set_xlabel('Renewable Source', fontsize=14)
ax2.set_ylabel('Proportion of Total Production', fontsize=14)

plt.tight_layout()
plt.show()