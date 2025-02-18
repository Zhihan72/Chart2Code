import matplotlib.pyplot as plt
import numpy as np

# Original data
decades = np.array(['80s', '90s', '00s', '10s', '20s'])
solar_energy = np.array([2, 5, 10, 18, 25])
wind_energy = np.array([1, 3, 12, 20, 30])
hydropower = np.array([10, 15, 20, 25, 28])
geothermal = np.array([2, 4, 6, 10, 12])
biomass = np.array([5, 6, 8, 15, 20])
tidal_energy = np.array([1, 2, 3, 5, 6])

fig, ax = plt.subplots(figsize=(12, 7))

# Shuffled colors
ax.fill_between(decades, solar_energy, label='Sun Power', color='#32CD32', alpha=0.7, step='pre')
ax.fill_between(decades, solar_energy, wind_energy + solar_energy, label='Breeze Power', color='#2F4F4F', alpha=0.7, step='mid')
ax.fill_between(decades, wind_energy + solar_energy, wind_energy + solar_energy + hydropower, label='Water Energy', color='#FFD700', alpha=0.7, linewidth=2, linestyle='-.')
ax.fill_between(decades, wind_energy + solar_energy + hydropower, wind_energy + solar_energy + hydropower + geothermal, label='Earth Heat', color='#1E90FF', alpha=0.7, linestyle=':')
ax.fill_between(decades, wind_energy + solar_energy + hydropower + geothermal, wind_energy + solar_energy + hydropower + geothermal + biomass, label='Bio Energy', color='#4682B4', alpha=0.7, linestyle='-')
ax.fill_between(decades, wind_energy + solar_energy + hydropower + geothermal + biomass, wind_energy + solar_energy + hydropower + geothermal + biomass + tidal_energy, label='Sea Waves', color='#8B4513', alpha=0.7, linestyle='--')

ax.set_title('Green Energy Sources Over Time\n(From 1980s Onwards)', fontsize=16, fontweight='bold')
ax.set_xlabel('Time Periods', fontsize=12)
ax.set_ylabel('Energy Share (%)', fontsize=12)

ax.set_xticks(np.arange(len(decades)))
ax.set_xticklabels(decades, rotation=45)

ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.7)
ax.legend(loc='best', title='Sources of Power', fontsize=9, frameon=False)

plt.tight_layout()
plt.show()