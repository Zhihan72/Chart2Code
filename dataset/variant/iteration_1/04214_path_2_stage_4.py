import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solar_energy = np.array([5, 8, 13, 18, 25, 35, 50, 70, 95, 125, 160])
wind_energy = np.array([20, 24, 30, 35, 40, 50, 60, 75, 90, 110, 135])

solar_projection = np.array([160, 200, 240, 290, 350])
wind_projection = np.array([135, 150, 165, 180, 200])
projection_years = np.arange(2021, 2026)

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, solar_energy, label='Solar', color='red', linewidth=2, marker='D')
ax.plot(years, wind_energy, label='Wind', color='blue', linewidth=2, marker='x')

ax.plot(projection_years, solar_projection, label='Solar Projection', color='red', linestyle=':', linewidth=2)
ax.plot(projection_years, wind_projection, label='Wind Projection', color='blue', linestyle='-.', linewidth=2)

ax.set_title('Renewable Energy (2010-25)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14, fontweight='bold')
ax.set_ylabel('Energy (TWh)', fontsize=14, fontweight='bold')

ax.grid(True, linewidth=1, color='gray', linestyle='-')

ax.legend(loc='lower right', fontsize=12)

ax.set_xticks(np.concatenate((years, projection_years)))
ax.set_xticklabels([str(year) for year in np.concatenate((years, projection_years))], rotation=45, ha='right')

plt.tight_layout()
plt.show()