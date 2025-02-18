import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2041)
solar_power = np.linspace(5, 35, len(years))
wind_power = np.linspace(7, 25, len(years))
hydropower = np.linspace(20, 22, len(years))
geothermal_power = np.linspace(1, 10, len(years))
biomass_power = np.linspace(3, 8, len(years))

renewable_sources = np.array([solar_power, wind_power, hydropower, geothermal_power, biomass_power])

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, renewable_sources, 
             colors=['#FDB813', '#77B5FE', '#4682B4', '#D2691E', '#32CD32'], alpha=0.85)

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Production Share (%)', fontsize=12, color='black')

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()