import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2010, 2020)
avg_temperatures = np.array([15.2, 15.3, 15.4, 15.7, 16.0, 16.1, 16.2, 16.4, 16.5, 16.8])
temperature_errors = np.array([0.2, 0.3, 0.25, 0.3, 0.2, 0.3, 0.15, 0.2, 0.25, 0.2])
co2_emissions = np.array([370, 375, 380, 385, 390, 395, 400, 405, 410, 415])

# Sort data
sorted_indices_temp = np.argsort(avg_temperatures)
sorted_years_temp = years[sorted_indices_temp]
sorted_avg_temperatures = avg_temperatures[sorted_indices_temp]
sorted_temperature_errors = temperature_errors[sorted_indices_temp]

sorted_indices_co2 = np.argsort(-co2_emissions)
sorted_years_co2 = years[sorted_indices_co2]
sorted_co2_emissions = co2_emissions[sorted_indices_co2]

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 12))

# Temperature plot
ax1.bar(sorted_years_temp, sorted_avg_temperatures, yerr=sorted_temperature_errors,
        color='mediumseagreen', alpha=0.8, label='Varied Temp ± Error', capsize=5)
ax1.set_xlabel('Timeline', fontsize=12, fontweight='bold')
ax1.set_ylabel('Heat Levels (°C)', fontsize=12, fontweight='bold')
ax1.set_title('Mixed Yearly Temperature Patterns\nCoastal Zone (2010-2019)', fontsize=13, fontweight='bold')
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_ylim(14.5, 17.5)
ax1.legend(loc='upper left', fontsize=10)

# CO2 emissions plot
ax2.bar(sorted_years_co2, sorted_co2_emissions, color='steelblue', alpha=0.8, label='Gas Emissions')
ax2.set_xlabel('Timeline', fontsize=12, fontweight='bold')
ax2.set_ylabel('Gas Levels (ppm)', fontsize=12, fontweight='bold')
ax2.set_title('Mixed Yearly CO2 Trends\n(2010-2019)', fontsize=13, fontweight='bold')
ax2.grid(True, linestyle='--', alpha=0.7, axis='y')
ax2.set_ylim(365, 420)
ax2.legend(loc='upper left', fontsize=10)

plt.tight_layout()
plt.show()