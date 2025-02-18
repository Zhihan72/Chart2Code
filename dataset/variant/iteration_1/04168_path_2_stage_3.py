import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1990, 2021)

physical_media = np.array([90, 87, 85, 82, 76, 70, 65, 60, 55, 50, 45, 40, 35, 32, 28, 24, 20, 18, 15, 12, 10, 8, 6, 5, 4, 3, 3, 3, 2, 1, 1])
digital_downloads = np.array([0, 1, 2, 4, 6, 7, 8, 9, 12, 15, 20, 25, 30, 35, 40, 42, 45, 48, 50, 52, 53, 54, 56, 58, 60, 60, 58, 55, 50, 48, 45])
streaming = np.array([0, 0, 0, 0, 0, 0, 1, 2, 3, 5, 10, 15, 20, 25, 30, 35, 40, 45, 48, 50, 55, 60, 62, 65, 68, 72, 75, 78, 82, 85, 88])

# Adding new data series for Vinyl Revival
vinyl_revival = np.array([0, 0, 0, 0, 0, 0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 18, 20, 23, 26, 28, 30, 35, 40, 43, 46, 50, 55, 60])

# Calculate 'others' again, now including vinyl_revival
others = 100 - (physical_media + digital_downloads + streaming + vinyl_revival)

fig, ax = plt.subplots(figsize=(14, 8))

# Updated colors to include one more for vinyl_revival
colors = ['#FFD700', '#DA70D6', '#32CD32', '#FF6347', '#4682B4']

# Include vinyl_revival in stackplot
ax.stackplot(years, physical_media, digital_downloads, streaming, vinyl_revival, others, colors=colors, alpha=0.8)

ax.grid(linestyle='-', linewidth=1, alpha=0.3)

plt.xticks(years[::5])

plt.tight_layout()
plt.show()