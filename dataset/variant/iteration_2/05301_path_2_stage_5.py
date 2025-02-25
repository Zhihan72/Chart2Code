import matplotlib.pyplot as plt
import numpy as np

years = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

xenia_height = np.array([8, 12, 20, 25, 30, 37, 40, 48, 55, 60])
xenia_diameter = np.array([2, 3, 5, 7, 9, 12, 13, 16, 19, 21])

trogar_height = np.array([5, 9, 13, 17, 21, 25, 29, 32, 35, 39])
trogar_diameter = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 16))

ax1.scatter(xenia_height, xenia_diameter, color='orange', edgecolor='blue', alpha=0.9, s=120, marker='s', label='Xenia')
ax1.scatter(trogar_height, trogar_diameter, color='purple', edgecolor='blue', alpha=0.9, s=120, marker='^', label='Trogar')

ax1.set_title('Extraterrestrial Flora Growth', fontsize=16)
ax1.set_xlabel('Height (cm)', fontsize=10)
ax1.set_ylabel('Diameter (cm)', fontsize=10)
ax1.legend(title='Alien Species', fontsize=12, loc='upper left')
ax1.grid(color='gray', linestyle='-', linewidth=1, alpha=0.3)

for i in range(1, len(years), 3):
    ax1.annotate(f'Y{years[i]}', (xenia_height[i], xenia_diameter[i]), textcoords="offset points", xytext=(10,-15), ha='center', fontsize=8)
    ax1.annotate(f'Y{years[i]}', (trogar_height[i], trogar_diameter[i]), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=8)

average_heights = [np.mean(xenia_height), np.mean(trogar_height)]
average_diameters = [np.mean(xenia_diameter), np.mean(trogar_diameter)]

bar_width = 0.3
index = np.arange(len(average_heights))

ax2.bar(index, average_heights, bar_width, label='Height (cm)', color='cyan', alpha=0.8, edgecolor='black')
ax2.bar(index + bar_width, average_diameters, bar_width, label='Diameter (cm)', color='magenta', alpha=0.8, edgecolor='black')

ax2.set_title('Mean Alien Plant Sizes', fontsize=16)
ax2.set_xlabel('Species', fontsize=10)
ax2.set_ylabel('Size (cm)', fontsize=10)
ax2.set_xticks(index + bar_width / 2)
ax2.set_xticklabels(['Xenia', 'Trogar'])
ax2.legend(loc='upper right', fontsize=9)
ax2.grid(axis='y', linestyle=':', linewidth=0.5, alpha=0.5)

plt.tight_layout()
plt.show()