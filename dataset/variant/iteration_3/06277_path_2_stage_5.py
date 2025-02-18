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

fig, axes = plt.subplots(3, 1, figsize=(14, 18))
fig.subplots_adjust(hspace=0.4)

new_shuffled_colors = ['#2ca02c', '#9467bd', '#d62728', '#1f77b4', '#ff7f0e']

# Sort function for descending order based on the energy values of 2021
def sort_data_by(values):
    sorted_indices = np.argsort(values)[::-1]
    return sorted_indices

# Wind Energy Plot - Moved to the top
sorted_indices = sort_data_by(wind_energy[:, -1])
for idx in sorted_indices:
    axes[0].bar(years, wind_energy[idx], label=countries[idx], color=new_shuffled_colors[idx], hatch='|')
axes[0].set_title('Wind Energy (2017-2021)', fontsize=16, fontweight='bold')
axes[0].set_ylabel('TWh', fontsize=12)
axes[0].legend(title='Country', fontsize=8, loc='lower right', bbox_to_anchor=(1, 0), title_fontsize='10')
axes[0].grid(axis='x', linestyle='-', alpha=0.5)

# Solar Energy Plot - Moved to the middle
sorted_indices = sort_data_by(solar_energy[:, -1])
for idx in sorted_indices:
    axes[1].bar(years, solar_energy[idx], label=countries[idx], color=new_shuffled_colors[idx], hatch='//')
axes[1].set_title('Solar Energy (2017-2021)', fontsize=16, fontweight='bold')
axes[1].set_ylabel('TWh', fontsize=12)
axes[1].legend(title='Country', fontsize=8, loc='lower right', bbox_to_anchor=(1, 0), title_fontsize='10')
axes[1].grid(axis='x', linestyle='-', alpha=0.5)

# Hydro Energy Plot - Remains at the bottom
sorted_indices = sort_data_by(hydro_energy[:, -1])
for idx in sorted_indices:
    axes[2].bar(years, hydro_energy[idx], label=countries[idx], color=new_shuffled_colors[idx], hatch='\\')
axes[2].set_title('Hydro Energy (2017-2021)', fontsize=16, fontweight='bold')
axes[2].set_xlabel('Year', fontsize=12)
axes[2].set_ylabel('TWh', fontsize=12)
axes[2].legend(title='Country', fontsize=8, loc='lower right', bbox_to_anchor=(1, 0), title_fontsize='10')
axes[2].grid(axis='x', linestyle='-', alpha=0.5)

plt.tight_layout()
plt.show()