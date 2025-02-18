import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_energy = [30, 68, 15, 95, 130, 170, 22, 265, 215, 320, 45]
wind_energy = [145, 80, 290, 105, 215, 340, 95, 120, 250, 160, 185]
hydro_energy = [980, 1015, 1005, 900, 920, 935, 950, 965, 995, 1025, 1035]
geothermal_energy = [12, 39, 16, 11, 21, 33, 24, 18, 14, 28, 10]

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, solar_energy, marker='o', linestyle='-', color='#FF6347', linewidth=2)   # Changed color to tomato
ax.plot(years, wind_energy, marker='s', linestyle='-', color='#4682B4', linewidth=2)   # Changed color to steelblue
ax.plot(years, hydro_energy, marker='^', linestyle='-', color='#20B2AA', linewidth=2)  # Changed color to lightseagreen
ax.plot(years, geothermal_energy, marker='D', linestyle='-', color='#DAA520', linewidth=2)  # Changed color to goldenrod

plt.title('Renewable Energy Trend (2010-20)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Capacity (GW)', fontsize=14)

ax.annotate('Growth', xy=(2016, 18), xytext=(2013, 60),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, color='darkred')

plt.text(2010, 320, "Rise in renewables\nvia tech and policy.",
         fontsize=12, color='grey', bbox=dict(facecolor='white', alpha=0.5))

plt.tight_layout()

plt.show()