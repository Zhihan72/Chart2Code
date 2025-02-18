import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_energy = [15, 22, 30, 45, 68, 95, 130, 170, 215, 265, 320]
wind_energy = [80, 95, 105, 120, 145, 160, 185, 215, 250, 290, 340]
hydro_energy = [900, 920, 935, 950, 965, 980, 995, 1005, 1015, 1025, 1035]
geothermal_energy = [10, 11, 12, 14, 16, 18, 21, 24, 28, 33, 39]

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, solar_energy, marker='o', linestyle='-', color='#FFA07A', linewidth=2, label='Solar')
ax.plot(years, wind_energy, marker='s', linestyle='-', color='#8FBC8F', linewidth=2, label='Wind')
ax.plot(years, hydro_energy, marker='^', linestyle='-', color='#6495ED', linewidth=2, label='Hydro')
ax.plot(years, geothermal_energy, marker='D', linestyle='-', color='#FFD700', linewidth=2, label='Geo')

plt.title('Renewable Energy Trend (2010-20)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Capacity (GW)', fontsize=14)

plt.grid(True, linestyle='--', alpha=0.6)

plt.legend(title='Sources', title_fontsize='13', fontsize='12', loc='upper left')

ax.annotate('Growth', xy=(2016, 18), xytext=(2013, 60),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, color='darkred')

plt.text(2010, 320, "Rise in renewables\nvia tech and policy.",
         fontsize=12, color='grey', bbox=dict(facecolor='white', alpha=0.5))

plt.tight_layout()

plt.show()