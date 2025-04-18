import matplotlib.pyplot as plt
import numpy as np

years = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
xenia_height = np.array([8, 12, 20, 25, 30, 37, 40, 48, 55, 60])
xenia_diameter = np.array([2, 3, 5, 7, 9, 12, 13, 16, 19, 21])
zog_height = np.array([6, 10, 14, 18, 23, 28, 35, 37, 40, 42])
zog_diameter = np.array([1, 2, 3, 4, 6, 8, 10, 11, 12, 13])
trogar_height = np.array([5, 9, 13, 17, 21, 25, 29, 32, 35, 39])
trogar_diameter = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

ax1.scatter(xenia_height, xenia_diameter, color='green', edgecolor='black', alpha=0.7, s=100, label='Planet X')
ax1.scatter(zog_height, zog_diameter, color='red', edgecolor='black', alpha=0.7, s=100, label='Plant Z')
ax1.scatter(trogar_height, trogar_diameter, color='blue', edgecolor='black', alpha=0.7, s=100, label='World T')

ax1.set_title('Intergalactic Flora Beneath Suns', fontsize=14, fontweight='bold')
ax1.set_xlabel('Height of Flora (cm)', fontsize=12)
ax1.set_ylabel('Width of Greenery (cm)', fontsize=12)
ax1.legend(title='Cosmic Realms', fontsize=10)
ax1.grid(linestyle='--', alpha=0.7)

for i in range(0, len(years), 2):
    ax1.annotate(f'Cycle {years[i]}', (xenia_height[i], xenia_diameter[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
    ax1.annotate(f'Cycle {years[i]}', (zog_height[i], zog_diameter[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
    ax1.annotate(f'Cycle {years[i]}', (trogar_height[i], trogar_diameter[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

average_heights = [np.mean(xenia_height), np.mean(zog_height), np.mean(trogar_height)]
average_diameters = [np.mean(xenia_diameter), np.mean(zog_diameter), np.mean(trogar_diameter)]

bar_width = 0.35
index = np.arange(len(average_heights))

bars1 = ax2.bar(index, average_heights, bar_width, label='Height Mean (cm)', color='r', alpha=0.7)
bars2 = ax2.bar(index + bar_width, average_diameters, bar_width, label='Diameter Mean (cm)', color='b', alpha=0.7)

ax2.set_title('Mean Sizes of Extraterrestrial Vegetation', fontsize=14, fontweight='bold')
ax2.set_xlabel('Interplanetary Zones', fontsize=12)
ax2.set_ylabel('Scale (cm)', fontsize=12)
ax2.set_xticks(index + bar_width / 2)
ax2.set_xticklabels(['Gal X', 'Terr Z', 'Planet T'])
ax2.legend()

plt.tight_layout()
plt.show()