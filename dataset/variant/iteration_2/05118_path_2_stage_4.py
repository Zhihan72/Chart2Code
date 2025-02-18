import matplotlib.pyplot as plt
import numpy as np

# Data construction
years = np.arange(2020, 2031)
solar_energy = np.array([10, 14, 18, 22, 27, 33, 40, 48, 57, 67, 78])
wind_energy = np.array([15, 18, 22, 26, 31, 37, 44, 51, 59, 68, 78])
hydro_energy = np.array([20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
geothermal_energy = np.array([5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 25])
biomass_energy = np.array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

# Stacked data array
data = np.vstack([solar_energy, wind_energy, hydro_energy, geothermal_energy, biomass_energy])

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, data, colors=['#4caf50'] * 5, alpha=0.8)

# Removing axis labels and annotations
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 241, 20))
ax.tick_params(labelbottom=False, labelleft=False)  # Removes tick labels

plt.tight_layout()
plt.show()