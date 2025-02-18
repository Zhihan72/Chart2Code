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
colors = ['#FF6347', '#3CB371', '#4682B4', '#DA70D6']  # Changed color set

ax.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Bio', 'Geo'], colors=colors, alpha=0.8)

ax.plot(years, total_energy, color='black', linestyle='--', linewidth=2, label='Total')

ax.set_title('Renewable Growth (2010-22)', fontsize=15, weight='bold', pad=20)
ax.set_xlabel('Yr', fontsize=12)
ax.set_ylabel('Energy (GWh)', fontsize=12)

ax.legend(loc='upper left', fontsize=10)

ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.xticks(rotation=45)

ax.annotate('Solar Surge', xy=(2015, 50), xytext=(2011, 180),
            arrowprops=dict(facecolor='yellow', arrowstyle='->'),
            fontsize=10, color='orange')

ax.annotate('Wind Growth', xy=(2021, 420), xytext=(2017, 490),
            arrowprops=dict(facecolor='blue', arrowstyle='->'),
            fontsize=10, color='blue')

plt.tight_layout()

plt.show()