import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2000, 2021)

# Manually shuffled values from the original arrays
solar = np.array([2, 35, 2.8, 12, 1.5, 1.2, 22, 50, 1, 40, 30, 18, 55, 10, 3.5, 8, 5, 45, 27, 6.5, 15])
wind = np.array([24, 27, 18, 5, 7, 32, 22, 2, 14, 9, 28, 2, 35, 26, 30, 4, 12, 23, 3, 33, 20])
hydro = np.array([21.5, 23.5, 21, 24, 12, 10, 14, 13, 11, 16, 18, 17, 25, 20, 15, 19, 24.5, 23, 22.5, 22, 24])
biomass = np.array([12.5, 11, 10.5, 8, 1.5, 5, 7, 12, 6, 2, 13.5, 9, 3, 10, 4, 11.5, 3.5, 13, 12.5, 9.5, 1])

energy_data = np.vstack([solar, wind, hydro, biomass])

fig, ax = plt.subplots(figsize=(14, 8))

single_color = '#1f77b4'
ax.stackplot(years, energy_data, colors=[single_color]*energy_data.shape[0], alpha=0.8)

plt.tight_layout()

plt.show()