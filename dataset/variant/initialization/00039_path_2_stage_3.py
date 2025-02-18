import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)
solar_energy = [20, 25, 30, 40, 50, 65, 80, 100, 130, 160]
wind_energy = [50, 55, 60, 80, 100, 120, 150, 180, 210, 240]
hydro_energy = [100, 100, 110, 115, 120, 125, 130, 135, 140, 145]
bioenergy = [30, 35, 40, 50, 55, 65, 75, 85, 95, 100]

energy_data = np.vstack([solar_energy, wind_energy, hydro_energy, bioenergy])

fig, ax = plt.subplots(figsize=(10, 6))

# Alter line styles and marker types for the stack plot
ax.stackplot(years, energy_data, labels=['Sol', 'Wnd', 'Hyd', 'Bio'],
             colors=['#ff6347', '#00bfff', '#32cd32', '#ffa07a'], alpha=0.9,
             edgecolor='gray', linestyle='-', linewidth=0.8)

ax.set_title('Renewable Energy: 2010-2019', fontsize=16, fontweight='normal')
ax.set_xlabel('Years', fontsize=11, style='italic')
ax.set_ylabel('Energy Consumption (PJ)', fontsize=11, style='italic')

# Change grid style
ax.grid(True, linestyle=':', linewidth=0.7, alpha=0.7)

# Altar legend style
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='Energy Sources',
          fontsize=9, title_fontsize='11', fancybox=True, shadow=True)

# Modify ticks and layout for clear visibility
plt.xticks(years, rotation=30)
plt.tight_layout(rect=[0, 0, 0.85, 1]) # Adjust layout to accommodate legend

plt.show()