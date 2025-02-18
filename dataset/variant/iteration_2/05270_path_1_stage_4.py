import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_energy = [30, 70, 40, 110, 90, 60, 160, 50, 220, 190, 130]
wind_energy = [65, 20, 30, 50, 140, 35, 110, 95, 80, 125, 155]
hydro_energy = [50, 60, 70, 100, 105, 55, 90, 85, 95, 80, 75]
energy_data = np.vstack([solar_energy, wind_energy, hydro_energy])

fig, ax = plt.subplots(figsize=(14, 8))
new_colors = ['#8a2be2', '#ff6347', '#4682b4']

ax.stackplot(years, energy_data, colors=new_colors, alpha=0.75)

ax.grid(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.5)

plt.xticks(years, rotation=30, fontsize=10)
plt.yticks(fontsize=10)

fig, ax2 = plt.subplots(figsize=(8, 6))

total_2020_energy = np.sum(np.array([solar_energy[-1], wind_energy[-1], hydro_energy[-1]]))
proportions = [solar_energy[-1] / total_2020_energy,
               wind_energy[-1] / total_2020_energy,
               hydro_energy[-1] / total_2020_energy]

ax2.bar(['Solar Energy', 'Wind Energy', 'Hydro Energy'], proportions, color=new_colors, alpha=0.75)
ax2.grid_axis = None  # Remove grid

plt.xticks(rotation=30, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()