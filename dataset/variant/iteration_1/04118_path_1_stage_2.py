import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023)
months = np.arange(1, 13)

monthly_temps = np.array([
    [0, 3, 5, 9, 14, 17, 22, 20, 17, 12, 6, 2],
    [1, 3, 6, 10, 15, 19, 23, 21, 18, 13, 5, 3],
    [0, 1, 5, 9, 13, 18, 21, 20, 16, 10, 6, 1],
    [1, 5, 7, 11, 16, 19, 23, 21, 19, 14, 8, 4],
    [2, 4, 7, 10, 16, 21, 23, 22, 19, 15, 8, 5],
    [1, 3, 6, 10, 14, 19, 22, 21, 16, 13, 9, 2],
    [0, 2, 4, 8, 13, 17, 21, 20, 16, 11, 6, 1],
    [2, 4, 9, 12, 17, 21, 23, 24, 20, 15, 9, 5],
    [1, 3, 8, 11, 15, 20, 23, 21, 18, 12, 7, 4],
    [0, 2, 6, 11, 15, 18, 22, 21, 17, 13, 6, 3]
])

average_temps = np.mean(monthly_temps, axis=0)

fig, ax = plt.subplots(figsize=(14, 8))

for i, year in enumerate(years):
    ax.plot(months, monthly_temps[i], marker='o', linestyle='-', linewidth=2, markersize=6, label=f'Year {year}')

ax.plot(months, average_temps, marker='D', linestyle='--', color='black', linewidth=2, markersize=8, label='Ten-Year Avg', zorder=10)

ax.set_title('Decadal Temperature Trends', fontsize=18, fontweight='bold')
ax.set_xlabel('Months', fontsize=14)
ax.set_ylabel('Avg Temp (°C)', fontsize=14)

ax.set_xticks(months)
ax.set_xticklabels(['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'])

ax.grid(True, linestyle='--', alpha=0.6)

ax.annotate('Hottest Period', xy=(7, 24), xytext=(3, 26),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=12, color='darkred', bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightgrey', alpha=0.8))

ax.annotate('Coldest Period', xy=(1, 0), xytext=(6, -3),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=12, color='darkblue', bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightgrey', alpha=0.8))

ax.set_xlim(1, 12)
ax.set_ylim(-5, 30)

ax.legend(loc='upper left', fontsize=12, ncol=2, title='Annual', title_fontsize='13')

plt.tight_layout()
plt.show()