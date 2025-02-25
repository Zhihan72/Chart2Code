import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

# Manually altered the data by shuffling values in each group
industrial_solar = [32, 7, 20, 12, 15, 9, 28, 25, 18, 30, 5]
industrial_wind = [4, 22, 12, 3, 17, 24, 6, 20, 8, 15, 10]
industrial_hydro = [10, 27, 32, 8, 22, 15, 17, 19, 24, 12, 30]
industrial_geothermal = [14, 8, 6, 2, 4, 20, 16, 18, 10, 3, 12]

residential_solar = [14, 5, 23, 3, 8, 25, 11, 19, 16, 21, 1]
residential_wind = [6, 8, 11, 3, 0.5, 5, 9, 10, 1, 4, 2]
residential_hydro = [13, 4, 10, 2, 6, 15, 8, 19, 3, 21, 17]
residential_geothermal = [8, 2, 11, 5, 9, 4, 7, 10, 2, 3, 1]

transportation_solar = [6, 7, 2, 4, 12, 14, 3, 8, 1, 10, 2]
transportation_wind = [5, 4, 0.5, 1, 7, 3, 2, 8, 1.5, 0.2, 6]
transportation_hydro = [1.5, 0.8, 6, 2, 9, 3, 5, 7, 1, 8, 4]
transportation_geothermal = [4, 3.5, 2.5, 0.5, 1.5, 2, 5, 4.5, 3, 0.2, 1]

plt.figure(figsize=(16, 10))

plt.subplot(3, 1, 1)
plt.stackplot(years, industrial_solar, industrial_wind, industrial_hydro, industrial_geothermal,
              labels=['Solar', 'Wind', 'Hydro', 'Geothermal'], colors=['#FFD700', '#1E90FF', '#00FF7F', '#FF6347'], alpha=0.9)
plt.title('Industrial Sector: Sustainable Energy Adoption in Greenlandia', fontsize=14, fontweight='bold')
plt.ylabel('Energy Use (GWh)', fontsize=12)
plt.legend(loc='upper left', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)

plt.subplot(3, 1, 2)
plt.stackplot(years, residential_solar, residential_wind, residential_hydro, residential_geothermal,
              labels=['Solar', 'Wind', 'Hydro', 'Geothermal'], colors=['#FFD700', '#1E90FF', '#00FF7F', '#FF6347'], alpha=0.9)
plt.title('Residential Sector: Sustainable Energy Adoption in Greenlandia', fontsize=14, fontweight='bold')
plt.ylabel('Energy Use (GWh)', fontsize=12)
plt.legend(loc='upper left', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)

plt.subplot(3, 1, 3)
plt.stackplot(years, transportation_solar, transportation_wind, transportation_hydro, transportation_geothermal,
              labels=['Solar', 'Wind', 'Hydro', 'Geothermal'], colors=['#FFD700', '#1E90FF', '#00FF7F', '#FF6347'], alpha=0.9)
plt.title('Transportation Sector: Sustainable Energy Adoption in Greenlandia', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Use (GWh)', fontsize=12)
plt.legend(loc='upper left', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()