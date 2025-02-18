import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter1d

years = np.arange(2010, 2021)

solar_eco = np.array([5, 7, 10, 14, 18, 23, 27, 32, 37, 42, 48])
wind_eco = np.array([3, 6, 10, 13, 17, 22, 26, 30, 33, 37, 40])
hydro_eco = np.array([2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 6])
total_eco = solar_eco + wind_eco + hydro_eco

solar_solarville = np.array([10, 15, 20, 28, 35, 42, 49, 56, 63, 70, 78])
wind_solarville = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5])
hydro_solarville = np.array([1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6])
total_solarville = solar_solarville + wind_solarville + hydro_solarville

solar_windycity = np.array([2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 16])
wind_windycity = np.array([8, 12, 18, 23, 29, 35, 41, 46, 51, 57, 63])
hydro_windycity = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5])
total_windycity = solar_windycity + wind_windycity + hydro_windycity

solar_hydropolis = np.array([3, 4, 5, 7, 9, 11, 13, 16, 18, 21, 24])
wind_hydropolis = np.array([4, 5, 6, 8, 11, 14, 17, 20, 23, 26, 29])
hydro_hydropolis = np.array([5, 5, 6, 7, 8, 9, 10, 10, 11, 11, 12])
total_hydropolis = solar_hydropolis + wind_hydropolis + hydro_hydropolis

smooth_eco = gaussian_filter1d(total_eco, sigma=2)
smooth_solarville = gaussian_filter1d(total_solarville, sigma=2)
smooth_windycity = gaussian_filter1d(total_windycity, sigma=2)
smooth_hydropolis = gaussian_filter1d(total_hydropolis, sigma=2)

fig, ax = plt.subplots(4, 1, figsize=(12, 24), sharex=True, constrained_layout=True)

# New color scheme
ax[3].stackplot(years, solar_eco, wind_eco, hydro_eco, labels=['Solar', 'Wind', 'Hydro'], colors=['#FF4500', '#6A5ACD', '#2E8B57'], alpha=0.9)
ax[3].plot(years, smooth_eco, color='purple', linestyle='--', linewidth=3, marker='s', markersize=6, label='Total (Smoothed)')
ax[3].set_title('EcoMetropolis\n2010-20', fontsize=14, weight='bold')
ax[3].set_ylabel('Energy (GW)', fontsize=12)
ax[3].legend(loc='lower right', fontsize=10)
ax[3].grid(False)

ax[2].stackplot(years, solar_solarville, wind_solarville, hydro_solarville, labels=['Solar', 'Wind', 'Hydro'], colors=['#FFD700', '#FF4500', '#4682B4'], alpha=0.9)
ax[2].plot(years, smooth_solarville, color='green', linestyle='-.', linewidth=2, marker='o', markersize=7, label='Total (Smoothed)')
ax[2].set_title('SolarVille\n2010-20', fontsize=14, weight='bold')
ax[2].set_ylabel('Energy (GW)', fontsize=12)
ax[2].legend(loc='upper right', fontsize=10)
ax[2].grid(True, linestyle='-.', alpha=0.7)

ax[1].stackplot(years, solar_windycity, wind_windycity, hydro_windycity, labels=['Solar', 'Wind', 'Hydro'], colors=['#F0E68C', '#32CD32', '#FF69B4'], alpha=0.9)
ax[1].plot(years, smooth_windycity, color='red', linestyle=':', linewidth=1.5, marker='^', markersize=8, label='Total (Smoothed)')
ax[1].set_title('WindyCity\n2010-20', fontsize=14, weight='bold')
ax[1].set_ylabel('Energy (GW)', fontsize=12)
ax[1].legend(loc='lower left', fontsize=10)
ax[1].grid(True, linestyle=':', alpha=0.6)

# Updated Hydropolis colors
ax[0].stackplot(years, solar_hydropolis, wind_hydropolis, hydro_hydropolis, labels=['Solar', 'Wind', 'Hydro'], colors=['#FAEBD7', '#98FB98', '#4682B4'], alpha=0.9)
ax[0].plot(years, smooth_hydropolis, color='blue', linestyle='-', linewidth=2, marker='d', markersize=8, label='Total (Smoothed)')
ax[0].set_title('Hydropolis\n2010-20', fontsize=14, weight='bold')
ax[0].set_ylabel('Energy (GW)', fontsize=12)
ax[0].legend(loc='upper left', fontsize=10)
ax[0].grid(True, alpha=0.5)

for axis in ax:
    axis.tick_params(axis='x', labelrotation=45)
    axis.xaxis.set_major_locator(plt.MaxNLocator(integer=True))

plt.suptitle('Renewable Energy in Cities:\n2010-2020 Review', fontsize=16, weight='bold', y=1.02)

plt.show()