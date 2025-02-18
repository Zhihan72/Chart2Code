import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2024)
solar_energy = np.array([10, 15, 22, 33, 50, 65, 80, 100, 125, 150, 180])
wind_energy = np.array([20, 25, 35, 50, 70, 90, 120, 160, 200, 250, 310])
hydro_energy = np.array([50, 55, 60, 65, 70, 75, 78, 80, 82, 85, 88])

energy_data = np.vstack([solar_energy, wind_energy, hydro_energy])

plt.figure(figsize=(12, 8))
plt.stackplot(years, energy_data, colors=['#228B22', '#228B22', '#228B22'], alpha=0.8)

plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 601, 50))
plt.grid(alpha=0.3, linestyle='--')

plt.tight_layout()
plt.show()