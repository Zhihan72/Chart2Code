import matplotlib.pyplot as plt
import numpy as np

# Define the years and energy data
years = np.arange(2010, 2021)
energy_types = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass']

# Given energy production data for each energy type
solar_energy = [220, 960, 50, 300, 120, 650, 160, 520, 800, 80, 400]
wind_energy = [150, 720, 90, 900, 200, 350, 70, 450, 580, 1080, 270]
hydro_energy = [380, 460, 340, 320, 300, 440, 400, 360, 500, 480, 420]
geothermal_energy = [65, 30, 25, 50, 70, 20, 60, 40, 55, 45, 35]
biomass_energy = [160, 280, 300, 220, 180, 190, 240, 170, 260, 150, 200]

# Combine the energy data and sum them per year
total_energy_per_year = np.array(solar_energy) + np.array(wind_energy) + \
                        np.array(hydro_energy) + np.array(geothermal_energy) + \
                        np.array(biomass_energy)

# Create a sorted index based on the total energy per year in descending order
sorted_index = np.argsort(total_energy_per_year)[::-1]

# Sort the years and data based on the total energy per year
sorted_years = years[sorted_index]
sorted_data = total_energy_per_year[sorted_index]

fig, ax = plt.subplots(figsize=(14, 8))

# Plot the sorted bar chart
ax.bar(sorted_years, sorted_data, color='#66B3FF', edgecolor='black')

ax.set_xticks(sorted_years)
ax.set_xticklabels(sorted_years, rotation=45)

ax.yaxis.grid(True, linestyle='-.', linewidth=0.5, alpha=0.8)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_linewidth(2)
ax.spines['right'].set_color('grey')

plt.tight_layout()
plt.show()