import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2041)
solar_power = np.linspace(5, 35, len(years))
wind_power = np.linspace(7, 25, len(years))
hydropower = np.linspace(20, 22, len(years))
biomass_power = np.linspace(3, 8, len(years))

renewable_sources = np.array([solar_power, wind_power, hydropower, biomass_power])

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, renewable_sources, 
             colors=['#FF6347', '#40E0D0', '#9370DB', '#00FA9A'], alpha=0.85)

ax.set_xlabel('Timeline', fontsize=12)
ax.set_ylabel('Power Contribution (%)', fontsize=12, color='black')

plt.xticks(rotation=45)
plt.tight_layout()
plt.title('Renewable Energy Sources Variation Over Years', fontsize=14)

plt.show()