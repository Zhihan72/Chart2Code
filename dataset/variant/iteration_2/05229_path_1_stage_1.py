import matplotlib.pyplot as plt
import numpy as np

# Data preparation: Noise levels (in dB) at different times of day for five locations
noise_data = [
    [70, 75, 80, 72, 74, 78, 77, 73, 76, 79, 82, 74],
    [55, 60, 58, 57, 59, 61, 62, 56, 63, 64, 65, 57],
    [50, 52, 48, 49, 53, 51, 54, 47, 55, 57, 50, 52],
    [65, 68, 70, 72, 67, 66, 69, 71, 73, 74, 62, 65],
    [45, 48, 50, 47, 49, 46, 51, 52, 50, 53, 49, 48],
]

# Setting up the figure for the box plot
fig, ax = plt.subplots(figsize=(14, 8))
box = ax.boxplot(noise_data, vert=True, patch_artist=True, notch=True, whis=1.5)

# Customizing the plot with colors and styles
colors = ['#FFA07A', '#20B2AA', '#FFD700', '#FF6347', '#40E0D0']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

# Customize whiskers, caps, and medians
for whisker in box['whiskers']:
    whisker.set(color='#8B8B8B', linewidth=1.5, linestyle='--')
for cap in box['caps']:
    cap.set(color='#8B8B8B', linewidth=1.5)
for median in box['medians']:
    median.set(color='black', linewidth=2)

# Add scatter plot with jitter for individual data points
for i, data in enumerate(noise_data, 1):
    y = data
    x = np.random.normal(i, 0.04, size=len(y))
    ax.scatter(x, y, alpha=0.6, color=colors[i - 1], edgecolors='w', s=50)

# Reference line for acceptable noise level
acceptable_noise_level = 65
ax.axhline(acceptable_noise_level, color='r', linestyle='--', linewidth=1.5)

# Display the chart
plt.show()