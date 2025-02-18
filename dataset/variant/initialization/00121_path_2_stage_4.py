import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

student_counts = np.array([600, 700, 1000, 250, 850, 300, 500, 400])

widths = student_counts / student_counts[0]

# Shuffled colors
colors = ['#e78ac3', '#66c2a5', '#b3b3b3', '#fc8d62', '#a6d854', '#8da0cb', '#e5c494', '#ffd92f']

fig, ax = plt.subplots(figsize=(14, 10))

# Different line styles and markers
line_styles = ['-', '--', '-.', ':']
markers = ['o', 's', '^', 'D']

for i in range(len(student_counts)):
    top_width = widths[i-1] if i > 0 else 1.0
    bottom_width = widths[i]
    
    trapezoid = patches.Polygon(
        [
            [(1 - top_width) / 2, i], [(1 + top_width) / 2, i], 
            [(1 + bottom_width) / 2, i + 1], [(1 - bottom_width) / 2, i + 1]
        ], closed=True, color=colors[i],
        edgecolor='black',
        linestyle=line_styles[i % len(line_styles)],
        linewidth=1.5
    )
    ax.add_patch(trapezoid)

# Add gridlines
ax.yaxis.grid(True, linestyle='--', color='gray')

# Add border
for spine in ax.spines.values():
    spine.set_edgecolor('blue')
    spine.set_linewidth(1.5)

ax.set_xlim(0, 1)
ax.set_ylim(0, len(student_counts))

# Create legend manually
legend_handles = [
    patches.Patch(color=colors[i], label=f'Student Group {i+1}',
                  linestyle=line_styles[i % len(line_styles)])
    for i in range(len(student_counts))
]
ax.legend(handles=legend_handles, loc='upper right')

plt.tight_layout()
plt.show()