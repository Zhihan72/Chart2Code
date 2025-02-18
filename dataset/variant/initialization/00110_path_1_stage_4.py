import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2024)

# Energy data
solar_energy = np.array([10, 15, 22, 33, 50, 65, 80, 100, 125, 150, 180])
wind_energy = np.array([20, 25, 35, 50, 70, 90, 120, 160, 200, 250, 310])
hydro_energy = np.array([50, 55, 60, 65, 70, 75, 78, 80, 82, 85, 88])
geothermal_energy = np.array([5, 7, 10, 12, 15, 18, 20, 22, 25, 28, 30])
biomass_energy = np.array([8, 10, 12, 14, 20, 25, 30, 35, 40, 48, 55])

energy_data = np.vstack([solar_energy, wind_energy, hydro_energy, geothermal_energy, biomass_energy])

plt.figure(figsize=(12, 8))
plt.stackplot(years, energy_data, colors=['#FFD700', '#87CEEB', '#006400', '#FFA500', '#8B4513'], alpha=0.8)

plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 701, 50))

plt.show()