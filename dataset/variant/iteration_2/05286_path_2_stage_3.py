import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2025)

solar_power = np.array([10, 12, 15, 18, 25, 35, 45, 60, 80, 100, 120, 140, 165, 190, 215, 240, 275, 300, 340, 400, 450, 500, 550, 600, 650])
wind_power = np.array([5, 8, 12, 20, 30, 45, 55, 80, 110, 150, 200, 250, 300, 350, 400, 460, 520, 600, 700, 800, 900, 1000, 1100, 1150, 1200])
hydro_power = np.array([180, 182, 185, 188, 190, 195, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 275, 280])
geothermal = np.array([30, 32, 34, 37, 40, 45, 50, 55, 60, 70, 80, 90, 95, 100, 110, 120, 130, 140, 150, 155, 160, 165, 170, 172, 175])
bioenergy = np.array([50, 52, 55, 58, 63, 70, 75, 80, 90, 100, 110, 125, 130, 135, 140, 145, 150, 155, 170, 180, 190, 195, 200, 205, 210])
wave_energy = np.array([0, 0, 0, 0, 0, 0, 0, 2, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 85, 100, 120, 140, 160, 180])
tidal_energy = np.array([1, 2, 3, 3, 4, 5, 6, 7, 8, 10, 12, 13, 15, 17, 19, 21, 24, 27, 30, 35, 40, 45, 50, 55, 60])

energy_data = np.vstack([solar_power, wind_power, hydro_power, geothermal, bioenergy, wave_energy, tidal_energy])

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Hydro', 'Geothermal', 'Bioenergy', 'Wave', 'Tidal'],
             colors=['#ffd700', '#1e90ff', '#32cd32', '#ff7f50', '#9370db', '#00ced1', '#4682b4'], alpha=0.7, edgecolor='darkgrey', linewidth=1.5)

ax.set_title('Renewable Energy Growth (2000-2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Adoption Level', fontsize=12)

ax.legend(loc='upper right', fontsize=10, title='Energy Types', frameon=True, shadow=True)

ax.grid(linestyle='-', linewidth=0.5, alpha=0.4)

plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 1301, 100))

ax.annotate('Solar Boom', xy=(2010, 150), xytext=(2005, 250),
            arrowprops=dict(arrowstyle='wedge', color='darkgoldenrod', lw=1.5), fontsize=10, color='darkgoldenrod')

ax.annotate('Wind Breakthrough', xy=(2015, 300), xytext=(2013, 600),
            arrowprops=dict(arrowstyle='fancy', connectionstyle='arc3', color='blue', lw=1.5),
            fontsize=10, color='blue')

description_box = dict(boxstyle='round', facecolor='white', alpha=0.5)
description = ("The advance in renewable energy tech\n"
               "is highlighted by policy and innovation impacts.")
ax.text(0.02, 0.97, description, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', bbox=description_box)

plt.tight_layout()
plt.show()