import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2010, 2020)
avg_temperatures = np.array([15.2, 15.3, 15.4, 15.7, 16.0, 16.1, 16.2, 16.4, 16.5, 16.8])
temperature_errors = np.array([0.2, 0.3, 0.25, 0.3, 0.2, 0.3, 0.15, 0.2, 0.25, 0.2])
co2_emissions = np.array([370, 375, 380, 385, 390, 395, 400, 405, 410, 415])

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# First subplot: Line chart with random style elements
ax1.errorbar(
    years, avg_temperatures, yerr=temperature_errors,
    fmt='--d', color='royalblue', ecolor='silver',
    elinewidth=1.5, capsize=4, capthick=1.5, alpha=0.85, label='Temperature ± Error'
)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Temperature (°C)', fontsize=12)
ax1.set_title('Yearly Temperature Trends (2010-2019)', fontsize=13)
ax1.grid(False)
ax1.spines['top'].set_visible(False)
ax1.set_xlim(2009, 2020)
ax1.set_ylim(14.5, 17.5)
ax1.legend(loc='lower right', fontsize=10)

# Second subplot: Bar chart with random style elements
ax2.bar(years, co2_emissions, color='firebrick', alpha=0.9, label='CO2 Emissions')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('CO2 Emissions (ppm)', fontsize=12)
ax2.set_title('Yearly CO2 Emissions (2010-2019)', fontsize=13)
ax2.grid(False)
ax2.spines['right'].set_visible(False)
ax2.set_xlim(2009, 2020)
ax2.set_ylim(365, 420)
ax2.legend(loc='best', fontsize=10)

plt.tight_layout()
plt.show()