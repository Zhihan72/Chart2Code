import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)
solaria_energy = [20, 25, 35, 45, 55, 70, 85, 100, 120, 135, 150]
windlandia_energy = [15, 30, 50, 65, 80, 95, 110, 130, 150, 170, 200]
hydrovia_energy = [50, 52, 54, 55, 60, 63, 65, 68, 70, 75, 78]
geothermalia_energy = [5, 7, 10, 14, 19, 25, 32, 40, 49, 59, 70]
biomassia_energy = [10, 15, 22, 30, 40, 50, 65, 80, 100, 125, 150]
oceanica_energy = [2, 3, 5, 7, 9, 12, 16, 21, 27, 34, 40]
fusionlandia_energy = [1, 2, 3, 5, 8, 12, 18, 25, 33, 42, 52]

energy_sources = np.array([
    solaria_energy,
    windlandia_energy,
    hydrovia_energy,
    geothermalia_energy,
    biomassia_energy,
    oceanica_energy,
    fusionlandia_energy
])

fig, ax = plt.subplots(figsize=(10, 6))

new_colors = ['red', 'blue', 'green', 'purple', 'cyan', 'magenta', 'lime']

ax.stackplot(years, energy_sources, labels=['Solar', 'Wind', 'Hydro', 'Geo', 'Bio', 'Ocean', 'Fusion'],
             colors=new_colors, alpha=0.8)
ax.set_title("Renewable Energy Gen. (2020-2030)", fontsize=14, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Energy (GWh)", fontsize=12)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Source')
ax.grid(alpha=0.3)

plt.tight_layout()
plt.show()