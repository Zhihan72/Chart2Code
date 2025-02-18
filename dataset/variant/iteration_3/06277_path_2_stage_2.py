import matplotlib.pyplot as plt
import numpy as np

countries = ['USA', 'GER', 'CHN', 'IND', 'BRA']
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

# Plot setup
fig, axes = plt.subplots(3, 1, figsize=(14, 18))
fig.subplots_adjust(hspace=0.4)

# Define a shuffled color list
shuffled_colors = ['#1f77b4',  # Original color for USA
                   '#ff7f0e',  # Original color for GER
                   '#2ca02c',  # Original color for CHN
                   '#d62728',  # Original color for IND
                   '#9467bd']  # Original color for BRA

# Solar Energy Plot
for i in range(len(countries)):
    axes[0].bar(years, solar_energy[i], label=countries[i], color=shuffled_colors[i])
axes[0].set_title('Solar Energy (2017-2021)', fontsize=16, fontweight='bold')
axes[0].set_ylabel('TWh', fontsize=12)
axes[0].legend(title='Country', fontsize=10, loc='upper left', bbox_to_anchor=(1, 1), title_fontsize='12')
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

# Wind Energy Plot
for i in range(len(countries)):
    axes[1].bar(years, wind_energy[i], label=countries[i], color=shuffled_colors[(i+2)%5])
axes[1].set_title('Wind Energy (2017-2021)', fontsize=16, fontweight='bold')
axes[1].set_ylabel('TWh', fontsize=12)
axes[1].legend(title='Country', fontsize=10, loc='upper left', bbox_to_anchor=(1, 1), title_fontsize='12')
axes[1].grid(axis='y', linestyle='--', alpha=0.7)

# Hydro Energy Plot
for i in range(len(countries)):
    axes[2].bar(years, hydro_energy[i], label=countries[i], color=shuffled_colors[(i+1)%5])
axes[2].set_title('Hydro Energy (2017-2021)', fontsize=16, fontweight='bold')
axes[2].set_xlabel('Year', fontsize=12)
axes[2].set_ylabel('TWh', fontsize=12)
axes[2].legend(title='Country', fontsize=10, loc='upper left', bbox_to_anchor=(1, 1), title_fontsize='12')
axes[2].grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()