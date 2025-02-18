import matplotlib.pyplot as plt

mars_yields = [20, 23, 21, 19, 25, 22, 24, 23, 20, 22, 21, 24]
venus_yields = [18, 22, 19, 17, 23, 20, 21, 20, 18, 21, 19, 22]
jupiter_yields = [21, 24, 20, 18, 26, 23, 25, 22, 21, 23, 22, 25]

data = [mars_yields, venus_yields, jupiter_yields]

plt.figure(figsize=(9, 7))
box = plt.boxplot(data, vert=True, patch_artist=True, notch=True, whis=1.5)

colors = ['#FF9999', '#66B3FF', '#99FF99']  # Changed order of colors
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

for flier in box['fliers']:
    flier.set(marker='x', color='red', alpha=0.7)

for median in box['medians']:
    median.set(color='purple', linestyle='-', linewidth=2)

plt.grid(axis='x', linestyle=':', alpha=0.5)
plt.tight_layout()
plt.show()