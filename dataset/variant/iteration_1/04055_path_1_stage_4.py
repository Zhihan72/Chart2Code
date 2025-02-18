import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_energy = [90, 45, 250, 10, 180, 120, 25, 65, 150, 300, 220]  # Shuffled data points
wind_energy = [95, 60, 210, 40, 240, 145, 195, 75, 170, 280, 120]  # Shuffled data points
total_renewable = [s + w for s, w in zip(solar_energy, wind_energy)]

fig, ax1 = plt.subplots(figsize=(14, 9))

ax1.plot(years, solar_energy, color='darkorange', linestyle='-', linewidth=2, marker='D', label='Sunshine Power')
ax1.plot(years, wind_energy, color='royalblue', linestyle='-.', linewidth=2, marker='^', label='Breeze Power')

ax1.grid(True, linestyle='-.', linewidth=0.7, alpha=0.5)

ax2 = ax1.twinx()
ax2.plot(years, total_renewable, color='green', linestyle='--', linewidth=2, marker='*', label='Aggregate Green Energy')

ax1.set_title('Renewable Energy Growth: Solar & Wind\n(2010-2020)', fontsize=16, weight='bold')
ax1.set_xlabel('Timeline', fontsize=14)
ax1.set_ylabel('Solo Output (TWh)', fontsize=14, color='dimgray')
ax2.set_ylabel('Complete Output (TWh)', fontsize=14, color='dimgray')

z_solar = np.polyfit(years, solar_energy, 1)
p_solar = np.poly1d(z_solar)
ax1.plot(years, p_solar(years), color='darkorange', linestyle=':', alpha=0.7, linewidth=1)

z_wind = np.polyfit(years, wind_energy, 1)
p_wind = np.poly1d(z_wind)
ax1.plot(years, p_wind(years), color='royalblue', linestyle=':', alpha=0.7, linewidth=1)

z_total = np.polyfit(years, total_renewable, 1)
p_total = np.poly1d(z_total)
ax2.plot(years, p_total(years), color='green', linestyle=':', alpha=0.7, linewidth=1)

ax1.annotate('Solar Surge', xy=(2015, solar_energy[5]), xytext=(2013, 50),
             arrowprops=dict(facecolor='darkorange', arrowstyle='->'),
             fontsize=12, ha='center')

highlight_year = 2018
ax1.axvline(x=highlight_year, color='teal', linestyle='--', linewidth=1, alpha=0.8)
ax1.text(highlight_year + 0.2, 210, '2018 Highlight', color='teal', fontsize=12, rotation=90)

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left', fontsize=10, borderpad=1.5, shadow=True)

plt.tight_layout()
plt.show()