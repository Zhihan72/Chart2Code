import matplotlib.pyplot as plt
import numpy as np

steps_data = [
    [8500, 8700, 7800, 9000, 8800, 8900, 8600, 9100, 9200, 8450],
    [4500, 4200, 4100, 4600, 4700, 4900, 4300, 4800, 4400, 4550],
    [9500, 9600, 9400, 9300, 9200, 9800, 9900, 9700, 9350, 9600],
    [7000, 7500, 7200, 7100, 7350, 7600, 7800, 7400, 7500, 7350],
    [5000, 4800, 4700, 5100, 5200, 5400, 4550, 4900, 5050, 5250]
]

fig, ax = plt.subplots(figsize=(10, 8))
box = ax.boxplot(steps_data, vert=False, patch_artist=True, notch=True, whis=1.5)  # Ensure horizontal box

colors = ['#FFDDC1', '#FFD6A5', '#FDFFB6', '#CAFFBF', '#9BF6FF']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_edgecolor('black')
    patch.set_linewidth(1.5)

for flier in box['fliers']:
    flier.set(marker='o', color='red', alpha=0.5)

plt.tight_layout()
plt.show()