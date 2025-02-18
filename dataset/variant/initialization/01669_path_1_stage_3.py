import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

stages = ["Conceptualization", "R&D", "Pilot Testing", "Market Testing", "Full Deployment"]
percentages = [100, 80, 65, 50, 40]
average_durations = [3, 6, 5, 4, 2]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
plt.subplots_adjust(wspace=0.3)

# Change consistent color
funnel_colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00']

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
        color=funnel_colors[i],  # Different color for each stage
        edgecolor='gray',
        linestyle=':'  # Dashed border style
    )
    ax1.add_patch(polygon)
ax1.set_xlim(0, 1)
ax1.set_ylim(0, total_height)
ax1.axis('off')

# Bar Chart for Average Duration with stylistic changes
ax2.barh(stages, average_durations, color='lightgreen', edgecolor='darkgreen', hatch='//')
ax2.invert_yaxis()
ax2.grid(axis='x', linestyle=':', alpha=0.5)  # Dash-dotted grid
ax2.set_xlabel("Months", fontweight='bold')
ax2.set_title("Average Duration per Stage", style='italic')

plt.tight_layout()
plt.show()