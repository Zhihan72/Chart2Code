import matplotlib.pyplot as plt
import numpy as np

# Data for the original funnel chart
stages = ["Conceptualization", "R&D", "Pilot Testing", "Market Testing", "Full Deployment"]
percentages = [100, 80, 65, 50, 40]

# Data for the new subplot
average_durations = [3, 6, 5, 4, 2]  # Months spent in each stage

# Sort the stages and durations based on the average_durations for the bar chart
sorted_indices = np.argsort(average_durations)[::-1]
sorted_stages = [stages[i] for i in sorted_indices]
sorted_durations = [average_durations[i] for i in sorted_indices]

# Create the subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
plt.subplots_adjust(wspace=0.3)

# Colors for consistency
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Original Funnel Chart
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
        edgecolor='black'
    )
    ax1.add_patch(polygon)
    ax1.text(0.5, sum(trapezoid_heights[:i]) + trapezoid_heights[i] / 2, 
             f'{stages[i]}: {percentages[i]}%', 
             ha='center', va='center', color='white', fontsize=12, fontweight='bold',
             bbox=dict(facecolor='black', edgecolor='none', alpha=0.5))

ax1.set_xlim(0, 1)
ax1.set_ylim(0, total_height)
ax1.axis('off')
ax1.set_title("AI Project Funnel:\nFrom Concept to Deployment", fontsize=14, fontweight='bold', pad=20)

# Sorted Bar Chart for Average Duration
ax2.barh(sorted_stages, sorted_durations, color=colors, edgecolor='black')
ax2.set_xlabel('Duration (Months)', fontsize=12)
ax2.set_title("Average Duration per Stage (Sorted)", fontsize=14, fontweight='bold', pad=20)
ax2.set_xlim(0, max(sorted_durations) + 2)
ax2.invert_yaxis()
ax2.grid(axis='x', linestyle='--', alpha=0.7)
for i, v in enumerate(sorted_durations):
    ax2.text(v + 0.1, i, f'{v} months', va='center', fontsize=10, color='black')

plt.tight_layout()
plt.show()