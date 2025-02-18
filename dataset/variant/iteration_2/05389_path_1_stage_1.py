import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

bird_species = ['Storks', 'Eagles', 'Herons', 'Flamingos', 'Sparrows', 'Hawks', 'Pelicans', 'Swans']

storks_altitude = np.array([1500, 1600, 1400, 1450, 1550, 1650, 1400, 1500, 1550, 1600, 1500, 1400])
eagles_altitude = np.array([3000, 3100, 2900, 2950, 3050, 3150, 2900, 3000, 3050, 3100, 3000, 2900])
herons_altitude = np.array([800, 850, 750, 770, 820, 860, 750, 800, 820, 850, 800, 750])
flamingos_altitude = np.array([1300, 1350, 1250, 1270, 1320, 1370, 1250, 1300, 1320, 1350, 1300, 1250])
sparrows_altitude = np.array([500, 550, 450, 470, 520, 560, 450, 500, 520, 550, 500, 450])
hawks_altitude = np.array([2800, 2900, 2700, 2750, 2850, 2950, 2700, 2800, 2850, 2900, 2800, 2700])
pelicans_altitude = np.array([2000, 2100, 1900, 1950, 2050, 2150, 1900, 2000, 2050, 2100, 2000, 1900])
swans_altitude = np.array([1700, 1800, 1600, 1650, 1750, 1850, 1600, 1700, 1750, 1800, 1700, 1600])

data = [storks_altitude, eagles_altitude, herons_altitude, 
        flamingos_altitude, sparrows_altitude, hawks_altitude, 
        pelicans_altitude, swans_altitude]

colors = ['#FF6347', '#1E90FF', '#32CD32', '#FFD700', '#8A2BE2', '#FF4500', '#2E8B57', '#8B0000']

fig, ax = plt.subplots(2, 1, figsize=(12, 10))

for i, altitude in enumerate(data):
    sns.kdeplot(altitude, ax=ax[0], label=bird_species[i], color=colors[i], shade=True, alpha=0.6)

ax[0].set_title('Density Estimation of Flight Altitudes\nDuring the Great Migration Over Serengeti', fontsize=16, fontweight='bold', pad=20)
ax[0].set_xlabel('Flight Altitude (meters)', fontsize=12)
ax[0].set_ylabel('Density', fontsize=12)
ax[0].legend(loc='upper right')

# Plotting horizontal box plots
box = ax[1].boxplot(data, patch_artist=True, notch=True, vert=False, showmeans=True, labels=bird_species)

for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    
for median, mean in zip(box['medians'], box['means']):
    median.set_color('black')
    median.set_linewidth(2)
    mean.set_markerfacecolor('red')
    mean.set_markeredgecolor('red')

ax[1].set_title('Distribution of Flight Altitudes\nFor Different Bird Species', fontsize=16, fontweight='bold', pad=20)
ax[1].set_xlabel('Flight Altitude (meters)', fontsize=12)
ax[1].set_ylabel('Bird Species', fontsize=12)
ax[1].set_yticklabels(bird_species)

# Adding legend
median_legend = plt.Line2D([0], [0], color='black', lw=2, label='Median')
mean_legend = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=8, label='Mean')
ax[1].legend(handles=[median_legend, mean_legend], loc='upper left')

plt.tight_layout()
plt.show()