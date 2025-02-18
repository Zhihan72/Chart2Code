import matplotlib.pyplot as plt

combined_yield = [45, 50, 55, 47, 52, 60, 58, 54, 49, 53]

fig, ax = plt.subplots(figsize=(8, 10))

box = ax.boxplot(combined_yield, vert=True, patch_artist=True,
                 flierprops=dict(marker='o', color='red', alpha=0.5),
                 boxprops=dict(color='darkblue', linewidth=1.5),
                 whiskerprops=dict(color='blue', linestyle='--'),
                 capprops=dict(color='blue'),
                 medianprops=dict(color='orange', linewidth=2),
                 notch=True)

for patch in box['boxes']:
    patch.set_facecolor('skyblue')

ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()