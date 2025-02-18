import matplotlib.pyplot as plt
import numpy as np

seasons = ['Cold Breeze', 'Falling Leaves', 'Fresh Green', 'Hot Sun']

rainfall_data = {
    'Meadow of Twilight': [175, 125, 145, 115],
    'Falls of Mist': [150, 110, 140, 120],
    'Pines Whisper': [180, 140, 135, 125],
    'Glen of Fae': [160, 120, 130, 110],
    'Grove of Enchant': [170, 130, 150, 140],
    'Valley of Echoes': [165, 135, 155, 145],  # New data series
    'Forest of Secrets': [155, 115, 135, 125]  # New data series
}

season_data = np.array(list(rainfall_data.values()))

fig, ax = plt.subplots(figsize=(14, 8))

boxplots = ax.boxplot(season_data, notch=False, vert=False, patch_artist=True, labels=seasons)

single_color = '#41b6c4'

for patch in boxplots['boxes']:
    patch.set_facecolor(single_color)
    patch.set_alpha(0.9)
    patch.set_edgecolor('grey')

for median in boxplots['medians']:
    median.set_color('darkred')
    median.set_linewidth(2)

ax.set_title('Rainfall Variations of Enchanted Realms\nAcross the Mysterious Seasons', fontsize=18, fontweight='bold')
ax.set_xlabel('Rainfall (mm)', fontsize=14)
ax.set_ylabel('Seasons', fontsize=14)
ax.yaxis.grid(True, linestyle='-.', color='blue', alpha=0.5)

location_labels = rainfall_data.keys()
for line, label in zip(boxplots['medians'], location_labels):
    line.set_label(label)

ax.legend(title='Mystical Locations', fontsize=11, loc='upper right')

plt.tight_layout()
plt.show()