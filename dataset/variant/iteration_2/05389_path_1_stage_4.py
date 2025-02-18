import numpy as np
import matplotlib.pyplot as plt

bird_species = ['Storks', 'Eagles', 'Herons', 'Sparrows', 'Hawks', 'Pelicans']

storks_altitude = np.array([1500, 1600, 1400, 1450, 1550, 1650, 1400, 1500, 1550, 1600, 1500, 1400])
eagles_altitude = np.array([3000, 3100, 2900, 2950, 3050, 3150, 2900, 3000, 3050, 3100, 3000, 2900])
herons_altitude = np.array([800, 850, 750, 770, 820, 860, 750, 800, 820, 850, 800, 750])
sparrows_altitude = np.array([500, 550, 450, 470, 520, 560, 450, 500, 520, 550, 500, 450])
hawks_altitude = np.array([2800, 2900, 2700, 2750, 2850, 2950, 2700, 2800, 2850, 2900, 2800, 2700])
pelicans_altitude = np.array([2000, 2100, 1900, 1950, 2050, 2150, 1900, 2000, 2050, 2100, 2000, 1900])

data = [storks_altitude, eagles_altitude, herons_altitude, 
        sparrows_altitude, hawks_altitude, 
        pelicans_altitude]

color = '#1E90FF'  # Single color applied to all boxes

fig, ax = plt.subplots(figsize=(12, 6))

box = ax.boxplot(data, patch_artist=True, notch=True, vert=False, showmeans=True, labels=bird_species)

for patch in box['boxes']:
    patch.set_facecolor(color)

for median, mean in zip(box['medians'], box['means']):
    median.set_color('black')
    median.set_linewidth(2)
    mean.set_markerfacecolor('red')
    mean.set_markeredgecolor('red')

ax.set_title('Distribution of Flight Altitudes\nFor Different Bird Species', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Flight Altitude (meters)', fontsize=12)
ax.set_ylabel('Bird Species', fontsize=12)
ax.set_yticklabels(bird_species)

median_legend = plt.Line2D([0], [0], color='black', lw=2, label='Median')
mean_legend = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=8, label='Mean')
ax.legend(handles=[median_legend, mean_legend], loc='upper left')

plt.tight_layout()
plt.show()