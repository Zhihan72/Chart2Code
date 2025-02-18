import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1990, 2021)

physical_media = np.array([90, 87, 85, 82, 76, 70, 65, 60, 55, 50, 45, 40, 35, 32, 28, 24, 20, 18, 15, 12, 10, 8, 6, 5, 4, 3, 3, 3, 2, 1, 1])
digital_downloads = np.array([0, 1, 2, 4, 6, 7, 8, 9, 12, 15, 20, 25, 30, 35, 40, 42, 45, 48, 50, 52, 53, 54, 56, 58, 60, 60, 58, 55, 50, 48, 45])
streaming = np.array([0, 0, 0, 0, 0, 0, 1, 2, 3, 5, 10, 15, 20, 25, 30, 35, 40, 45, 48, 50, 55, 60, 62, 65, 68, 72, 75, 78, 82, 85, 88])
others = 100 - (physical_media + digital_downloads + streaming)

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#FFD700', '#DA70D6', '#32CD32', '#FF6347']

ax.stackplot(years, physical_media, digital_downloads, streaming, others, colors=colors, alpha=0.8)

ax.grid(linestyle='-', linewidth=1, alpha=0.3)

plt.xticks(years[::5])

plt.tight_layout()
plt.show()