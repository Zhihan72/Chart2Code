import matplotlib.pyplot as plt
import numpy as np

countries = ['USA', 'Ger', 'Chn', 'Ind', 'Bra']
years = ['2017', '2018', '2019', '2020', '2021']
solar_energy = np.array([
    [100, 110, 120, 130, 140], 
    [90, 100, 110, 120, 130], 
    [150, 160, 170, 180, 200], 
    [50, 55, 60, 65, 70], 
    [70, 75, 80, 85, 90]
])
wind_energy = np.array([
    [300, 310, 320, 330, 340], 
    [150, 160, 170, 180, 190], 
    [400, 420, 440, 460, 480], 
    [100, 110, 120, 130, 140], 
    [200, 210, 220, 230, 240]
])
hydro_energy = np.array([
    [800, 810, 820, 830, 850], 
    [700, 710, 720, 730, 740], 
    [600, 620, 640, 660, 680], 
    [550, 560, 570, 580, 590], 
    [500, 510, 520, 530, 540]
])
geothermal_energy = np.array([
    [20, 25, 30, 35, 40], 
    [15, 18, 20, 22, 25], 
    [50, 52, 54, 56, 58], 
    [8, 9, 10, 11, 12], 
    [5, 6, 7, 8, 9]
])

fig, axes = plt.subplots(2, 2, figsize=(14, 14))
fig.subplots_adjust(hspace=0.4, wspace=0.4)

# Solar Energy
for i in range(len(years)):
    axes[0, 0].barh(countries, solar_energy[:, i])
axes[0, 0].set_title('Solar Energy (2017-21)', fontsize=16, fontweight='bold')
axes[0, 0].set_xlabel('Energy (TWh)', fontsize=12)

# Wind Energy
for i in range(len(years)):
    axes[0, 1].barh(countries, wind_energy[:, i])
axes[0, 1].set_title('Wind Energy (2017-21)', fontsize=16, fontweight='bold')
axes[0, 1].set_xlabel('Energy (TWh)', fontsize=12)

# Hydro Energy
for i in range(len(years)):
    axes[1, 0].barh(countries, hydro_energy[:, i])
axes[1, 0].set_title('Hydro Energy (2017-21)', fontsize=16, fontweight='bold')
axes[1, 0].set_xlabel('Energy (TWh)', fontsize=12)

# Geothermal Energy
for i in range(len(years)):
    axes[1, 1].barh(countries, geothermal_energy[:, i])
axes[1, 1].set_title('Geo Energy (2017-21)', fontsize=16, fontweight='bold')
axes[1, 1].set_xlabel('Energy (TWh)', fontsize=12)

plt.tight_layout()
plt.show()