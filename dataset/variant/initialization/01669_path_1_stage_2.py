import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Data for the chart
stages = ["Conceptualization", "R&D", "Pilot Testing", "Market Testing", "Full Deployment"]
percentages = [100, 80, 65, 50, 40]
average_durations = [3, 6, 5, 4, 2]  # Months spent in each stage

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
plt.subplots_adjust(wspace=0.3)

consistent_color = '#1f77b4'

# Funnel Chart
total_height = 1.0
trapezoid_widths = np.array(percentages) * 0.01
trapezoid_heights = np.diff(np.linspace(0, total_height, len(stages) + 1))
x_positions = (1 - trapezoid_widths) / 2

for i in range(len(stages)):
    polygon = patches.Polygon(
        [
            (x_positions[i], sum(trapezoid_heights[:i])),
            (x_positions[i] + trapezoid_widths[i], sum(trapezoid_heights[:i])),
            (x_positions[i] + trapezoid_widths[i], sum(trapezoid_heights[:i + 1])),
            (x_positions[i], sum(trapezoid_heights[:i + 1]))
        ],
        closed=True,
        color=consistent_color,
        edgecolor='black'
    )
    ax1.add_patch(polygon)

ax1.set_xlim(0, 1)
ax1.set_ylim(0, total_height)
ax1.axis('off')

# Bar Chart for Average Duration
ax2.barh(stages, average_durations, color=consistent_color, edgecolor='black')
ax2.invert_yaxis()
ax2.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()