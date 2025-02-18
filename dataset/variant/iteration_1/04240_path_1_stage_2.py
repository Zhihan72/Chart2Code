import matplotlib.pyplot as plt
import numpy as np

decades = [1980, 1990, 2000, 2010, 2020]
sea_levels_ny = [0, 12, 22, 35, 48]
sea_levels_la = [0, 10, 20, 32, 50]
sea_levels_miami = [0, 15, 25, 40, 60]
sea_levels_tokyo = [0, 8, 18, 30, 45]
sea_levels_mumbai = [0, 20, 30, 45, 65]

fig, ax = plt.subplots(figsize=(14, 7))

# Choose a consistent color, e.g., 'blue'
ax.plot(decades, sea_levels_ny, 'o-', label='NY', linewidth=2, markersize=8, color='blue')
ax.plot(decades, sea_levels_la, 's-', label='LA', linewidth=2, markersize=8, color='blue')
ax.plot(decades, sea_levels_miami, '^-', label='Miami', linewidth=2, markersize=8, color='blue')
ax.plot(decades, sea_levels_tokyo, 'd-', label='Tokyo', linewidth=2, markersize=8, color='blue')
ax.plot(decades, sea_levels_mumbai, '*-', label='Mumbai', linewidth=2, markersize=8, color='blue')

ax.annotate('Hurricane', xy=(2010, 35), xytext=(2010, 40),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('Coral Bleaching', xy=(2010, 40), xytext=(2000, 60),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax.set_title("Sea Level Rise", fontsize=16, fontweight='bold')
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Avg Level (mm)', fontsize=12)

ax.grid(True, linestyle='--', alpha=0.5)

plt.xticks(decades)
plt.yticks(np.arange(0, 71, 10))

ax.set_xlim(1975, 2025)
ax.set_ylim(0, 70)

ax.legend(title='Cities', loc='upper left', fontsize=11)

plt.tight_layout()
plt.show()