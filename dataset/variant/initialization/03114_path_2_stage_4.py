import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2041, 0.25)

solar_energy = np.interp(years, np.arange(2000, 2041), np.linspace(2, 650, 41)) + 10 * np.sin(np.linspace(0, 8 * np.pi, len(years)))
wind_energy = solar_energy + np.interp(years, np.arange(2000, 2041), np.linspace(1, 490, 41)) + 15 * np.cos(np.linspace(0, 6 * np.pi, len(years)))
hydro_energy = wind_energy + np.interp(years, np.arange(2000, 2041), np.linspace(15, 600, 41)) + 20 * np.sin(np.linspace(0, 4 * np.pi, len(years)))

fig, ax = plt.subplots(figsize=(16, 10))

ax.fill_between(years, solar_energy, color='tomato', alpha=0.7, label='Solar')
ax.fill_between(years, solar_energy, wind_energy, color='lightcoral', alpha=0.7, label='Wind')
ax.fill_between(years, wind_energy, hydro_energy, color='mediumseagreen', alpha=0.7, label='Hydro')

ax.set_title('Renewable Energy (2000-2040)', fontsize=16, fontweight='bold')
ax.set_xlabel('Yr', fontsize=12)
ax.set_ylabel('Production (GW)', fontsize=12)

ax.set_xticks(years[::8])
ax.set_xticklabels([str(int(year)) if i % 4 == 0 else '' for i, year in enumerate(years[::8])], rotation=45, ha='right')

ax.grid(linestyle='-.', alpha=0.6)

ax.legend(loc='lower right', fontsize=9, shadow=True)

ax.plot(years, hydro_energy, color='indigo', linestyle='-.', linewidth=2.5, marker='o', label='Total')

plt.tight_layout()

plt.show()