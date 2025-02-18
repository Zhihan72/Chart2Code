import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Randomly altered texts:
random_steps = [
    "Graduation",
    "Dissertation\nDefense",
    "Coursework\nCompletion",
    "Qualifying\nExam",
    "Enrollment",
    "Comprehensive\nExams"
]

student_counts = np.array([1000, 850, 700, 500, 300, 250])
dropout_rates = 100 * (1 - student_counts[1:] / student_counts[:-1])
widths = student_counts / student_counts[0]

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#e377c2', '#7f7f7f']

fig, ax = plt.subplots(figsize=(14, 8))

for i in range(len(random_steps)):
    top_width = widths[i-1] if i > 0 else 1.0
    bottom_width = widths[i]
    line_style = '-' if i % 2 == 0 else '--'
    
    trapezoid = patches.Polygon(
        [
            [(1 - top_width) / 2, i], [(1 + top_width) / 2, i], 
            [(1 + bottom_width) / 2, i + 1], [(1 - bottom_width) / 2, i + 1]
        ], closed=True, color=colors[i], edgecolor='black', linestyle=line_style
    )
    ax.add_patch(trapezoid)
    
    ax.text(0.5, i + 0.5, f"{random_steps[i]}\n{student_counts[i]} Students",
            ha='center', va='center', fontsize=11, color='black', weight='bold')

    if i > 0:
        ax.text(0.95, i + 0.5, f"Dropoff: {dropout_rates[i-1]:.1f}%", 
                ha='right', va='center', fontsize=10, color='red', weight='bold')

ax.set_xlim(0, 1)
ax.set_ylim(0, len(random_steps))
ax.grid(visible=True, linestyle=':', linewidth=0.5)
ax.axis('on')

legend_elements = [patches.Patch(facecolor=colors[i], edgecolor='black',
                                 label=f"{random_steps[i]}: {student_counts[i]}")
                   for i in range(len(random_steps))]
ax.legend(handles=legend_elements, loc='upper right', fontsize=9, frameon=True, shadow=True, title="Phases", title_fontsize='13')

# Random title
ax.set_title('Randomized Academic Journey:\nStudent Attrition Analysis',
             fontsize=16, weight='bold', ha='center', va='bottom', pad=30)

plt.tight_layout()
plt.show()