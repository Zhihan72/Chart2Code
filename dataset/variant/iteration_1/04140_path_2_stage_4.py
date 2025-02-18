import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_energy = [130, 22, 265, 30, 45, 170, 15, 320, 68, 95, 215]
wind_energy = [250, 95, 290, 80, 340, 105, 215, 160, 120, 145, 185]
hydro_energy = [1025, 935, 900, 995, 1015, 950, 980, 920, 1035, 965, 1005]
geothermal_energy = [11, 39, 21, 12, 33, 28, 14, 24, 16, 18, 10]

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, solar_energy, marker='*', linestyle=':', color='#4682B4', linewidth=2, label='Solar')
ax.plot(years, wind_energy, marker='D', linestyle='--', color='#CD5C5C', linewidth=2, label='Wind')
ax.plot(years, hydro_energy, marker='x', linestyle='-.', color='#FFD700', linewidth=2, label='Water Energy')
ax.plot(years, geothermal_energy, marker='+', linestyle='-', color='#2E8B57', linewidth=2, label='Geo Energy')

plt.title('Renewables Expansion (2010-2020)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Timeline: Year', fontsize=14)
plt.ylabel('Generation Capacity (Gigawatts)', fontsize=14)
plt.grid(True, linestyle=':', alpha=0.8)
plt.legend(title='Sources of Power', title_fontsize='13', fontsize='12', loc='lower right')

ax.annotate('Growth Spike', xy=(2016, 18), xytext=(2013, 60), 
             arrowprops=dict(facecolor='grey', arrowstyle='->', lw=1.5), fontsize=12, color='darkblue')

plt.text(2010, 320, "Renewable energy surge due to\ninnovation and eco-policies.",
         fontsize=12, color='darkgrey', bbox=dict(facecolor='lightgrey', alpha=0.7))

plt.tight_layout()
plt.show()