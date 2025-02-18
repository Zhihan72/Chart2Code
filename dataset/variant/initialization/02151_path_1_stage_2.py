import matplotlib.pyplot as plt
from matplotlib.colors import hex2color
from matplotlib.patches import Polygon
import numpy as np

stages = ['Idea Generation', 'Manuscript Drafting', 'Editing & Revisions', 
          'Submission to Publishers', 'Publication', 'Bestseller Status']
writers = [1000, 800, 500, 250, 120, 50]
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

# Changing colors, edge colors, and line styles for variety
colors = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
edge_colors = ['#6084b3', '#b36b6b', '#6bb36b', '#b3876b', '#9993b3', '#b3809e']
line_styles = ['-', '--', '-.', ':', '-', '--']
markers = ['o', 'v', 's', 'P', '^', '<']

for i, points in enumerate(polygon_points):
    funnel_polygon = Polygon(
        points, closed=True, 
        facecolor=colors[i], edgecolor=edge_colors[i], 
        linewidth=2, alpha=0.85, linestyle=line_styles[i]
    )
    ax.add_patch(funnel_polygon)
    percentage = (writers[i] / writers[0]) * 100
    ax.text(0.5, i + 0.5, f'{writers[i]} Writers\n({percentage:.1f}%)', va='center', ha='center', fontsize=10, color='black', fontweight='bold')

ax.set_yticks([i + 0.5 for i in range(len(stages))])
ax.set_yticklabels(stages, fontsize=12, fontweight='bold', ha='right')
ax.invert_yaxis()

plt.title("The Writer's Journey:\nFrom Concept to Bestseller", fontsize=16, fontweight='bold')
plt.xlabel('Proportion of Writers', fontsize=12)

# Adding a grid for better visual division
ax.grid(which='both', linestyle='--', linewidth=0.5, color='gray', axis='both')

ax.set_xticks([])
ax.set_xlim(0, 1)

# Adding a custom legend for markers
plt.legend(markers, [f'Stage {i+1}' for i in range(len(stages))], loc='upper right', title='Markers')

plt.tight_layout()
plt.show()