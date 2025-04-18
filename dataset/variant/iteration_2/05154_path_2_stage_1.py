import matplotlib.pyplot as plt
import numpy as np

techniques = ['Sweep', 'Blast', 'Precision', 'Eco Mode']
lawns = ['Lawn A', 'Lawn B', 'Lawn C']

sweep_data = [
    [20, 22, 23, 21, 24, 25],     # Lawn A
    [18, 20, 18, 21, 19, 22],     # Lawn B
    [25, 27, 26, 28, 26, 29]      # Lawn C
]

blast_data = [
    [15, 16, 14, 17, 15, 16],     # Lawn A
    [14, 13, 15, 14, 13, 16],     # Lawn B
    [17, 16, 18, 17, 15, 19]      # Lawn C
]

precision_data = [
    [25, 26, 24, 27, 25, 26],     # Lawn A
    [23, 22, 24, 23, 22, 25],     # Lawn B
    [28, 29, 27, 30, 28, 29]      # Lawn C
]

eco_mode_data = [
    [30, 32, 28, 31, 30, 33],     # Lawn A
    [28, 27, 29, 28, 27, 30],     # Lawn B
    [35, 34, 32, 36, 33, 37]      # Lawn C
]

box_data = [
    sweep_data[0], blast_data[0], precision_data[0], eco_mode_data[0],  
    sweep_data[1], blast_data[1], precision_data[1], eco_mode_data[1],  
    sweep_data[2], blast_data[2], precision_data[2], eco_mode_data[2]
]

positions = [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14]

fig, ax = plt.subplots(figsize=(14, 8))

boxprops = dict(facecolor='#AEDFF7', color='blue')
whiskerprops = dict(color='blue', linestyle='--')
capprops = dict(color='blue')
flierprops = dict(markerfacecolor='red', marker='o', markersize=8, linestyle='none')
medianprops = dict(color='darkblue', linewidth=2)

ax.boxplot(box_data, positions=positions, patch_artist=True, notch=True,
           boxprops=boxprops, whiskerprops=whiskerprops,
           capprops=capprops, flierprops=flierprops,
           medianprops=medianprops)

ax.set_xticks([2.5, 7.5, 12.5])
ax.set_xticklabels(lawns, fontsize=12)
ax.set_xlabel("Lawns", fontsize=14)
ax.set_ylabel("Time Taken (minutes)", fontsize=14)

plt.title("Effectiveness of Leaf Blowing Techniques on Different Lawns", fontsize=16, fontweight='bold')

plt.tight_layout()

plt.show()