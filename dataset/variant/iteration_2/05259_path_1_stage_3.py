import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
# Manually altered CO2 levels
co2_levels = [371, 376, 369, 382, 379, 384, 373, 387, 397, 390, 400, 403, 405, 394, 418, 407, 410, 416, 412, 414, 392]
# Manually altered global temperatures
global_temps = [14.4, 14.2, 14.5, 14.7, 14.6, 14.9, 14.3, 15.0, 15.2, 14.9, 15.4, 15.3, 15.6, 15.1, 15.9, 15.5, 15.8, 15.6, 14.8, 15.7, 15.4]
# Manually altered population in millions
population_million = [6493.4, 6364.7, 6112.8, 6235.1, 6751.2, 6880.1, 6622.4, 7138.2, 7267.4, 7396.8, 7655.8, 7526.2, 7785.6, 7009.1, 8305.7, 8436.0, 8566.4, 7915.4, 8045.4, 8175.5, 8697.0]
# Manually altered CO2 emissions
co2_emissions = [29.5, 28.2, 27.5, 30.1, 30.8, 31.5, 28.9, 33.2, 34.5, 32.6, 37.0, 36.4, 35.8, 32.0, 40.1, 39.5, 38.9, 35.1, 33.9, 38.2, 37.6]
per_capita_emissions = [co2/pop for co2, pop in zip(co2_emissions, population_million)]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), dpi=100)

ax1.plot(years, co2_levels, color='darkred', linestyle='-', linewidth=2, marker='o')
ax1.plot(years, global_temps, color='darkblue', linestyle='--', linewidth=2, marker='s')

ax1.set_title('CO2 & Temp Trends (2000-2020)', fontsize=16, weight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('CO2 (ppm)', fontsize=14, color='darkred')
ax1.tick_params(axis='y', labelcolor='darkred')

ax1_secondary = ax1.twinx()
ax1_secondary.set_ylabel('Temp (°C)', fontsize=14, color='darkblue')
ax1_secondary.tick_params(axis='y', labelcolor='darkblue')

ax2.plot(years, per_capita_emissions, color='green', linestyle='-', linewidth=2, marker='o')

ax2.set_title('Per Capita CO2 Emissions', fontsize=16, weight='bold')
ax2.set_xlabel('Year', fontsize=14)
ax2.set_ylabel('Per Capita CO2\n(MT/Person)', fontsize=14, color='green')
ax2.tick_params(axis='y', labelcolor='green')

ax1.annotate('Kyoto Ends', xy=(2012, co2_levels[12]), xytext=(2008, 410),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, ha='center')

ax2.annotate('Sharp Rise', xy=(2015, per_capita_emissions[15]), xytext=(2010, 4.5),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, ha='center')

plt.tight_layout()
plt.show()