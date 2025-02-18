import matplotlib.pyplot as plt
import numpy as np

months = np.array([
    'Feb', 'Apr', 'Oct', 'Nov', 'Jul', 'May',
    'Mar', 'Sep', 'Aug', 'Jun', 'Dec', 'Jan'
])

# Manually altered energy data while preserving dimensional structure
solar_energy = np.array([95, 75, 60, 85, 130, 135, 50, 100, 115, 75, 55, 120])
wind_energy = np.array([100, 85, 125, 95, 110, 130, 80, 120, 105, 90, 90, 125])
hydro_energy = np.array([135, 100, 130, 115, 110, 150, 110, 145, 140, 145, 115, 155])
biomass_energy = np.array([42, 45, 48, 37, 35, 35, 40, 42, 45, 38, 50, 47])

energy_data = np.vstack([solar_energy, wind_energy, hydro_energy, biomass_energy])

plt.figure(figsize=(14, 8))

# Maintain consistent single color for all groups
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