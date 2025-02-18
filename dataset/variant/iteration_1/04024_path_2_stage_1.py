import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2023)

solar_energy = np.array([10, 20, 35, 50, 70, 95, 120, 150, 190, 240, 300, 370, 450])
wind_energy = np.array([5, 15, 30, 50, 80, 115, 155, 200, 250, 300, 360, 420, 490])
biomass_energy = np.array([3, 5, 10, 20, 35, 55, 80, 105, 140, 180, 230, 280, 340])
geothermal_energy = np.array([1, 3, 5, 10, 18, 28, 35, 47, 60, 80, 100, 130, 160])

energy_data = np.vstack([solar_energy, wind_energy, biomass_energy, geothermal_energy])
total_energy = solar_energy + wind_energy + biomass_energy + geothermal_energy

fig, ax = plt.subplots(figsize=(12, 8))
colors = ['#FFD700', '#1E90FF', '#32CD32', '#FF4500']

ax.stackplot(years, energy_data, labels=['Sunshine Energy', 'Breeze Power', 'Bio-fuel', 'Earth Heat'], colors=colors, alpha=0.8)
ax.plot(years, total_energy, color='black', linestyle='--', linewidth=2, label='Total Renewable')

# Changed titles and labels
ax.set_title('Eco-village: Renewable Energy Surge (2010-2022)', fontsize=15, weight='bold', pad=20)
ax.set_xlabel('Year of Analysis', fontsize=12)
ax.set_ylabel('Energy Output (GWh)', fontsize=12)

ax.legend(loc='upper left', fontsize=10)
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.xticks(rotation=45)

# Randomly altered annotation texts
ax.annotate('Solar Boom!', xy=(2015, 50), xytext=(2011, 180),
            arrowprops=dict(facecolor='yellow', arrowstyle='->'),
            fontsize=10, color='orange')

ax.annotate('Breezy Advances', xy=(2021, 420), xytext=(2017, 490),
            arrowprops=dict(facecolor='blue', arrowstyle='->'),
            fontsize=10, color='blue')

plt.tight_layout()
plt.show()