import matplotlib.pyplot as plt
import numpy as np

# Decades
decades = np.array([1980, 1990, 2000, 2010, 2020])

# Number of butterflies spotted at different points
key_point_1 = np.array([1500, 1200, 900, 800, 1100])
key_point_2 = np.array([3000, 2800, 2500, 2400, 3000])
key_point_3 = np.array([2500, 2200, 1900, 1800, 2600])
key_point_4 = np.array([2000, 1800, 1500, 1400, 2000])

# Conservation efforts effectiveness
conservation_efforts = np.array([20, 40, 60, 80, 90])

fig, ax = plt.subplots(figsize=(12, 8))

# Plot data with altered styles
ax.plot(decades, key_point_1, '*-', label='KP1', color='teal', linewidth=2)
ax.plot(decades, key_point_2, ':', label='KP2', color='darkorange', marker='P')
ax.plot(decades, key_point_3, 'x--', label='KP3', color='forestgreen', markersize=8)
ax.plot(decades, key_point_4, 'h-.', label='KP4', color='crimson')

ax2 = ax.twinx()
ax2.plot(decades, conservation_efforts, 'v-', color='mediumpurple', label='Conservation', linestyle=(0, (5, 10)))

# Titles and labels
ax.set_title('Monarchs (1980-2020)', fontsize=16, pad=20)
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Butterflies Spotted', fontsize=12)
ax2.set_ylabel('Conservation (%)', fontsize=12, color='mediumpurple')

# Legend and grid
ax.legend(loc='lower right', fontsize=10, ncol=2)
ax2.legend(loc='upper left', fontsize=10, frameon=False)
ax.grid(True, linestyle='-', linewidth=0.7, color='gray', alpha=0.7)

# Tweaked annotations
for decade, kp1, kp2, kp3, kp4 in zip(decades, key_point_1, key_point_2, key_point_3, key_point_4):
    ax.text(decade, kp1 + 100, f'{kp1}', ha='right', fontsize=8, color='teal')
    ax.text(decade, kp2 + 100, f'{kp2}', ha='center', fontsize=8, color='darkorange')
    ax.text(decade, kp3 + 100, f'{kp3}', ha='left', fontsize=8, color='forestgreen')
    ax.text(decade, kp4 + 100, f'{kp4}', ha='center', fontsize=8, color='crimson')

for decade, ce in zip(decades, conservation_efforts):
    ax2.text(decade, ce - 10, f'{ce}%', ha='left', fontsize=9, color='mediumpurple')

plt.tight_layout()
plt.show()