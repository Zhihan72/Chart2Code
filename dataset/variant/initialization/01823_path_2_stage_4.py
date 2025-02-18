import matplotlib.pyplot as plt
import numpy as np

# Data preparation
star_ages = np.array([1.5, 2.0, 4.1, 5.5, 6.3, 7.9, 8.5, 9.1, 10.4, 11.2, 12.6, 13.3, 14.5, 15.0, 16.1])
exoplanets_count = np.array([2, 3, 4, 6, 5, 8, 7, 7, 9, 8, 10, 11, 13, 12, 14])

# Shuffle colors
colors = plt.cm.viridis(np.random.permutation((star_ages - star_ages.min()) / (star_ages.max() - star_ages.min())))

fig, ax = plt.subplots(figsize=(12, 8))

# Plotting horizontal bar chart
ax.barh(star_ages, exoplanets_count, color=colors, alpha=0.7)
ax.set_xlabel('Number of Exoplanets', fontsize=12)
ax.set_ylabel('Star Age (Billion Years)', fontsize=12)

title = 'Star Age vs. Number of Exoplanets'
plt.title(title, fontsize=16, fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.6)

fig.tight_layout()
plt.show()