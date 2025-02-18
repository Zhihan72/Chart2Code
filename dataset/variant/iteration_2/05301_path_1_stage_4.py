import matplotlib.pyplot as plt
import numpy as np

years = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
xenia_height = np.array([8, 12, 20, 25, 30, 37, 40, 48, 55, 60])
xenia_diameter = np.array([2, 3, 5, 7, 9, 12, 13, 16, 19, 21])
zog_height = np.array([6, 10, 14, 18, 23, 28, 35, 37, 40, 42])
zog_diameter = np.array([1, 2, 3, 4, 6, 8, 10, 11, 12, 13])
trogar_height = np.array([5, 9, 13, 17, 21, 25, 29, 32, 35, 39])
trogar_diameter = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
vornas_height = np.array([7, 11, 16, 22, 27, 34, 38, 41, 46, 49])
vornas_diameter = np.array([2, 3, 4, 5, 7, 9, 11, 13, 15, 16])

fig, ax1 = plt.subplots(figsize=(8, 8))

ax1.scatter(xenia_height, xenia_diameter, color='green', edgecolor='black', alpha=0.7, s=100, label='Planet X')
ax1.scatter(zog_height, zog_diameter, color='red', edgecolor='black', alpha=0.7, s=100, label='Plant Z')
ax1.scatter(trogar_height, trogar_diameter, color='blue', edgecolor='black', alpha=0.7, s=100, label='World T')
ax1.scatter(vornas_height, vornas_diameter, color='purple', edgecolor='black', alpha=0.7, s=100, label='Realm V')

ax1.set_title('Intergalactic Flora Beneath Suns', fontsize=14, fontweight='bold')
ax1.set_xlabel('Height of Flora (cm)', fontsize=12)
ax1.set_ylabel('Width of Greenery (cm)', fontsize=12)
ax1.legend(title='Cosmic Realms', fontsize=10)
ax1.grid(linestyle='--', alpha=0.7)

for i in range(0, len(years), 2):
    ax1.annotate(f'Cycle {years[i]}', (xenia_height[i], xenia_diameter[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
    ax1.annotate(f'Cycle {years[i]}', (zog_height[i], zog_diameter[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
    ax1.annotate(f'Cycle {years[i]}', (trogar_height[i], trogar_diameter[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
    ax1.annotate(f'Cycle {years[i]}', (vornas_height[i], vornas_diameter[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

plt.tight_layout()
plt.show()