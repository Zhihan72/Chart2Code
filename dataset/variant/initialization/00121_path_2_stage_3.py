import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

student_counts = np.array([600, 700, 1000, 250, 850, 300, 500, 400])

widths = student_counts / student_counts[0]

# Shuffled colors
colors = ['#fc8d62', '#b3b3b3', '#e5c494', '#8da0cb', '#66c2a5', '#e78ac3', '#ffd92f', '#a6d854']

fig, ax = plt.subplots(figsize=(14, 10))

for i in range(len(student_counts)):
    top_width = widths[i-1] if i > 0 else 1.0
    bottom_width = widths[i]
    
    trapezoid = patches.Polygon(
        [
            [(1 - top_width) / 2, i], [(1 + top_width) / 2, i], 
            [(1 + bottom_width) / 2, i + 1], [(1 - bottom_width) / 2, i + 1]
        ], closed=True, color=colors[i], edgecolor='black'
    )
    ax.add_patch(trapezoid)

ax.set_xlim(0, 1)
ax.set_ylim(0, len(student_counts))
ax.axis('off')

plt.tight_layout()
plt.show()