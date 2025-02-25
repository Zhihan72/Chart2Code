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

colors = ['#FF6347', '#4682B4', '#3CB371', '#FFA07A', '#9370DB', '#FFD700']  # Different colors for each box

fig, ax = plt.subplots(figsize=(12, 6))

box = ax.boxplot(data, patch_artist=True, notch=False, vert=False, showmeans=True, labels=bird_species, flierprops=dict(marker='x', color='gray', markersize=9))

for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

for median, mean in zip(box['medians'], box['means']):
    median.set_color('grey')
    median.set_linewidth(1.5)
    mean.set_markerfacecolor('blue')
    mean.set_markeredgecolor('blue')

ax.grid(True, linestyle='--', alpha=0.7)  # Adding dashed gridlines

ax.set_title('Flight Altitude Distribution\nAcross Bird Species', fontsize=14, fontweight='medium', pad=15)
ax.set_xlabel('Altitude (meters)', fontsize=11)
ax.set_ylabel('Bird Species', fontsize=11)

mean_legend = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=8, label='Mean')
ax.legend(handles=[mean_legend], loc='lower right', frameon=False)  # Removed the median legend for simplicity

plt.tight_layout()
plt.show()