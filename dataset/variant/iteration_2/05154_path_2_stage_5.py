import matplotlib.pyplot as plt
import numpy as np

techniques = ['Fast Sweep', 'Crater', 'Accurate', 'Eco Friendly Mode', 'Silent Mode']
lawns = ['Garden Y', 'Field X', 'Plot Z', 'Park W']

sweep_data = [[20, 22, 23, 21, 24, 25], [18, 20, 18, 21, 19, 22], [25, 27, 26, 28, 26, 29], [22, 23, 24, 23, 22, 23]]
blast_data = [[15, 16, 14, 17, 15, 16], [14, 13, 15, 14, 13, 16], [17, 16, 18, 17, 15, 19], [16, 17, 16, 16, 16, 17]]
precision_data = [[25, 26, 24, 27, 25, 26], [23, 22, 24, 23, 22, 25], [28, 29, 27, 30, 28, 29], [26, 27, 26, 26, 26, 27]]
eco_mode_data = [[30, 32, 28, 31, 30, 33], [28, 27, 29, 28, 27, 30], [35, 34, 32, 36, 33, 37], [31, 32, 31, 31, 31, 32]]
silent_mode_data = [[10, 12, 11, 13, 12, 11], [9, 10, 8, 9, 10, 11], [11, 13, 12, 14, 13, 12], [12, 12, 12, 12, 12, 13]]

box_data = [
    sweep_data[0], blast_data[0], precision_data[0], eco_mode_data[0], silent_mode_data[0],
    sweep_data[1], blast_data[1], precision_data[1], eco_mode_data[1], silent_mode_data[1], 
    sweep_data[2], blast_data[2], precision_data[2], eco_mode_data[2], silent_mode_data[2], 
    sweep_data[3], blast_data[3], precision_data[3], eco_mode_data[3], silent_mode_data[3]
]

positions = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23]

fig, ax = plt.subplots(figsize=(14, 10))

boxprops = dict(facecolor='#F4A582', color='darkorange')
whiskerprops = dict(color='darkorange', linestyle='--')
capprops = dict(color='darkorange')
flierprops = dict(markerfacecolor='purple', marker='o', markersize=8, linestyle='none')
medianprops = dict(color='green', linewidth=2)

ax.boxplot(box_data, positions=positions, patch_artist=True, notch=True, vert=False,
           boxprops=boxprops, whiskerprops=whiskerprops,
           capprops=capprops, flierprops=flierprops,
           medianprops=medianprops)

ax.set_yticks([3, 9, 15, 21])
ax.set_yticklabels(lawns, fontsize=12)
ax.set_ylabel("Landscape Areas", fontsize=14)
ax.set_xlabel("Duration (minutes)", fontsize=14)

plt.title("Performance of Various Leaf Blowing Methods Across Areas", fontsize=16, fontweight='bold')

plt.tight_layout()
plt.show()