import matplotlib.pyplot as plt

# Single group of data
populations_yellowstone = [35, 40, 45, 42, 38, 44, 47, 48, 43, 45]

plt.figure(figsize=(6, 8))
plt.boxplot(populations_yellowstone, vert=True, patch_artist=True, notch=True,
            boxprops=dict(facecolor='lightgreen', color='darkgreen', alpha=0.6),
            capprops=dict(color='darkgreen'),
            whiskerprops=dict(color='darkgreen'),
            flierprops=dict(marker='o', color='red', alpha=0.5),
            medianprops=dict(color='gold', linewidth=2))

plt.ylabel('Tiger Population Size', fontsize=14)
plt.xticks([1], ['Yellowstone'], fontsize=12)
plt.title('Tiger Population Dynamics in Yellowstone', fontsize=16, weight='bold', pad=20)

plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

plt.show()