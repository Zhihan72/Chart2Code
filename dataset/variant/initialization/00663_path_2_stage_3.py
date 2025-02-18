import matplotlib.pyplot as plt
import numpy as np

months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])

solar_energy = np.array([50, 60, 75, 85, 100, 120, 135, 130, 115, 95, 75, 55])
wind_energy = np.array([80, 85, 90, 95, 105, 110, 120, 125, 130, 125, 100, 90])
hydro_energy = np.array([110, 100, 115, 135, 145, 140, 150, 155, 145, 130, 115, 110])
biomass_energy = np.array([35, 37, 40, 42, 45, 47, 50, 48, 45, 42, 38, 35])

energy_data = np.vstack([solar_energy, wind_energy, hydro_energy, biomass_energy])

plt.figure(figsize=(14, 8))

plt.stackplot(months, energy_data, 
              colors=['#1abc9c', '#3498db', '#e67e22', '#f1c40f'], alpha=0.8)

plt.title('Renewable Energy Highlights:\nMonthly Output Overview for 2023', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Monthly Timeline', fontsize=14)
plt.ylabel('Generated Energy - GWh', fontsize=14)

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()