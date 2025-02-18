import matplotlib.pyplot as plt
import numpy as np

cities = ['Metropolis', 'Gotham', 'Asgard']

flu_cases_data = {
    'Metropolis': [30, 25, 40, 35, 50, 60, 45, 55, 65, 70, 75, 80],
    'Gotham': [20, 18, 25, 28, 30, 35, 40, 45, 50, 55, 60, 65],
    'Asgard': [15, 10, 20, 25, 30, 35, 40, 45, 55, 60, 70, 75]
}

data_for_box = [flu_cases_data[city] for city in cities]

fig, ax = plt.subplots(figsize=(12, 7))

color = '#FFA07A'

box = ax.boxplot(data_for_box, patch_artist=True, notch=False, vert=False,
                 boxprops=dict(facecolor=color, color='green'),
                 whiskerprops=dict(color='green', linestyle='-.'),
                 capprops=dict(color='green', linestyle='-.'),
                 medianprops=dict(color='blue', linewidth=3),
                 flierprops=dict(markerfacecolor='purple', marker='x', markersize=8, alpha=0.4))

ax.set_title('Viral Cases Distribution (2023)', fontsize=17, fontweight='bold')
ax.set_xlabel('Number of Cases', fontsize=13)
ax.set_ylabel('Regions', fontsize=13)

ax.set_yticks(np.arange(1, len(cities) + 1))
ax.set_yticklabels(cities, fontsize=12)

ax.xaxis.grid(False)
ax.yaxis.grid(True, linestyle=':')

ax.legend(['Metropolis', 'Gotham', 'Asgard'], loc='upper left', fontsize=10)

plt.tight_layout()
plt.show()