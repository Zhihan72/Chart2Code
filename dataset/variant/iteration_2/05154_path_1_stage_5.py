import matplotlib.pyplot as plt

techniques = ['Sweep', 'Blast', 'Prec.']
lawns = ['A', 'B', 'C']

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

box_data = [
    sweep_data[0], blast_data[0], precision_data[0],
    sweep_data[1], blast_data[1], precision_data[1],
    sweep_data[2], blast_data[2], precision_data[2]
]

positions = [1, 2, 3, 5, 6, 7, 9, 10, 11]

fig, ax = plt.subplots(figsize=(14, 8))

boxprops = dict(facecolor='#CCE8FF', color='darkblue')
whiskerprops = dict(color='darkblue', linestyle='-.')
capprops = dict(color='darkblue')
flierprops = dict(markerfacecolor='#FF6666', marker='x', markersize=10, linestyle='none')
medianprops = dict(color='#FFA500', linewidth=3)

ax.boxplot(box_data, positions=positions, patch_artist=True, notch=True,
           boxprops=boxprops, whiskerprops=whiskerprops,
           capprops=capprops, flierprops=flierprops,
           medianprops=medianprops, vert=False)

ax.set_yticks([2, 6, 10])
ax.set_yticklabels(lawns, fontsize=12)
ax.set_ylabel("Lawns", fontsize=14)
ax.set_xlabel("Time (min)", fontsize=14)

plt.title("Tech Effectiveness on Lawns", fontsize=16, fontweight='bold')
ax.yaxis.grid(True, linestyle='-', linewidth=1, alpha=0.5)

colors = ['#CCE8FF', '#FFD700', '#98FB98']
patches = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
plt.legend(patches, techniques, loc='upper left', fontsize=12, title="Technologies")

plt.tight_layout()
plt.show()