import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart represents the environmental noise levels in decibels (dB) recorded at different times of the day across five different locations in a busy city. This comparison helps in understanding the noise pollution levels during various periods and locations. The comparisons are essential for urban planning and creating quieter urban spaces.

# Data preparation: Noise levels (in dB) at different times of day for five locations
locations = ['City Center', 'Residential Area', 'Park', 'Industrial Zone', 'Suburbs']
times_of_day = ['Morning', 'Afternoon', 'Evening', 'Night']

# Manually constructed data representing noise levels
noise_data = [
    [70, 75, 80, 72, 74, 78, 77, 73, 76, 79, 82, 74],  # City Center
    [55, 60, 58, 57, 59, 61, 62, 56, 63, 64, 65, 57],  # Residential Area
    [50, 52, 48, 49, 53, 51, 54, 47, 55, 57, 50, 52],  # Park
    [65, 68, 70, 72, 67, 66, 69, 71, 73, 74, 62, 65],  # Industrial Zone
    [45, 48, 50, 47, 49, 46, 51, 52, 50, 53, 49, 48],  # Suburbs
]

# Setting up the figure for the box plot
fig, ax = plt.subplots(figsize=(14, 8))
box = ax.boxplot(noise_data, vert=True, patch_artist=True, labels=locations, notch=True, whis=1.5)

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
    x = np.random.normal(i, 0.04, size=len(y))  # jitter x-coordinates
    ax.scatter(x, y, alpha=0.6, color=colors[i - 1], edgecolors='w', s=50, label=f'{locations[i - 1]} Data' if i == 1 else "")

# Preparing means and standard deviation annotations
means = [np.mean(scores) for scores in noise_data]
std_devs = [np.std(scores) for scores in noise_data]
for i, (mean, std_dev) in enumerate(zip(means, std_devs)):
    ax.text(i + 1, mean + 1, f"μ={mean:.1f}\nσ={std_dev:.1f}", 
            ha='center', va='bottom', fontsize=9, color='black')

# Title and labels
ax.set_title("Environmental Noise Levels in a Busy City\nComparing Noise Pollution Across Different Locations and Times of Day", 
             fontsize=16, fontweight='bold')
ax.set_xlabel("City Locations", fontsize=13)
ax.set_ylabel("Noise Levels (dB)", fontsize=13)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Reference line for acceptable noise level
acceptable_noise_level = 65
ax.axhline(acceptable_noise_level, color='r', linestyle='--', linewidth=1.5, label='Acceptable Noise Level (65 dB)')

# Legend for different elements
ax.legend(loc='upper right', fontsize=10)

# Enhance the visual appeal and layout
plt.tight_layout()

# Display the chart
plt.show()