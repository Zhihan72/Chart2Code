import matplotlib.pyplot as plt
import numpy as np

star_ages = np.array([1.5, 2.0, 4.1, 5.5, 6.3, 7.9, 8.5, 9.1, 10.4, 11.2, 12.6, 13.3, 14.5, 15.0, 16.1])
exoplanets_count = np.array([2, 3, 4, 6, 5, 8, 7, 7, 9, 8, 10, 11, 13, 12, 14])
brightness = np.array([15, 20, 35, 40, 45, 60, 65, 50, 70, 80, 95, 90, 105, 110, 120])

star_ages_group2 = np.array([1.0, 2.5, 3.0, 4.5, 5.8, 6.7, 7.0, 8.3, 9.6, 10.5, 11.8, 12.5, 13.1, 15.5, 16.5])
exoplanets_count_group2 = np.array([1, 2, 3, 5, 4, 6, 7, 6, 7, 7, 9, 10, 11, 11, 13])
brightness_group2 = np.array([10, 18, 30, 38, 42, 58, 60, 48, 66, 76, 90, 89, 103, 112, 117])

colors1 = plt.cm.plasma((star_ages - star_ages.min()) / (star_ages.max() - star_ages.min()))
colors2 = plt.cm.viridis((star_ages_group2 - star_ages_group2.min()) / (star_ages_group2.max() - star_ages_group2.min()))

fig, ax1 = plt.subplots(figsize=(12, 8))

ax1.barh(range(len(star_ages)), exoplanets_count, color=colors1, alpha=0.7, label='Group 1')
ax1.barh(range(len(star_ages_group2)), exoplanets_count_group2, left=exoplanets_count, color=colors2, alpha=0.7, label='Group 2')

ax1.set_yticks(range(len(star_ages)))
ax1.set_yticklabels(star_ages)
ax1.set_xlabel('Exoplanets', fontsize=12)
ax1.set_ylabel('Star Ages (B Years)', fontsize=12)

ax2 = ax1.twiny()

ax2.plot(brightness, range(len(brightness)), color='orange', linestyle='--', linewidth=2, label='Brightness 1')
ax2.plot(brightness_group2, range(len(brightness_group2)), color='green', linestyle=':', linewidth=2, label='Brightness 2')

ax2.set_xlabel('Brightness', fontsize=12)
plt.title('Star Age vs. Exoplanets with Additional Data Series', fontsize=16, fontweight='bold')

ax1.legend(loc='upper right')
ax2.legend(loc='lower right')

plt.show()