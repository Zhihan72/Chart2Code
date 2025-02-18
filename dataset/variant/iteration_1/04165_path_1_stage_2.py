import matplotlib.pyplot as plt
import numpy as np

# Data preparation
screen_time = np.array([0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
sleep_quality = np.array([9, 8.5, 8, 7.5, 7, 6.5, 5.5, 5, 4.5, 4, 3.5, 3, 2.5])
sleep_disturbances = np.array([3, 2, 4, 6, 7, 9, 10, 12, 13, 15, 18, 20, 22])

# Create a figure and axis with dual y-axes
fig, ax1 = plt.subplots(figsize=(12, 8))

# Scatter plot
ax1.scatter(screen_time, sleep_quality, c='orange', edgecolor='k', s=100, alpha=0.7)
ax1.set_xlabel('Daily Screen Time (hours)', fontsize=12)
ax1.set_ylabel('Sleep Quality Rating (1-10)', fontsize=12, color='orange')
ax1.tick_params(axis='y', labelcolor='orange')

# Secondary y-axis for sleep disturbances
ax2 = ax1.twinx()
ax2.plot(screen_time, sleep_disturbances, color='skyblue', linewidth=2, linestyle='--')
ax2.set_ylabel('Sleep Disturbances (count)', fontsize=12, color='skyblue')
ax2.tick_params(axis='y', labelcolor='skyblue')

# Title
plt.title('Impact of Daily Screen Time on Sleep Quality and Sleep Disturbances\nStudy of Digital Device Usage', fontsize=16, fontweight='bold')

# Remove chart borders
for spine in ax1.spines.values():
    spine.set_visible(False)
for spine in ax2.spines.values():
    spine.set_visible(False)

# Annotate an important data point
ax1.annotate('Significant Drop in Sleep Quality and Increase in Disturbances', xy=(10, 3.5), xytext=(7, 5.5), arrowprops=dict(facecolor='black', arrowstyle='->', alpha=0.7), fontsize=10)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()