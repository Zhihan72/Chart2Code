import matplotlib.pyplot as plt
import numpy as np

sectors = ["Bio-Innov", "Renewables+Energy", "Robotics AI", "Quantum Simulations", "Future Biotech"]
innovation_data = [
    [65, 78, 85, 72, 90, 92, 97, 95, 105, 100], 
    [70, 62, 50, 65, 78, 80, 88, 82, 85, 55],  
    [30, 35, 42, 50, 75, 70, 80, 90, 85, 60],  
    [72, 74, 70, 75, 77, 80, 85, 88, 92, 90],  
    [40, 50, 65, 58, 72, 85, 80, 93, 95, 89],  
]

fig, ax = plt.subplots(figsize=(12, 8))

bp = ax.boxplot(innovation_data, vert=False, patch_artist=True, 
                notch=True, showmeans=True, meanline=True,
                meanprops=dict(linestyle='-.', linewidth=2.0, color='green'))

single_color = '#FFD700'
hatch = 'o'
for patch in bp['boxes']:
    patch.set(facecolor=single_color, hatch=hatch, alpha=0.8)

for median in bp['medians']:
    median.set(color='red', linewidth=2.5)
for whisker in bp['whiskers']:
    whisker.set(color='purple', linewidth=1.5, linestyle=':')
for cap in bp['caps']:
    cap.set(color='grey', linewidth=1.5)

ax.set_title('Tech Sector Index Trends\nLast 10 Years Review', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Innovation Score', fontsize=13)
ax.set_ylabel('Sector Type', fontsize=13)
ax.set_yticks(np.arange(1, len(sectors) + 1))
ax.set_yticklabels(sectors, fontsize=12, rotation=15)

ax.xaxis.grid(True, linestyle='-', alpha=0.5)

boxplot_elements = [bp['means'][0], bp['medians'][0], bp['caps'][0]]
ax.legend(boxplot_elements, ['Average', 'Median', 'Cap Line'], loc='upper right')

plt.tight_layout()
plt.show()