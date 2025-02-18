import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2023)

solar_energy = np.array([10, 20, 35, 50, 70, 95, 120, 150, 190, 240, 300, 370, 450])
wind_energy = np.array([5, 15, 30, 50, 80, 115, 155, 200, 250, 300, 360, 420, 490])
# biomass_energy = np.array([3, 5, 10, 20, 35, 55, 80, 105, 140, 180, 230, 280, 340])
geothermal_energy = np.array([1, 3, 5, 10, 18, 28, 35, 47, 60, 80, 100, 130, 160])

# Updated energy data and total energy
energy_data = np.vstack([solar_energy, wind_energy, geothermal_energy])
total_energy = solar_energy + wind_energy + geothermal_energy

fig, ax = plt.subplots(figsize=(12, 8))
colors = ['#FFD700', '#1E90FF', '#FF4500']

# Modified stackplot without biomass energy
ax.stackplot(years, energy_data, labels=['Sunshine Energy', 'Breeze Power', 'Earth Heat'], colors=colors, alpha=0.7)
ax.plot(years, total_energy, color='green', linestyle='-.', linewidth=2.5, label='Total Renewable', marker='o')

ax.set_title('Eco-village: Renewable Energy Surge (2010-2022)', fontsize=16, weight='bold', color='darkblue', pad=15)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('Energy Output (GWh)', fontsize=13)

ax.legend(loc='upper right', fontsize=11, frameon=False)
ax.grid(True, linestyle='-', linewidth=0.7, alpha=0.6, color='gray')

plt.xticks(rotation=45)

ax.annotate('Solar Boom!', xy=(2014, 60), xytext=(2011, 150),
            arrowprops=dict(facecolor='orange', arrowstyle='-|>'),
            fontsize=11, color='red')

ax.annotate('Breezy Advances', xy=(2020, 400), xytext=(2017, 450),
            arrowprops=dict(facecolor='cyan', arrowstyle='-|>'),
            fontsize=11, color='blue')

plt.tight_layout()
plt.show()