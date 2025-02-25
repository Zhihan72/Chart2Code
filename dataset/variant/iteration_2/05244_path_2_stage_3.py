import numpy as np
import matplotlib.pyplot as plt

years = np.arange(1920, 2021, 10)

northern_hemisphere = [0.6, 1.4, 0.8, -0.1, 0.4, 0.0, 1.2, -0.3, 1.0, 0.2, 0.8]
tropical_regions = [0.5, 0.1, 0.9, 0.0, 0.3, 1.0, 0.7, 0.2, 1.1, 0.1, 0.8]
southern_hemisphere = [-0.2, 0.0, 0.7, 0.1, 0.5, 0.3, -0.3, 0.9, 0.6, -0.2, 0.8]

fig, ax = plt.subplots(figsize=(14, 8))

common_color = '#FF4500'

ax.plot(years, northern_hemisphere, marker='o', linestyle='-', color=common_color, linewidth=2)
ax.plot(years, tropical_regions, marker='^', linestyle='--', color=common_color, linewidth=2)
ax.plot(years, southern_hemisphere, marker='s', linestyle='-.', color=common_color, linewidth=2)

ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.5)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.axhline(0, color='gray', linewidth=1.5, linestyle='--', alpha=0.6)

plt.gca().set_facecolor('#f7f7f7')
plt.tight_layout()
plt.show()