import matplotlib.pyplot as plt
import numpy as np

noise_data = [
    [70, 75, 80, 72, 74, 78, 77, 73, 76, 79, 82, 74],
    [55, 60, 58, 57, 59, 61, 62, 56, 63, 64, 65, 57],
    [50, 52, 48, 49, 53, 51, 54, 47, 55, 57, 50, 52],
    [65, 68, 70, 72, 67, 66, 69, 71, 73, 74, 62, 65],
    [45, 48, 50, 47, 49, 46, 51, 52, 50, 53, 49, 48],
]

fig, ax = plt.subplots(figsize=(14, 8))
box = ax.boxplot(noise_data, vert=False, patch_artist=True, notch=True, whis=1.5)

# Manually shuffled colors:
colors = ['#20B2AA', '#FF6347', '#40E0D0', '#FFA07A', '#FFD700']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

for whisker in box['whiskers']:
    whisker.set(color='#8B8B8B', linewidth=1.5, linestyle='--')
for cap in box['caps']:
    cap.set(color='#8B8B8B', linewidth=1.5)
for median in box['medians']:
    median.set(color='black', linewidth=2)

for i, data in enumerate(noise_data, 1):
    x = data
    y = np.full_like(x, i) + np.random.normal(0, 0.04, size=len(x))
    ax.scatter(x, y, alpha=0.6, color=colors[i - 1], edgecolors='w', s=50)

acceptable_noise_level = 65
ax.axvline(acceptable_noise_level, color='r', linestyle='--', linewidth=1.5)

plt.show()