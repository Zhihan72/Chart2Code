import matplotlib.pyplot as plt
from matplotlib.colors import ColorConverter
from matplotlib.patches import Polygon
import numpy as np

stages = ['Submission to Publishers', 'Idea Generation', 'Publication', 
          'Manuscript Drafting', 'Bestseller Status', 'Editing & Revisions']
writers = [250, 1000, 120, 800, 50, 500]

single_color = '#66b3ff'

widths = [w / max(writers) for w in writers]
polygon_points = [
    [((1 - widths[i]) / 2, i), ((1 + widths[i]) / 2, i), 
     ((1 + widths[i+1]) / 2, i + 1), ((1 - widths[i+1]) / 2, i + 1)]
    for i in range(len(widths) - 1)
]
# Add the last polygon
polygon_points.append([
    ((1 - widths[-1]) / 2, len(widths) - 1), 
    ((1 + widths[-1]) / 2, len(widths) - 1),
    (1, len(widths)), (0, len(widths))
])

fig, ax = plt.subplots(figsize=(10, 7))
for i, points in enumerate(polygon_points):
    funnel_polygon = Polygon(points, closed=True, facecolor=single_color, edgecolor=None, linewidth=0)
    ax.add_patch(funnel_polygon)
    
    percentage = (writers[i] / writers[0]) * 100
    ax.text(0.5, i + 0.5, f'{writers[i]} Writers\n({percentage:.1f}%)', va='center', ha='center', fontsize=10, color='black', fontweight='bold')

ax.set_yticks([i + 0.5 for i in range(len(stages))])
ax.set_yticklabels(stages, fontsize=12, fontweight='bold', ha='right')
ax.invert_yaxis()

ax.set_xticks([])
ax.set_xlim(0, 1)
ax.set_frame_on(False)  # Eliminate the plot borders

plt.tight_layout()
plt.show()