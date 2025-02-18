import matplotlib.pyplot as plt
import numpy as np

# Define years for the analysis
years = np.array([2018, 2019, 2020, 2021, 2022])

# Economic contributions (in million USD) for each sector
solar_contribution = np.array([50, 70, 90, 110, 130])
wind_contribution = np.array([40, 60, 85, 95, 105])
hydro_contribution = np.array([45, 50, 55, 60, 65])
biomass_contribution = np.array([25, 30, 35, 40, 45])

# Create the stacked bar chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the stacked bars with altered stylistic elements
ax.bar(years, solar_contribution, label='Solar', color='#FFD700', edgecolor='black', hatch='/', alpha=0.85)
ax.bar(years, wind_contribution, bottom=solar_contribution, label='Wind', color='#3CB371', edgecolor='black', hatch='\\', alpha=0.75)
ax.bar(years, hydro_contribution, bottom=solar_contribution + wind_contribution, label='Hydro', color='#4682B4', edgecolor='black', hatch='o', alpha=0.65)
ax.bar(years, biomass_contribution, bottom=solar_contribution + wind_contribution + hydro_contribution, 
       label='Biomass', color='#8B4513', edgecolor='black', hatch='x', alpha=0.55)

ax.set_title("Economic Contribution of Renewable Energy\nin GreenVille (2018-2022)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Economic Contribution (Million USD)", fontsize=14)

# Randomly altered legend parameters
ax.legend(loc='upper right', fontsize=12)

# Randomly altered grid style
ax.grid(axis='y', linestyle=':', alpha=0.5)

plt.xticks(rotation=60)

plt.tight_layout(rect=[0, 0, 0.98, 1])

# Display the plot
plt.show()