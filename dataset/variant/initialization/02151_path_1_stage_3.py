import matplotlib.pyplot as plt
from matplotlib.colors import hex2color
from matplotlib.patches import Polygon
import numpy as np

stages = ['Idea Generation', 'Manuscript Drafting', 'Editing & Revisions', 
          'Submission to Publishers', 'Publication', 'Bestseller Status']
writers = [1000, 800, 500, 250, 120, 50]
editing_team = [500, 400, 350, 270, 150, 70]  # New data series for 'Editing Team'
widths_writers = [w / max(writers) for w in writers]
widths_editors = [e / max(editing_team) for e in editing_team]  # Normalized widths for the editing team

polygon_points_writers = []
polygon_points_editors = []

for i, width in enumerate(widths_writers):
    bottom_width = width if i == len(widths_writers) - 1 else widths_writers[i + 1]
    top_left = ((1 - width) / 2, i)
    top_right = ((1 + width) / 2, i)
    bottom_left = ((1 - bottom_width) / 2, i + 1)
    bottom_right = ((1 + bottom_width) / 2, i + 1)
    polygon_points_writers.append([top_left, top_right, bottom_right, bottom_left])

for i, width in enumerate(widths_editors):
    bottom_width = width if i == len(widths_editors) - 1 else widths_editors[i + 1]
    top_left = ((1.5 - width) / 2, i + 0.1)
    top_right = ((1.5 + width) / 2, i + 0.1)
    bottom_left = ((1.5 - bottom_width) / 2, i + 1.1)
    bottom_right = ((1.5 + bottom_width) / 2, i + 1.1)
    polygon_points_editors.append([top_left, top_right, bottom_right, bottom_left])

fig, ax = plt.subplots(figsize=(10, 7))

colors_writers = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
colors_editors = ['#ffd966', '#e6b3ff', '#ff99ff', '#ff99b6', '#99e6ff', '#b3e6cc']

for i, points in enumerate(polygon_points_writers):
    funnel_polygon_writers = Polygon(
        points, closed=True, 
        facecolor=colors_writers[i], edgecolor='gray', 
        linewidth=2, alpha=0.7
    )
    ax.add_patch(funnel_polygon_writers)
    percentage = (writers[i] / writers[0]) * 100
    ax.text(0.25, i + 0.5, f'{writers[i]} Writers\n({percentage:.1f}%)', va='center', ha='center', fontsize=10, color='black', fontweight='bold')

for i, points in enumerate(polygon_points_editors):
    funnel_polygon_editors = Polygon(
        points, closed=True, 
        facecolor=colors_editors[i], edgecolor='darkred', 
        linewidth=2, alpha=0.7
    )
    ax.add_patch(funnel_polygon_editors)
    percentage = (editing_team[i] / editing_team[0]) * 100
    ax.text(1.0, i + 0.6, f'{editing_team[i]} Editors\n({percentage:.1f}%)', va='center', ha='center', fontsize=10, color='black', fontweight='bold')

ax.set_yticks([i + 0.5 for i in range(len(stages))])
ax.set_yticklabels(stages, fontsize=12, fontweight='bold', ha='right')
ax.invert_yaxis()

plt.title("The Writer's and Editor's Journey:\nFrom Concept to Bestseller", fontsize=16, fontweight='bold')
plt.xlabel('Proportion of Participants', fontsize=12)

ax.grid(which='both', linestyle='--', linewidth=0.5, color='gray', axis='both')

ax.set_xticks([])
ax.set_xlim(-0.1, 1.5)

plt.tight_layout()
plt.show()