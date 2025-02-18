import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023)
months = np.arange(1, 13)

# Manually altered monthly temperature data, maintaining the structure.
monthly_temps = np.array([
    [2, 4, 8, 12, 17, 21, 24, 23, 20, 15, 9, 5],
    [1, 3, 6, 10, 15, 19, 22, 21, 17, 13, 7, 2],
    [0, 2, 5, 9, 14, 18, 21, 20, 16, 11, 6, 1],
    [2, 4, 7, 11, 16, 21, 23, 22, 19, 14, 8, 4],
    [0, 2, 5, 8, 13, 18, 21, 20, 16, 11, 6, 1],
    [1, 3, 6, 10, 15, 19, 22, 21, 17, 13, 7, 2],
    [2, 4, 8, 12, 17, 21, 24, 23, 20, 15, 9, 5],
    [1, 3, 6, 10, 15, 19, 22, 21, 17, 13, 7, 3],
    [0, 2, 5, 9, 14, 18, 21, 20, 16, 11, 6, 2],
    [1, 4, 7, 11, 16, 20, 23, 22, 18, 13, 7, 3]
])

average_temps = np.mean(monthly_temps, axis=0)

fig, ax = plt.subplots(figsize=(14, 8))

for i, year in enumerate(years):
    ax.plot(months, monthly_temps[i], marker='o', linestyle='-', linewidth=2, markersize=6, label=f'{year}')

ax.plot(months, average_temps, marker='D', linestyle='--', color='black', linewidth=2, markersize=8, label='Decadal Average', zorder=10)

ax.set_title('Seasonal Changes in Average Temperature Over a Decade', fontsize=18, fontweight='bold')
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Average Temperature (°C)', fontsize=14)

ax.set_xticks(months)
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

ax.grid(True, linestyle='--', alpha=0.6)

ax.annotate('Warmest Year', xy=(7, 24), xytext=(2, 25),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=12, color='darkred', bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightgrey', alpha=0.8))

ax.annotate('Coldest Year', xy=(1, 0), xytext=(5, -5),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=12, color='darkblue', bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightgrey', alpha=0.8))

ax.set_xlim(1, 12)
ax.set_ylim(-5, 30)

ax.legend(loc='upper left', fontsize=12, ncol=2, title='Year', title_fontsize='13')

plt.tight_layout()
plt.show()