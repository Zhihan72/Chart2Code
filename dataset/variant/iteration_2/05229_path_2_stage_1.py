import matplotlib.pyplot as plt
import numpy as np

locations = ['City Center', 'Residential Area', 'Park', 'Industrial Zone', 'Suburbs']

noise_data = [
    [70, 75, 80, 72, 74, 78, 77, 73, 76, 79, 82, 74],
    [55, 60, 58, 57, 59, 61, 62, 56, 63, 64, 65, 57],
    [50, 52, 48, 49, 53, 51, 54, 47, 55, 57, 50, 52],
    [65, 68, 70, 72, 67, 66, 69, 71, 73, 74, 62, 65],
    [45, 48, 50, 47, 49, 46, 51, 52, 50, 53, 49, 48],
]

fig, ax = plt.subplots(figsize=(14, 8))
box = ax.boxplot(noise_data, vert=True, patch_artist=True, labels=locations, notch=True, whis=1.5)

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
    y = data
    x = np.full_like(y, i, dtype=float) + 0.04 * (np.random.rand(len(y)) - 0.5)
    ax.scatter(x, y, alpha=0.6, color=single_color, edgecolors='w', s=50, label=f'{locations[i - 1]} Data' if i == 1 else "")

means = [np.mean(scores) for scores in noise_data]
std_devs = [np.std(scores) for scores in noise_data]
for i, (mean, std_dev) in enumerate(zip(means, std_devs)):
    ax.text(i + 1, mean + 1, f"μ={mean:.1f}\nσ={std_dev:.1f}", ha='center', va='bottom', fontsize=9, color='black')

ax.set_title("Environmental Noise Levels in a Busy City\nComparing Noise Pollution Across Different Locations", fontsize=16, fontweight='bold')
ax.set_xlabel("City Locations", fontsize=13)
ax.set_ylabel("Noise Levels (dB)", fontsize=13)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

acceptable_noise_level = 65
ax.axhline(acceptable_noise_level, color='r', linestyle='--', linewidth=1.5, label='Acceptable Noise Level (65 dB)')

ax.legend(loc='upper right', fontsize=10)

plt.tight_layout()
plt.show()