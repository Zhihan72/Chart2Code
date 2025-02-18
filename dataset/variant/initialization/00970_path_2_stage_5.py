import matplotlib.pyplot as plt

combined_yield = [45, 50, 55, 47, 52, 60, 58, 54, 49, 53]

fig, ax = plt.subplots(figsize=(8, 10))

box = ax.boxplot(combined_yield, vert=True, patch_artist=True,
                 flierprops=dict(marker='x', color='blue', alpha=0.6),
                 boxprops=dict(color='orange', linewidth=2),
                 whiskerprops=dict(color='red', linestyle='-'),
                 capprops=dict(color='red'),
                 medianprops=dict(color='darkblue', linewidth=1.5),
                 notch=False)

for patch in box['boxes']:
    patch.set_facecolor('lightcyan')

ax.grid(True, which='both', linestyle=':', linewidth=0.75, alpha=0.9)

plt.tight_layout()
plt.show()