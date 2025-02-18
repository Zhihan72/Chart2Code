import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2041)

solar_power = np.array([5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 35])
wind_power = np.array([7, 8, 9, 10, 11, 12, 15, 11, 17, 12, 13, 14, 18, 16, 15, 14, 19, 18, 17, 15, 11, 10, 9, 18, 20, 19, 21, 23, 24, 22, 25, 16, 18, 20, 22, 18, 14, 9, 8, 25, 23])
hydropower = np.array([20, 20.5, 21, 21.1, 21.2, 21.3, 21.4, 21.5, 21.6, 21.7, 21.8, 21.9, 22, 21.8, 21.6, 21.4, 21.2, 21, 20.8, 20.6, 20.4, 20.2, 20, 21, 21.2, 21.4, 21.6, 21.8, 22, 21.9, 21.7, 21.5, 21.3, 21.1, 20.9, 20.7, 20.5, 20.3, 20.1, 21, 20])
geothermal_power = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 10])
biomass_power = np.array([3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 7.7, 7.4, 7.1, 6.8, 6.5, 6.2, 5.9, 5.6, 5.3, 5, 4.7, 4.4, 4.1, 3.8, 3.5, 3.2, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 6.8, 6.5, 6.2, 5.9, 8])

renewable_sources = np.array([solar_power, wind_power, hydropower, geothermal_power, biomass_power])

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, renewable_sources, colors=['#32CD32', '#4682B4', '#77B5FE', '#FDB813', '#D2691E'], alpha=0.85)

ax.set_title("Growth of Renewable Energy Sources from 2000 to 2040", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Production Share (%)', fontsize=12, color='black')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()