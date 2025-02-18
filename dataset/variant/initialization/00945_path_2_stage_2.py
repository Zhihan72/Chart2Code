import matplotlib.pyplot as plt
import numpy as np

# Define years for the analysis
years = np.array([2018, 2019, 2020, 2021, 2022])

# Randomly shuffle each sector's contributions while maintaining the same length
solar_contribution = np.array([90, 70, 130, 50, 110])  # Randomly shuffled
wind_contribution = np.array([85, 105, 40, 60, 95])   # Randomly shuffled
hydro_contribution = np.array([55, 60, 50, 65, 45])   # Randomly shuffled
biomass_contribution = np.array([35, 30, 45, 25, 40]) # Randomly shuffled

fig, ax = plt.subplots(figsize=(12, 7))

ax.bar(years, solar_contribution, color='#FDB813', edgecolor='none', alpha=0.9)
ax.bar(years, wind_contribution, bottom=solar_contribution, color='#00A86B', edgecolor='none', alpha=0.9)
ax.bar(years, hydro_contribution, bottom=solar_contribution + wind_contribution, color='#1F78B4', edgecolor='none', alpha=0.9)
ax.bar(years, biomass_contribution, bottom=solar_contribution + wind_contribution + hydro_contribution, color='#8B4513', edgecolor='none', alpha=0.9)

ax.set_title("Economic Contribution of Renewable Energy\nin GreenVille (2018-2022)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Economic Contribution (Million USD)", fontsize=14)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()