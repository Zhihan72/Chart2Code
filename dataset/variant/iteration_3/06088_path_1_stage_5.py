import matplotlib.pyplot as plt
import numpy as np

seasons = ['Spr', 'Sum', 'Aut', 'Win']
rainfall_data = {
    'Glen': [160, 120, 130, 110],
    'Falls': [150, 110, 140, 120],
    'Grove': [170, 130, 150, 140],
    'Pines': [180, 140, 135, 125]
}

season_data = np.array(list(rainfall_data.values()))
fig, ax = plt.subplots(figsize=(14, 8))
boxplots = ax.boxplot(season_data, notch=True, vert=False, patch_artist=True, labels=seasons)

colors = ['#41b6c4', '#2c7fb8', '#253494', '#a1dab4']

for patch, color, median in zip(boxplots['boxes'], colors, boxplots['medians']):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
    patch.set_edgecolor('black')
    median.set_color('black')
    median.set_linewidth(1.5)

# Remove title, x/y labels, grids, and legend
plt.tight_layout()
plt.show()