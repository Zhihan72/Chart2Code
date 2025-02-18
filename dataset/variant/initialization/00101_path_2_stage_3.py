import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

years = np.arange(2010, 2024)
papers_published = np.array([150, 170, 190, 220, 260, 310, 400, 480, 590, 680, 820, 950, 1100, 1280])
patents_filed = np.array([10, 15, 20, 25, 30, 38, 52, 67, 85, 110, 140, 180, 230, 300])

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