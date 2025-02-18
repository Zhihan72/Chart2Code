import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

years = np.arange(2010, 2024)

# Manually shuffled data
papers_published = np.array([310, 480, 150, 820, 170, 190, 400, 220, 950, 1280, 590, 260, 1100, 680])
patents_filed = np.array([110, 230, 10, 52, 15, 38, 85, 180, 25, 30, 67, 20, 140, 300])

fig, ax1 = plt.subplots(figsize=(14, 8))

single_color = 'navy'

ax1.scatter(years, papers_published, color=single_color, edgecolor='black', s=100, zorder=3)
ax1.plot(years, papers_published, linestyle='-', color=single_color, linewidth=2, zorder=2)

ax2 = ax1.twinx()
ax2.plot(years, patents_filed, color=single_color, linewidth=2, linestyle='--', zorder=1)

ax1.set_ylim(0, 1400)
ax1.set_xlim(years.min() - 1, years.max() + 1)
ax1.xaxis.set_major_locator(MaxNLocator(integer=True))

plt.tight_layout()
plt.show()