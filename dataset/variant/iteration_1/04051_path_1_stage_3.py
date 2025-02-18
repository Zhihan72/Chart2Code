import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_energy = [5, 8, 15, 18, 25, 35, 50, 70, 90, 110, 130]
wind_energy = [10, 15, 20, 28, 35, 45, 60, 80, 100, 120, 140]
hydro_energy = [20, 22, 25, 30, 35, 40, 45, 50, 55, 60, 65]

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(years, solar_energy, color='red', marker='o', markersize=8, linewidth=2)
ax1.plot(years, wind_energy, color='blue', marker='^', markersize=8, linewidth=2, linestyle='--')
ax1.plot(years, hydro_energy, color='cyan', marker='s', markersize=8, linewidth=2, linestyle='-.')

ax1.set_title('Renewable Energy (2010-2020)', fontsize=18, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Energy (GWh)', fontsize=14)

ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 151, step=10))

combined_energy = np.array(solar_energy) + np.array(wind_energy) + np.array(hydro_energy)
ax2 = ax1.twinx()
ax2.plot(years, combined_energy, color='magenta', linewidth=2, alpha=0.6, linestyle='-')
ax2.set_ylabel('Total Energy (GWh)', fontsize=14, color='magenta')
ax2.tick_params(axis='y', labelcolor='magenta')

plt.tight_layout()
plt.show()