import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
populations = {
    'Maple Land': [300, 320, 280, 290, 310, 340, 365, 350, 330, 320, 310],  # Altered 'Canada'
    'Federation States': [1000, 1050, 990, 975, 1120, 1150, 1100, 1080, 1075, 1050, 1020],  # Altered 'USA'
    'Aztec Nation': [250, 270, 240, 245, 260, 290, 300, 290, 285, 280, 270]  # Altered 'Mexico'
}

plt.figure(figsize=(14, 8))
colors = ['#ff7f0e', '#2ca02c', '#1f77b4']

for (region, pops), color in zip(populations.items(), colors):
    plt.plot(years, pops, '-o', color=color, linewidth=2, markersize=6, alpha=0.8)
    
    midpoint_index = len(years) // 2
    key_points = [(years[0], pops[0]), (years[midpoint_index], pops[midpoint_index]), (years[-1], pops[-1])]
    for (year, pop) in key_points:
        plt.annotate(f'{pop}k', xy=(year, pop), xytext=(5, -15 if pop < max(pops) else 5), 
                     textcoords='offset points', arrowprops=dict(arrowstyle='->', color=color), 
                     fontsize=10, color=color, ha='center')

plt.title('North American Avian Journey (2010-2020)\nMonitored Population Shifts', 
          fontsize=16, fontweight='bold', pad=20)  # Altered title
plt.xlabel('Timeline in Years', fontsize=12)  # Altered xlabel
plt.ylabel('Counted Populations (in thousands)', fontsize=12)  # Altered ylabel

plt.tight_layout()
plt.show()