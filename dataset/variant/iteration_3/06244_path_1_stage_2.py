import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2023)

# Randomly altering energy data while preserving the structure
fossil_fuels = np.array([455, 415, 395, 375, 360, 315, 285, 245])
solar_energy = np.array([15, 25, 55, 65, 110, 135, 155, 195])
wind_energy = np.array([25, 35, 65, 75, 105, 115, 145, 185])

total_energy = fossil_fuels + solar_energy + wind_energy
share_renewable = (solar_energy + wind_energy) / total_energy * 100

plt.figure(figsize=(16, 9))

# Alter the energy data plot
plt.subplot(2, 1, 1)
plt.plot(years, fossil_fuels, label='Fossil Fuels', color='darkred', marker='o', linestyle='-')
plt.plot(years, solar_energy, label='Solar Energy', color='gold', marker='o', linestyle='-')
plt.plot(years, wind_energy, label='Wind Energy', color='deepskyblue', marker='o', linestyle='-')
plt.plot(years, total_energy, label='Total Energy', color='forestgreen', marker='D', linestyle='--')

plt.axvline(x=2019, color='gray', linestyle='--', linewidth=1)
plt.text(2019.5, 150, 'Significant Policy Update\nin 2019', rotation=90, verticalalignment='center', fontsize=10, color='gray')

plt.title('Green Energy Initiative:\nAnnual Energy Consumption Trends (2015-2022)', fontsize=14, fontweight='bold', loc='center')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Consumption (GWh)', fontsize=12)
plt.legend(loc='upper left', fontsize=10)
plt.grid(alpha=0.3)

plt.subplot(2, 1, 2)
plt.plot(years, share_renewable, label='Renewable Energy Share', color='darkviolet', marker='o', linestyle='-')

plt.title('Growth in Renewable Energy Share (2015-2022)', fontsize=14, fontweight='bold', loc='center')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Renewable Energy Share (%)', fontsize=12)
plt.legend(loc='upper left', fontsize=10)
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()