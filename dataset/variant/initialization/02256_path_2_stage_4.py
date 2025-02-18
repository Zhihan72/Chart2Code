import matplotlib.pyplot as plt
import numpy as np

ai_software_growth = [22, 24, 23, 25, 27, 30, 28, 25, 27, 26, 29, 31,
                      28, 32, 29, 30, 31, 33, 30, 31, 35, 29, 34, 37, 36, 35, 33, 32, 36, 37, 38, 39]
ai_hardware_growth = [18, 19, 22, 20, 21, 25, 24, 22, 23, 24, 20, 26,
                      27, 29, 22, 28, 30, 26, 28, 25, 27, 29, 31, 30, 32, 29, 31, 28, 30, 33, 29, 27]

cyber_network_growth = [10, 12, 11, 15, 18, 17, 16, 20, 22, 25, 27, 28,
                        26, 23, 22, 24, 26, 25, 23, 21, 25, 28, 29, 30, 31, 29, 32, 30, 31, 28, 26, 27]
cyber_app_growth = [9, 11, 13, 14, 16, 20, 17, 18, 20, 21, 24, 26,
                    27, 28, 29, 30, 28, 27, 26, 29, 32, 31, 33, 30, 29, 31, 32, 33, 30, 28, 29, 27]

edtech_k12_growth = [8, 10, 12, 15, 18, 16, 13, 17, 19, 22, 20, 21,
                     23, 25, 24, 26, 28, 30, 27, 25, 29, 31, 34, 32, 28, 30, 29, 33, 31, 35, 33, 32]
edtech_higher_growth = [7, 11, 14, 16, 19, 21, 23, 18, 20, 24, 27, 25,
                        22, 28, 29, 30, 32, 34, 33, 35, 37, 36, 31, 33, 38, 39, 34, 31, 30, 29, 32, 35]

healthtech_devices_growth = [25, 26, 24, 28, 29, 30, 27, 31, 34, 32, 30, 33,
                             36, 37, 35, 34, 38, 40, 39, 37, 35, 36, 31, 33, 32, 37, 39, 38, 36, 34, 32, 33]
healthtech_software_growth = [27, 29, 30, 28, 31, 32, 33, 35, 37, 36, 35, 38,
                              39, 37, 36, 35, 34, 33, 32, 31, 30, 29, 34, 32, 35, 37, 38, 39, 36, 35, 33, 31]

growth_data = [
    ai_software_growth, ai_hardware_growth,
    cyber_network_growth, cyber_app_growth,
    edtech_k12_growth, edtech_higher_growth,
    healthtech_devices_growth, healthtech_software_growth
]

fig, ax = plt.subplots(figsize=(14, 10))

colors = ['skyblue', 'palegreen', 'lightseagreen', 'lightcoral', 'plum', 'lavender', 'lightyellow', 'peachpuff']

bp = ax.boxplot(growth_data, vert=False, patch_artist=True,
                boxprops=dict(linestyle='--', color='gray'),
                whiskerprops=dict(linestyle=':', color='black'),
                capprops=dict(color='purple'),
                medianprops=dict(color='orange', linewidth=3),
                flierprops=dict(marker='s', color='green', markersize=10, alpha=0.6))

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

parts = ax.violinplot(growth_data, showmeans=True, showmedians=True, widths=0.5)
for pc in parts['bodies']:
    pc.set_facecolor('lightgray')
    pc.set_edgecolor('yellow')
    pc.set_alpha(0.3)

means = [np.mean(data) for data in growth_data]
ax.scatter(means, range(1, len(means) + 1), color='blue', zorder=3, marker='^')

ax.yaxis.grid(False)
ax.xaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

plt.show()