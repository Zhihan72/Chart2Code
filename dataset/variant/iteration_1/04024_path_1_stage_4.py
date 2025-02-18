import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2023)

solar_energy = np.array([10, 20, 35, 50, 70, 95, 120, 150, 190, 240, 300, 370, 450])
wind_energy = np.array([5, 15, 30, 50, 80, 115, 155, 200, 250, 300, 360, 420, 490])
geothermal_energy = np.array([1, 3, 5, 10, 18, 28, 35, 47, 60, 80, 100, 130, 160])

energy_data = np.vstack([solar_energy, wind_energy, geothermal_energy])
total_energy = solar_energy + wind_energy + geothermal_energy

fig, ax = plt.subplots(figsize=(12, 8))
colors = ['#4682B4', '#FF6347', '#3CB371']  # Adjusted color set

ax.stackplot(years, energy_data, labels=['Geo', 'Solar', 'Wind'], colors=colors, alpha=0.7)

ax.plot(years, total_energy, color='purple', linestyle='-.', linewidth=1.5, marker='o', markersize=5, label='Total Energy')

ax.set_title('Renewable Energy Growth (2010-22)', fontsize=16, weight='bold', pad=25)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('Energy (GWh)', fontsize=13)

ax.legend(loc='lower right', fontsize=9, frameon=False)

ax.grid(False)

plt.xticks(rotation=30)

plt.tight_layout()

plt.show()