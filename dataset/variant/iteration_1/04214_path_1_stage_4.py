import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_energy = np.array([5, 8, 13, 18, 25, 35, 50, 70, 95, 125, 160])
wind_energy = np.array([20, 24, 30, 35, 40, 50, 60, 75, 90, 110, 135])
hydro_energy = np.array([60, 62, 65, 68, 70, 73, 77, 80, 84, 87, 90])
biomass_energy = np.array([15, 18, 20, 22, 25, 28, 31, 34, 38, 42, 46])
geothermal_energy = np.array([3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16])

solar_projection = np.array([160, 200, 240, 290, 350])
wind_projection = np.array([135, 150, 165, 180, 200])
hydro_projection = np.array([90, 92, 94, 96, 98])
biomass_projection = np.array([46, 50, 55, 60, 65])
geothermal_projection = np.array([16, 18, 20, 22, 25])

projection_years = np.arange(2021, 2026)

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, solar_energy, color='crimson', linewidth=2, marker='o')
ax.plot(years, wind_energy, color='darkblue', linewidth=2, marker='s')
ax.plot(years, hydro_energy, color='forestgreen', linewidth=2, marker='^')
ax.plot(years, biomass_energy, color='purple', linewidth=2, marker='D')
ax.plot(years, geothermal_energy, color='darkred', linewidth=2, marker='*')

ax.plot(projection_years, solar_projection, color='crimson', linestyle='--', linewidth=2)
ax.plot(projection_years, wind_projection, color='darkblue', linestyle='--', linewidth=2)
ax.plot(projection_years, hydro_projection, color='forestgreen', linestyle='--', linewidth=2)
ax.plot(projection_years, biomass_projection, color='purple', linestyle='--', linewidth=2)
ax.plot(projection_years, geothermal_projection, color='darkred', linestyle='--', linewidth=2)

ax.set_title('Renew. Energy (2010-25)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14, fontweight='bold')
ax.set_ylabel('Prod. (TWh)', fontsize=14, fontweight='bold')

ax.set_xticks(np.concatenate((years, projection_years)))
ax.set_xticklabels([str(year) for year in np.concatenate((years, projection_years))], rotation=45, ha='right')

plt.tight_layout()
plt.show()