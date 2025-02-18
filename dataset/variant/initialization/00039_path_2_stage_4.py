import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)
solar_energy = [25, 30, 20, 50, 40, 80, 65, 130, 100, 160]
wind_energy = [55, 60, 50, 100, 80, 150, 120, 210, 180, 240]
hydro_energy = [100, 110, 100, 120, 115, 130, 125, 140, 135, 145]
bioenergy = [35, 40, 30, 55, 50, 75, 65, 95, 85, 100]

energy_data = np.vstack([solar_energy, wind_energy, hydro_energy, bioenergy])

fig, ax = plt.subplots(figsize=(10, 6))

ax.stackplot(years, energy_data, labels=['Sol', 'Wnd', 'Hyd', 'Bio'],
             colors=['#ff6347', '#00bfff', '#32cd32', '#ffa07a'], alpha=0.9,
             edgecolor='gray', linestyle='-', linewidth=0.8)

ax.set_title('Renewable Energy: 2010-2019', fontsize=16, fontweight='normal')
ax.set_xlabel('Years', fontsize=11, style='italic')
ax.set_ylabel('Energy Consumption (PJ)', fontsize=11, style='italic')

ax.grid(True, linestyle=':', linewidth=0.7, alpha=0.7)

ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='Energy Sources',
          fontsize=9, title_fontsize='11', fancybox=True, shadow=True)

plt.xticks(years, rotation=30)
plt.tight_layout(rect=[0, 0, 0.85, 1])

plt.show()