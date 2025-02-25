import matplotlib.pyplot as plt
import numpy as np

locations = ['City Center', 'Residential Area', 'Park', 'Industrial Zone', 'Suburbs']

# Manually shuffled data
noise_data = [
    [74, 70, 75, 72, 78, 77, 73, 76, 79, 82, 74, 80],
    [62, 60, 58, 57, 59, 61, 55, 56, 63, 64, 65, 57],
    [50, 54, 48, 49, 53, 51, 47, 52, 55, 57, 52, 50],
    [65, 68, 70, 66, 67, 72, 69, 71, 73, 74, 62, 65],
    [45, 48, 52, 47, 49, 51, 46, 50, 53, 50, 49, 48],
]

fig, ax = plt.subplots(figsize=(14, 8))
box = ax.boxplot(noise_data, vert=False, patch_artist=True, notch=True, whis=1.5)

single_color = '#FFA07A'
for patch in box['boxes']:
    patch.set_facecolor(single_color)
    patch.set_alpha(0.7)

for whisker in box['whiskers']:
    whisker.set(color='#8B8B8B', linewidth=1.5, linestyle='--')
for cap in box['caps']:
    cap.set(color='#8B8B8B', linewidth=1.5)
for median in box['medians']:
    median.set(color='black', linewidth=2)

for i, data in enumerate(noise_data, 1):
    x = data
    y = np.full_like(x, i, dtype=float) + 0.04 * (np.random.rand(len(x)) - 0.5)
    ax.scatter(x, y, alpha=0.6, color=single_color, edgecolors='w', s=50)

ax.xaxis.grid(True, linestyle='--', alpha=0.7)
acceptable_noise_level = 65
ax.axvline(acceptable_noise_level, color='r', linestyle='--', linewidth=1.5)

plt.tight_layout()
plt.show()