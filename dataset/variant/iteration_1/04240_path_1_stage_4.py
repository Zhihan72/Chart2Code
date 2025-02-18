import matplotlib.pyplot as plt
import numpy as np

decades = [1980, 1990, 2000, 2010, 2020]
sea_levels_ny = [0, 22, 12, 48, 35]
sea_levels_la = [0, 20, 32, 10, 50]
sea_levels_miami = [0, 25, 40, 15, 60]
sea_levels_tokyo = [0, 18, 8, 45, 30]
sea_levels_mumbai = [0, 30, 65, 20, 45]

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(decades, sea_levels_ny, 'o--', label='NY', linewidth=2, markersize=10, color='green')
ax.plot(decades, sea_levels_la, 's-.', label='LA', linewidth=2, markersize=10, color='red')
ax.plot(decades, sea_levels_miami, '^-', label='Miami', linewidth=2, markersize=10, color='purple')
ax.plot(decades, sea_levels_tokyo, 'd:', label='Tokyo', linewidth=2, markersize=10, color='orange')
ax.plot(decades, sea_levels_mumbai, '*-', label='Mumbai', linewidth=2, markersize=10, color='brown')

ax.annotate('Hurricane', xy=(2010, 48), xytext=(2005, 55),
            arrowprops=dict(facecolor='darkred', arrowstyle='->'))
ax.annotate('Coral Bleaching', xy=(2010, 40), xytext=(1995, 60),
            arrowprops=dict(facecolor='cyan', arrowstyle='->'))

ax.set_title("Sea Level Rise", fontsize=18, fontweight='bold', color='navy')
ax.set_xlabel('Decade', fontsize=14, color='darkgreen')
ax.set_ylabel('Avg Level (mm)', fontsize=14, color='darkgreen')

ax.grid(True, linestyle='-', alpha=0.3, color='gray')

plt.xticks(decades)
plt.yticks(np.arange(0, 71, 10))

ax.set_xlim(1975, 2025)
ax.set_ylim(0, 70)

ax.legend(title='Cities', loc='lower right', fontsize=12, title_fontsize='13')

plt.tight_layout()
plt.show()