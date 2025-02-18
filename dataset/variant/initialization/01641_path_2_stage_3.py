import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
gallery_visitors = {
    'NY': [950, 920, 970, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1400],
    'Paris': [750, 780, 760, 800, 850, 880, 910, 930, 950, 970, 1000],
    'Tokyo': [600, 620, 650, 670, 700, 730, 750, 770, 800, 830, 860],
    'London': [890, 870, 880, 920, 940, 960, 1000, 1020, 1040, 1060, 1100],
    'Berlin': [400, 420, 430, 450, 480, 500, 520, 540, 550, 570, 600],
    'Sydney': [500, 530, 560, 590, 620, 650, 680, 710, 740, 770, 800]
}

cumulative_visitors = np.sum(list(gallery_visitors.values()), axis=0)

fig, ax1 = plt.subplots(figsize=(14, 8))

colors = ['#8A2BE2', '#32CD32', '#FFD700', '#4682B4', '#FF6347', '#FFA500']
markers = ['s', 'v', '^', 'd', 'p', 'o']
linestyles = ['-.', ':', '--', '-', '-.', '--']

for (city, visitors), color, marker, linestyle in zip(gallery_visitors.items(), colors, markers, linestyles):
    ax1.plot(years, visitors, marker=marker, linestyle=linestyle, label=city, color=color, linewidth=2, markersize=6, alpha=0.8)
    
    midpoint_index = len(years) // 2
    key_points = [(years[0], visitors[0]), (years[midpoint_index], visitors[midpoint_index]), (years[-1], visitors[-1])]
    for (year, visitor) in key_points:
        ax1.annotate(f'{visitor}k', xy=(year, visitor), xytext=(10, -10 if visitor < max(visitors) else 10), 
                     textcoords='offset points', fontsize=10, color=color, ha='center')

ax1.grid(True, which='both', linestyle='-', linewidth=0.7, alpha=0.5)

ax2 = ax1.twinx()
ax2.fill_between(years, 0, cumulative_visitors, color='gray', alpha=0.2)
ax2.set_ylabel('Cumulative Visitors (k)', fontsize=12)
ax2.set_ylim(0, np.max(cumulative_visitors) + 500)

ax1.set_title('Gallery Visitors (2010-20)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Visitors (k)', fontsize=12)
ax1.legend(loc='upper right', fontsize=10)

plt.tight_layout()
plt.show()