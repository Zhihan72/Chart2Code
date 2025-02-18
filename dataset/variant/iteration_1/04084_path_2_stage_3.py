import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2041)
solar_power = np.linspace(5, 35, len(years))
wind_power = np.linspace(7, 25, len(years))
hydropower = np.linspace(20, 22, len(years))
biomass_power = np.linspace(3, 8, len(years))

# Removed geothermal_power from the data groups
renewable_sources = np.array([solar_power, wind_power, hydropower, biomass_power])

fig, ax = plt.subplots(figsize=(14, 8))

# Adjusted colors list to match remaining data groups
ax.stackplot(years, renewable_sources, 
             colors=['#FF6347', '#40E0D0', '#9370DB', '#00FA9A'], alpha=0.85)

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Production Share (%)', fontsize=12, color='black')

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()