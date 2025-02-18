import matplotlib.pyplot as plt
from matplotlib.colors import ColorConverter
from matplotlib.patches import Polygon
import numpy as np

# Manually shuffled stages and corresponding writer numbers to simulate randomness
stages = ['Submission to Publishers', 'Idea Generation', 'Publication', 
          'Manuscript Drafting', 'Bestseller Status', 'Editing & Revisions']
writers = [250, 1000, 120, 800, 50, 500]

# Use a single color for the entire funnel
single_color = '#66b3ff'

widths = [w / max(writers) for w in writers]
polygon_points = []
for i, width in enumerate(widths):
    bottom_width = width if i == len(widths) - 1 else widths[i + 1]
    top_left = ((1 - width) / 2, i)
    top_right = ((1 + width) / 2, i)
    bottom_left = ((1 - bottom_width) / 2, i + 1)
    bottom_right = ((1 + bottom_width) / 2, i + 1)
    polygon_points.append([top_left, top_right, bottom_right, bottom_left])

fig, ax = plt.subplots(figsize=(10, 7))
for i, points in enumerate(polygon_points):
    edge_color = tuple(map(lambda x: x * 0.8, ColorConverter.to_rgb(single_color)))
    funnel_polygon = Polygon(points, closed=True, facecolor=single_color, edgecolor=edge_color, linewidth=2, alpha=0.85)
    ax.add_patch(funnel_polygon)
    
    percentage = (writers[i] / writers[0]) * 100
    ax.text(0.5, i + 0.5, f'{writers[i]} Writers\n({percentage:.1f}%)', va='center', ha='center', fontsize=10, color='black', fontweight='bold')

ax.set_yticks([i + 0.5 for i in range(len(stages))])
ax.set_yticklabels(stages, fontsize=12, fontweight='bold', ha='right')
ax.invert_yaxis()

plt.title("The Writer's Journey:\nFrom Concept to Bestseller", fontsize=16, fontweight='bold')
plt.xlabel('Proportion of Writers', fontsize=12)

ax.set_xticks([])
ax.set_xlim(0, 1)

plt.tight_layout()
plt.show()