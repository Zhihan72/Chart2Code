import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
populations = {
    'Northland': [300, 320, 280, 290, 310, 340, 365, 350, 330, 320, 310],
    'United States': [1000, 1050, 990, 975, 1120, 1150, 1100, 1080, 1075, 1050, 1020],
    'Mexica': [250, 270, 240, 245, 260, 290, 300, 290, 285, 280, 270],
    'Centro America': [150, 160, 155, 158, 170, 175, 180, 185, 190, 195, 200]
}

plt.figure(figsize=(14, 8))

markers = ['s', '^', 'D', '*']
line_styles = ['--', '-.', ':', '-']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

for (region, pops), color, marker, style in zip(populations.items(), colors, markers, line_styles):
    plt.plot(years, pops, linestyle=style, marker=marker, label=region, color=color, linewidth=1.5, markersize=8, alpha=0.85)
    
    midpoint_index = len(years) // 2
    key_points = [(years[0], pops[0]), (years[midpoint_index], pops[midpoint_index]), (years[-1], pops[-1])]
    for (year, pop) in key_points:
        plt.annotate(f'{pop}k', xy=(year, pop), xytext=(5, -15 if pop < max(pops) else 5), 
                     textcoords='offset points', arrowprops=dict(arrowstyle='->', color=color), 
                     fontsize=10, color=color, ha='center')

plt.title('Butterfly Movement Trends (2010-2020)\nDetected Swarm in Latin Regions', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Calendar Year', fontsize=12)
plt.ylabel('Detected Swarms (in thousands)', fontsize=12)

plt.legend(title='Zones', loc='lower left', fontsize=10, frameon=False)
plt.grid(True, which='major', axis='x', linestyle='-', linewidth=0.7, alpha=0.6)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.tight_layout()
plt.show()