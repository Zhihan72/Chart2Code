import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Number of students at each stage (explicitly constructed data)
student_counts = np.array([1000, 850, 700, 600, 500, 400, 300, 250])

# Normalize widths for funnel-like appearance
widths = student_counts / student_counts[0]

# Define colors for each step
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f', '#e5c494', '#b3b3b3']

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 10))

# Add trapezoids for each stage of the funnel
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
ax.axis('off')  # Remove axes for a cleaner look

plt.tight_layout()
plt.show()