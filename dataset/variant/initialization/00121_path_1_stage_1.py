import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

steps = [
    "Enrollment",
    "Coursework\nCompletion",
    "Qualifying\nExam",
    "Mid-Candidacy\nReview",
    "Comprehensive\nExams",
    "Proposal\nDefense",
    "Dissertation\nDefense",
    "Graduation"
]

student_counts = np.array([1000, 850, 700, 600, 500, 400, 300, 250])
dropout_rates = 100 * (1 - student_counts[1:] / student_counts[:-1])
widths = student_counts / student_counts[0]
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f', '#e5c494', '#b3b3b3']

fig, ax = plt.subplots(figsize=(14, 10))

for i in range(len(steps)):
    top_width = widths[i-1] if i > 0 else 1.0
    bottom_width = widths[i]
    
    # Randomly varied line styles
    line_style = '-' if i % 2 == 0 else '--'
    
    trapezoid = patches.Polygon(
        [
            [(1 - top_width) / 2, i], [(1 + top_width) / 2, i], 
            [(1 + bottom_width) / 2, i + 1], [(1 - bottom_width) / 2, i + 1]
        ], closed=True, color=colors[i], edgecolor='black', linestyle=line_style
    )
    ax.add_patch(trapezoid)
    
    ax.text(0.5, i + 0.5, f"{steps[i]}\n{student_counts[i]} Students",
            ha='center', va='center', fontsize=11, color='black', weight='bold')

    if i > 0:
        ax.text(0.95, i + 0.5, f"Dropout: {dropout_rates[i-1]:.1f}%", 
                ha='right', va='center', fontsize=10, color='red', weight='bold')

ax.set_xlim(0, 1)
ax.set_ylim(0, len(steps))
ax.grid(visible=True, linestyle=':', linewidth=0.5)  # Grid added
ax.axis('on')  # Switch on axis for visibility

# Add Legend with altered properties
legend_elements = [patches.Patch(facecolor=colors[i], edgecolor='black',
                                 label=f"{steps[i]}: {student_counts[i]}")
                   for i in range(len(steps))]
ax.legend(handles=legend_elements, loc='upper right', fontsize=9, frameon=True, shadow=True, title="Stages", title_fontsize='13')

ax.set_title('The Path to PhD:\nAcademic Attrition in STEM Disciplines',
             fontsize=16, weight='bold', ha='center', va='bottom', pad=30)

plt.tight_layout()
plt.show()