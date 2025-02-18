import matplotlib.pyplot as plt
import numpy as np

months = np.array([
    'Feb', 'Apr', 'Oct', 'Nov', 'Jul', 'May',
    'Mar', 'Sep', 'Aug', 'Jun', 'Dec', 'Jan'
])

solar_energy = np.array([60, 85, 95, 75, 135, 100, 75, 115, 130, 120, 55, 50])
wind_energy = np.array([85, 95, 125, 100, 120, 105, 90, 130, 125, 110, 90, 80])
hydro_energy = np.array([100, 135, 130, 115, 150, 145, 115, 145, 155, 140, 110, 110])
biomass_energy = np.array([37, 42, 42, 38, 50, 45, 40, 45, 48, 47, 35, 35])

energy_data = np.vstack([solar_energy, wind_energy, hydro_energy, biomass_energy])

plt.figure(figsize=(14, 8))

# Apply a single color consistently across all data groups
plt.stackplot(months, energy_data, labels=['Biomass', 'Solar', 'Hydro', 'Wind'],
              colors=['#3498db'], alpha=0.8, edgecolor='black', linestyle='-.')

plt.title('Renewable Energy Surge & Monthly Patterns of Generation in 2023',
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Months', fontsize=14)
plt.ylabel('GWh Produced', fontsize=14)

plt.xticks(rotation=45)

plt.legend(loc='lower right', fontsize=12, frameon=True)

plt.grid(alpha=0.5, linestyle=':', linewidth=0.8)

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_linestyle('--')

plt.tight_layout()

plt.show()