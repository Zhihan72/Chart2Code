import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solar_energy = [5, 8, 15, 18, 25, 35, 50, 70, 90, 110, 130]
wind_energy = [10, 15, 20, 28, 35, 45, 60, 80, 100, 120, 140]
hydro_energy = [20, 22, 25, 30, 35, 40, 45, 50, 55, 60, 65]

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(years, solar_energy, label='Solar Energy', color='red', marker='x', markersize=10, linewidth=3)
ax1.plot(years, wind_energy, label='Wind Energy', color='teal', marker='*', markersize=10, linewidth=3, linestyle='--')
ax1.plot(years, hydro_energy, label='Hydroelectric Energy', color='purple', marker='d', markersize=10, linewidth=3, linestyle='-.')

ax1.set_title('Renewable Energy Adoption Over a Decade', fontsize=18, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Energy Consumption (GWh)', fontsize=14)

ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 151, step=10))
ax1.grid(alpha=0.5, linestyle='-.')

ax1.legend(loc='lower right', fontsize=12, edgecolor='black')

key_years = [2013, 2018]
for year in key_years:
    idx = np.where(years == year)[0][0]
    ax1.annotate(f'{year}', xy=(years[idx], solar_energy[idx]), xytext=(years[idx], solar_energy[idx]+10),
                 arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10, color='red')
    ax1.annotate(f'{year}', xy=(years[idx], wind_energy[idx]), xytext=(years[idx], wind_energy[idx]-15),
                 arrowprops=dict(facecolor='gray', arrowstyle='-'), fontsize=10, color='teal')
    ax1.annotate(f'{year}', xy=(years[idx], hydro_energy[idx]), xytext=(years[idx], hydro_energy[idx]+5),
                 arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10, color='purple')

combined_energy = np.array(solar_energy) + np.array(wind_energy) + np.array(hydro_energy)
ax2 = ax1.twinx()
ax2.plot(years, combined_energy, label='Combined Renewable Energy', color='gray', linewidth=2, alpha=0.6, linestyle='--')
ax2.set_ylabel('Combined Energy (GWh)', fontsize=14, color='gray')
ax2.tick_params(axis='y', labelcolor='gray')
ax2.legend(loc='upper left', fontsize=12, edgecolor='black')

plt.tight_layout()
plt.show()