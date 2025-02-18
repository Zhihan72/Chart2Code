import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2041, 0.25)

solar_energy = np.interp(years, np.arange(2000, 2041), np.linspace(2, 650, 41)) + 10 * np.sin(np.linspace(0, 8 * np.pi, len(years)))
wind_energy = solar_energy + np.interp(years, np.arange(2000, 2041), np.linspace(1, 490, 41)) + 15 * np.cos(np.linspace(0, 6 * np.pi, len(years)))
hydro_energy = wind_energy + np.interp(years, np.arange(2000, 2041), np.linspace(15, 600, 41)) + 20 * np.sin(np.linspace(0, 4 * np.pi, len(years)))

fig, ax = plt.subplots(figsize=(16, 10))

ax.fill_between(years, solar_energy, color='gold', alpha=0.7, label='Solar Energy')
ax.fill_between(years, solar_energy, wind_energy, color='deepskyblue', alpha=0.7, label='Wind Energy')
ax.fill_between(years, wind_energy, hydro_energy, color='darkseagreen', alpha=0.7, label='Hydro Energy')

ax.set_title('Renewable Energy Production (2000-2040): Transformation', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Production (GW)', fontsize=12)

ax.set_xticks(years[::8])
ax.set_xticklabels([str(int(year)) if i % 4 == 0 else '' for i, year in enumerate(years[::8])], rotation=45, ha='right')

ax.grid(linestyle='-.', alpha=0.6)

ax.legend(loc='lower right', fontsize=9, shadow=True)

ax.plot(years, hydro_energy, color='purple', linestyle='-.', linewidth=2.5, marker='o', label='Total Energy')

plt.tight_layout()

plt.show()