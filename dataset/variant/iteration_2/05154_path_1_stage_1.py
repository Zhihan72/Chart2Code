import matplotlib.pyplot as plt

techniques = ['Sweep', 'Blast', 'Precision', 'Eco Mode']
lawns = ['Lawn A', 'Lawn B', 'Lawn C']

sweep_data = [
    [20, 22, 23, 21, 24, 25],
    [18, 20, 18, 21, 19, 22],
    [25, 27, 26, 28, 26, 29]
]

blast_data = [
    [15, 16, 14, 17, 15, 16],
    [14, 13, 15, 14, 13, 16],
    [17, 16, 18, 17, 15, 19]
]

precision_data = [
    [25, 26, 24, 27, 25, 26],
    [23, 22, 24, 23, 22, 25],
    [28, 29, 27, 30, 28, 29]
]

eco_mode_data = [
    [30, 32, 28, 31, 30, 33],
    [28, 27, 29, 28, 27, 30],
    [35, 34, 32, 36, 33, 37]
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
           medianprops=medianprops, vert=False)

ax.set_yticks([2.5, 7.5, 12.5])
ax.set_yticklabels(lawns, fontsize=12)
ax.set_ylabel("Lawns", fontsize=14)
ax.set_xlabel("Time Taken (minutes)", fontsize=14)

plt.title("Effectiveness of Leaf Blowing Techniques on Different Lawns", fontsize=16, fontweight='bold')
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

colors = ['#AEDFF7', '#FF9999', '#99FF99', '#FFFF99']
patches = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
plt.legend(patches, techniques, loc='upper right', fontsize=12, title="Techniques")

plt.tight_layout()
plt.show()