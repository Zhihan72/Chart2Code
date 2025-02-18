import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2023)
fossil_fuels = np.array([450, 420, 400, 380, 350, 320, 290, 250])
solar_energy = np.array([10, 30, 50, 70, 100, 130, 160, 200])
wind_energy = np.array([20, 40, 60, 80, 100, 120, 150, 180])
# New data series for Hydro Energy
hydro_energy = np.array([15, 18, 21, 24, 30, 35, 40, 45])
# Update total energy to include Hydro Energy
total_energy = fossil_fuels + solar_energy + wind_energy + hydro_energy
share_renewable = (solar_energy + wind_energy + hydro_energy) / total_energy * 100

plt.figure(figsize=(16, 9))

plt.subplot(2, 1, 1)
plt.plot(years, fossil_fuels, color='blue', marker='o', linestyle='-', label='Fossil Fuels')
plt.plot(years, solar_energy, color='orange', marker='o', linestyle='-', label='Solar Energy')
plt.plot(years, wind_energy, color='green', marker='o', linestyle='-', label='Wind Energy')
plt.plot(years, hydro_energy, color='purple', marker='o', linestyle='-', label='Hydro Energy')
plt.plot(years, total_energy, color='red', marker='D', linestyle='--', label='Total Energy')
plt.axvline(x=2019, color='gray', linestyle='--', linewidth=1)
plt.text(2019.5, 150, 'Policy Shift\nin 2019', rotation=90, verticalalignment='center', fontsize=10, color='gray')

plt.title('Energy Initiative:\nYearly Consumption (2015-2022)', fontsize=14, fontweight='bold')
plt.xlabel('Timeline', fontsize=12)
plt.ylabel('Consumption (GWh)', fontsize=12)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(years, share_renewable, color='teal', marker='o', linestyle='-')
plt.title('Renewable Energy Rise (2015-2022)', fontsize=14, fontweight='bold')
plt.xlabel('Timeline', fontsize=12)
plt.ylabel('Renewable Share (%)', fontsize=12)

plt.tight_layout()
plt.show()