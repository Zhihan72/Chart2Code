import matplotlib.pyplot as plt
import numpy as np

countries = ['USA', 'Germany', 'China', 'India', 'Brazil']
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

# Update the figure to accommodate an additional subplot
fig, axes = plt.subplots(4, 1, figsize=(14, 22))
fig.subplots_adjust(hspace=0.4)

# Horizontal Bar chart for Solar Energy
for i in range(len(years)):
    axes[0].barh(
        countries, solar_energy[:, i], label=years[i]
    )
axes[0].set_title('Annual Solar Energy Production (2017-2021)', fontsize=16, fontweight='bold')
axes[0].set_xlabel('Energy (TWh)', fontsize=12)
axes[0].legend(title='Years', fontsize=10, loc='upper right', bbox_to_anchor=(1, 1), title_fontsize='12')
axes[0].grid(axis='x', linestyle='--', alpha=0.7)

# Horizontal Bar chart for Wind Energy
for i in range(len(years)):
    axes[1].barh(
        countries, wind_energy[:, i], label=years[i]
    )
axes[1].set_title('Annual Wind Energy Production (2017-2021)', fontsize=16, fontweight='bold')
axes[1].set_xlabel('Energy (TWh)', fontsize=12)
axes[1].legend(title='Years', fontsize=10, loc='upper right', bbox_to_anchor=(1, 1), title_fontsize='12')
axes[1].grid(axis='x', linestyle='--', alpha=0.7)

# Horizontal Bar chart for Hydro Energy
for i in range(len(years)):
    axes[2].barh(
        countries, hydro_energy[:, i], label=years[i]
    )
axes[2].set_title('Annual Hydro Energy Production (2017-2021)', fontsize=16, fontweight='bold')
axes[2].set_xlabel('Energy (TWh)', fontsize=12)
axes[2].legend(title='Years', fontsize=10, loc='upper right', bbox_to_anchor=(1, 1), title_fontsize='12')
axes[2].grid(axis='x', linestyle='--', alpha=0.7)

# Horizontal Bar chart for Geothermal Energy
for i in range(len(years)):
    axes[3].barh(
        countries, geothermal_energy[:, i], label=years[i]
    )
axes[3].set_title('Annual Geothermal Energy Production (2017-2021)', fontsize=16, fontweight='bold')
axes[3].set_xlabel('Energy (TWh)', fontsize=12)
axes[3].legend(title='Years', fontsize=10, loc='upper right', bbox_to_anchor=(1, 1), title_fontsize='12')
axes[3].grid(axis='x', linestyle='--', alpha=0.7)

# Adjust layout for better visibility
plt.tight_layout()

# Display the plot
plt.show()