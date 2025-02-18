import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
populations = {
    'Maple Land': [310, 300, 320, 280, 290, 340, 365, 330, 350, 310, 320],
    'Federation States': [1120, 1020, 1050, 990, 975, 1100, 1000, 1075, 1080, 1150, 1050],
    'Aztec Nation': [300, 240, 270, 245, 270, 250, 260, 290, 285, 280, 290]
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
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Timeline in Years', fontsize=12)
plt.ylabel('Counted Populations (in thousands)', fontsize=12)

plt.tight_layout()
plt.show()