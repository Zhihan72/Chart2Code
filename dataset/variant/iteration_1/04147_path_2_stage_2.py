import matplotlib.pyplot as plt
import numpy as np

# Updated data representing monthly temperatures (in °C) at seven different wells
well_temps = [
    [35, 36, 38, 40, 42, 45, 43, 41, 44, 37, 36, 35],  # Well A
    [50, 52, 54, 56, 55, 57, 58, 54, 53, 51, 52, 50],  # Well B
    [28, 30, 29, 31, 33, 35, 34, 32, 31, 30, 29, 28],  # Well C
    [45, 46, 47, 48, 49, 50, 49, 48, 47, 46, 45, 44],  # Well D
    [39, 38, 37, 36, 35, 34, 36, 38, 40, 39, 38, 37],  # Well E
    [22, 24, 23, 25, 27, 29, 30, 28, 26, 24, 23, 22],  # Well F
    [48, 49, 47, 46, 50, 53, 51, 49, 48, 47, 48, 49]   # Well G
]

# Updated well labels
wells = ['Well E', 'Well C', 'Well D', 'Well A', 'Well B', 'Well F', 'Well G']

fig, ax = plt.subplots(figsize=(12, 8))

bp = ax.boxplot(well_temps, patch_artist=True, notch=False, vert=True,
                boxprops=dict(color='black', linewidth=1.5),
                medianprops=dict(color='red', linewidth=2),
                whiskerprops=dict(color='black'),
                capprops=dict(color='black'),
                flierprops=dict(marker='o', color='blue', alpha=0.5))

colors = ['#ADD8E6', '#90EE90', '#FFC0CB', '#FA8072', '#87CEFA', '#FFD700', '#7FFFD4']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

for i, temps in enumerate(well_temps):
    mean = np.mean(temps)
    ax.annotate(f'Avg: {mean:.1f}°C', xy=(i+1, mean), xytext=(i+1.2, mean + 1),
                textcoords='data', arrowprops=dict(facecolor='black', arrowstyle='->'),
                fontsize=10, ha='center', va='bottom', color='darkred')

ax.set_title("Well Temperature Patterns Across Different Seasons", fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel("Temp in Celsius", fontsize=12, labelpad=10)
ax.set_xticklabels(wells, fontsize=12)

ax.grid(True, linestyle='--', alpha=0.6)
ax.set_facecolor('#f9f9f9')

for i, color in enumerate(colors):
    ax.scatter([], [], color=color, label=wells[i])
ax.legend(loc='upper left', fontsize=10, frameon=True, framealpha=1, edgecolor='black')

plt.tight_layout()
plt.show()