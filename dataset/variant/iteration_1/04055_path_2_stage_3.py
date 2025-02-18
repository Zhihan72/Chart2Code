import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_energy = [10, 25, 45, 65, 90, 120, 150, 180, 220, 250, 300]
wind_energy = [40, 60, 75, 95, 120, 145, 170, 195, 210, 240, 280]
hydro_energy = [80, 82, 85, 90, 95, 100, 100, 105, 110, 115, 120]

total_renewable = [s + w + h for s, w, h in zip(solar_energy, wind_energy, hydro_energy)]

fig, ax1 = plt.subplots(figsize=(14, 9))

ax1.plot(years, solar_energy, color='purple', linestyle='-', linewidth=2, marker='o', label='Photon Power')
ax1.plot(years, wind_energy, color='darkgreen', linestyle='--', linewidth=2, marker='s', label='Gale Force')
ax1.plot(years, hydro_energy, color='magenta', linestyle='-.', linewidth=2, marker='^', label='Aqua Surge')

ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

ax2 = ax1.twinx()
ax2.plot(years, total_renewable, color='darkred', linestyle='-', linewidth=2, marker='x', label='Aggregate Green')

ax1.set_title('Chronicle of Green Energies: 2010-2020\nExamining Key Trends in Environmentally-Friendly Sources', fontsize=16, weight='bold')
ax1.set_xlabel('Calendar Year', fontsize=14)
ax1.set_ylabel('Sector Output (TWh)', fontsize=14, color='black')
ax2.set_ylabel('Combined Yield (TWh)', fontsize=14, color='black')

z_solar = np.polyfit(years, solar_energy, 1)
p_solar = np.poly1d(z_solar)
ax1.plot(years, p_solar(years), color='purple', linestyle=':', alpha=0.5, linewidth=1)

z_wind = np.polyfit(years, wind_energy, 1)
p_wind = np.poly1d(z_wind)
ax1.plot(years, p_wind(years), color='darkgreen', linestyle=':', alpha=0.5, linewidth=1)

z_hydro = np.polyfit(years, hydro_energy, 1)
p_hydro = np.poly1d(z_hydro)
ax1.plot(years, p_hydro(years), color='magenta', linestyle=':', alpha=0.5, linewidth=1)

z_total = np.polyfit(years, total_renewable, 1)
p_total = np.poly1d(z_total)
ax2.plot(years, p_total(years), color='darkred', linestyle=':', alpha=0.5, linewidth=1)

ax1.annotate('Solar Surprise!', xy=(2015, solar_energy[5]), xytext=(2013, 50),
             arrowprops=dict(facecolor='purple', arrowstyle='->'),
             fontsize=12, ha='center')

highlight_year = 2018
ax1.axvline(x=highlight_year, color='red', linestyle='--', linewidth=1, alpha=0.8)
ax1.text(highlight_year + 0.2, 250, 'Focus Point: 2018', color='red', fontsize=12, rotation=90)

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left', fontsize=12)

plt.tight_layout()
plt.show()