import matplotlib.pyplot as plt
import numpy as np

decades = [1980, 1990, 2000, 2010, 2020]
sea_levels_ny = [0, 22, 12, 48, 35]  # Randomly changed values
sea_levels_la = [0, 20, 32, 10, 50]  # Randomly changed values
sea_levels_miami = [0, 25, 40, 15, 60]  # Randomly changed values
sea_levels_tokyo = [0, 18, 8, 45, 30]   # Randomly changed values
sea_levels_mumbai = [0, 30, 65, 20, 45] # Randomly changed values

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(decades, sea_levels_ny, 'o-', label='NY', linewidth=2, markersize=8, color='blue')
ax.plot(decades, sea_levels_la, 's-', label='LA', linewidth=2, markersize=8, color='blue')
ax.plot(decades, sea_levels_miami, '^-', label='Miami', linewidth=2, markersize=8, color='blue')
ax.plot(decades, sea_levels_tokyo, 'd-', label='Tokyo', linewidth=2, markersize=8, color='blue')
ax.plot(decades, sea_levels_mumbai, '*-', label='Mumbai', linewidth=2, markersize=8, color='blue')

ax.annotate('Hurricane', xy=(2010, 48), xytext=(2010, 50),
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