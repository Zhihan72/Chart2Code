import matplotlib.pyplot as plt

# Multiple groups of data
populations_yellowstone = [35, 40, 45, 42, 38, 44, 47, 48, 43, 45]
populations_glacier = [30, 33, 37, 39, 35, 36, 40, 41, 39, 34]
populations_yosemite = [25, 28, 29, 31, 30, 27, 33, 32, 29, 28]

plt.figure(figsize=(8, 8))
plt.boxplot([populations_yellowstone, populations_glacier, populations_yosemite], vert=True, patch_artist=True, notch=True,
            boxprops=dict(facecolor='lightgreen', color='darkgreen', alpha=0.6),
            capprops=dict(color='darkgreen'),
            whiskerprops=dict(color='darkgreen'),
            flierprops=dict(marker='o', color='red', alpha=0.5),
            medianprops=dict(color='gold', linewidth=2))

plt.ylabel('Tiger Population Size', fontsize=14)
plt.xticks([1, 2, 3], ['Yellowstone', 'Glacier', 'Yosemite'], fontsize=12)
plt.title('Tiger Population Dynamics Across Parks', fontsize=16, weight='bold', pad=20)

plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

plt.show()