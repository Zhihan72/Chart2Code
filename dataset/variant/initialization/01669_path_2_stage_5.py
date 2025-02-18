import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

stages = ["Idea Genesis", "Innovation Lab", "Customer Feedback", "Complete Rollout"]
percentages = [100, 80, 50, 40]
average_durations = [3, 6, 4, 2]

sorted_indices = np.argsort(average_durations)[::-1]
sorted_stages = [stages[i] for i in sorted_indices]
sorted_durations = [average_durations[i] for i in sorted_indices]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 12))
plt.subplots_adjust(hspace=0.3)

colors = ['#2ca02c', '#bcbd22', '#17becf', '#e377c2']

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
        color=colors[i],
        edgecolor='gray',
        linestyle='--'
    )
    ax1.add_patch(polygon)
    ax1.text(0.5, sum(trapezoid_heights[:i]) + trapezoid_heights[i] / 2,
             f'{stages[i]} - {percentages[i]}%', 
             ha='center', va='center', color='white', fontsize=12, fontweight='bold',
             bbox=dict(facecolor='black', edgecolor='none', alpha=0.7))

ax1.set_xlim(0, 1)
ax1.set_ylim(0, total_height)
ax1.axis('off')
ax1.set_title("Tech Initiative Pathway:\nFrom Thoughts to Action", fontsize=14, fontweight='bold', pad=20)

ax2.barh(sorted_stages, sorted_durations, color=colors, edgecolor='gray', linestyle=':')
ax2.set_xlabel('Timeframe (Months)', fontsize=12)
ax2.set_title("Stage Duration Overview", fontsize=14, fontweight='bold', pad=20)
ax2.set_xlim(0, max(sorted_durations) + 2)
ax2.invert_yaxis()
ax2.grid(axis='x', linestyle='-', alpha=0.4)
for i, v in enumerate(sorted_durations):
    ax2.text(v + 0.1, i, f'{v} mths', va='center', fontsize=10, color='gray')

plt.tight_layout()
plt.show()