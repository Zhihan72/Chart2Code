import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter1d

# Data preparation
years = np.arange(2010, 2021)

# EcoMetropolis
solar_eco = np.array([5, 7, 10, 14, 18, 23, 27, 32, 37, 42, 48])
wind_eco = np.array([3, 6, 10, 13, 17, 22, 26, 30, 33, 37, 40])
hydro_eco = np.array([2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 6])
total_eco = solar_eco + wind_eco + hydro_eco

# WindyCity
solar_windycity = np.array([2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 16])
wind_windycity = np.array([8, 12, 18, 23, 29, 35, 41, 46, 51, 57, 63])
hydro_windycity = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5])
total_windycity = solar_windycity + wind_windycity + hydro_windycity

# Smoothing data for line plots
smooth_eco = gaussian_filter1d(total_eco, sigma=2)
smooth_windycity = gaussian_filter1d(total_windycity, sigma=2)

# Plotting the Area Chart with Line Overlay
fig, ax = plt.subplots(2, 1, figsize=(12, 12), sharex=True, constrained_layout=True)

# Use a single color for all components
single_color = '#4682B4'  # SteelBlue

# Plot for EcoMetropolis
ax[0].stackplot(years, solar_eco, wind_eco, hydro_eco, colors=[single_color]*3, alpha=0.8)
ax[0].plot(years, smooth_eco, color='black', linestyle='-', linewidth=2)
ax[0].set_title('EcoMetropolis Power Blend\n2010-2020', fontsize=14, weight='bold')
ax[0].set_ylabel('Output (GW)', fontsize=12)

# Plot for WindyCity
ax[1].stackplot(years, solar_windycity, wind_windycity, hydro_windycity, colors=[single_color]*3, alpha=0.8)
ax[1].plot(years, smooth_windycity, color='black', linestyle='-', linewidth=2)
ax[1].set_title('WindyCity Power Blend\n2010-2020', fontsize=14, weight='bold')
ax[1].set_xlabel('Timeline', fontsize=12)
ax[1].set_ylabel('Output (GW)', fontsize=12)

# Adjusting tick parameters
for axis in ax:
    axis.tick_params(axis='x', labelrotation=45)
    axis.xaxis.set_major_locator(plt.MaxNLocator(integer=True))

plt.suptitle('Renewables Embrace in Visionary Hubs:\nA Decadal Glimpse', fontsize=16, weight='bold', y=1.02)

plt.show()