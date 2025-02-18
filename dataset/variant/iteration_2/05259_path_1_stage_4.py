import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
co2_levels = [371, 376, 369, 382, 379, 384, 373, 387, 397, 390, 400, 403, 405, 394, 418, 407, 410, 416, 412, 414, 392]
global_temps = [14.4, 14.2, 14.5, 14.7, 14.6, 14.9, 14.3, 15.0, 15.2, 14.9, 15.4, 15.3, 15.6, 15.1, 15.9, 15.5, 15.8, 15.6, 14.8, 15.7, 15.4]

fig, ax1 = plt.subplots(figsize=(14, 6), dpi=100)

ax1.plot(years, co2_levels, color='darkred', linestyle='-', linewidth=2, marker='o')
ax1.plot(years, global_temps, color='darkblue', linestyle='--', linewidth=2, marker='s')

ax1.set_title('CO2 & Temp Trends (2000-2020)', fontsize=16, weight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('CO2 (ppm)', fontsize=14, color='darkred')
ax1.tick_params(axis='y', labelcolor='darkred')

ax1_secondary = ax1.twinx()
ax1_secondary.set_ylabel('Temp (°C)', fontsize=14, color='darkblue')
ax1_secondary.tick_params(axis='y', labelcolor='darkblue')

ax1.annotate('Kyoto Ends', xy=(2012, co2_levels[12]), xytext=(2008, 410),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, ha='center')

plt.tight_layout()
plt.show()