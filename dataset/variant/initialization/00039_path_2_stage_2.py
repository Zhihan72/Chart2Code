import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)
solar_energy = [20, 25, 30, 40, 50, 65, 80, 100, 130, 160]
wind_energy = [50, 55, 60, 80, 100, 120, 150, 180, 210, 240]
hydro_energy = [100, 100, 110, 115, 120, 125, 130, 135, 140, 145]
bioenergy = [30, 35, 40, 50, 55, 65, 75, 85, 95, 100]

energy_data = np.vstack([solar_energy, wind_energy, hydro_energy, bioenergy])

fig, ax = plt.subplots(figsize=(10, 6))

ax.stackplot(years, energy_data, labels=['Sol', 'Wnd', 'Hyd', 'Bio'],
             colors=['#ff7f50', '#4682b4', '#9acd32', '#f4a460'], alpha=0.8)

ax.set_title('Renewable Energy\n2010-2019', fontsize=14, fontweight='bold')
ax.set_xlabel('Yr', fontsize=12)
ax.set_ylabel('Consumption (PJ)', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper left', title='Sources', fontsize=10, title_fontsize='13')

plt.xticks(years, rotation=45)
plt.tight_layout()
plt.show()