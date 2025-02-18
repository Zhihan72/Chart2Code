import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)

solar_energy = [10, 20, 30, 45, 55, 70, 85, 100, 115, 130, 150]
wind_energy = [15, 25, 35, 45, 60, 75, 90, 105, 120, 140, 160]
hydro_energy = [20, 30, 40, 55, 65, 80, 95, 110, 130, 150, 170]
geothermal_energy = [5, 10, 15, 25, 35, 45, 60, 75, 90, 110, 130]

colors = ['#FFD700', '#1E90FF', '#32CD32', '#FF6347']

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, solar_energy, wind_energy, hydro_energy, geothermal_energy, 
             colors=colors, alpha=0.8)

ax.set_xticks(years)
ax.set_xticklabels([])

ax.legend(frameon=False)

ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()

plt.show()