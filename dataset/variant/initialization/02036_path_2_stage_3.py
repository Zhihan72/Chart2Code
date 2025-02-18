import matplotlib.pyplot as plt
import numpy as np

sectors = ["Bio-Innov", "Renewables+Energy", "Robotics AI", "Quantum Simulations", "Future Biotech"]
innovation_data = [
    # Swap two elements in each list to demonstrate randomness
    [65, 85, 78, 72, 90, 92, 95, 97, 100, 105],  # Swapped indices 1 and 3
    [50, 62, 55, 65, 70, 78, 80, 88, 85, 82],    # Swapped indices 1 and 2, 7 and 9
    [30, 42, 35, 50, 60, 70, 75, 80, 90, 85],    # Swapped indices 1 and 2, 8 and 9
    [72, 70, 74, 75, 77, 80, 88, 85, 90, 92],    # Swapped indices 0 and 1, 6 and 7
    [40, 50, 58, 72, 65, 80, 85, 89, 93, 95],    # Swapped indices 3 and 4
]

fig, ax = plt.subplots(figsize=(12, 8))

bp = ax.boxplot(innovation_data, vert=True, patch_artist=True, 
                notch=True, showmeans=True, meanline=True,
                meanprops=dict(linestyle='--', linewidth=2.5, color='orange'))

single_color = '#66B3FF'
hatch = '/'
for patch in bp['boxes']:
    patch.set(facecolor=single_color, hatch=hatch, alpha=0.7)

for median in bp['medians']:
    median.set(color='blue', linewidth=3)
for whisker in bp['whiskers']:
    whisker.set(color='black', linewidth=2, linestyle='--')
for cap in bp['caps']:
    cap.set(color='black', linewidth=2)

ax.set_title('Tech Sector Index Trends\nLast 10 Years Review', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Sector Type', fontsize=13)
ax.set_ylabel('Innovation Score', fontsize=13)
ax.set_xticks(np.arange(1, len(sectors) + 1))
ax.set_xticklabels(sectors, fontsize=12, rotation=15)

ax.yaxis.grid(True, linestyle='--', alpha=0.7)

boxplot_elements = [bp['means'][0], bp['medians'][0], bp['whiskers'][0]]
ax.legend(boxplot_elements, ['Avg', 'Mid Value', 'Range Line'], loc='upper left')

plt.tight_layout()
plt.show()