import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Stages and Data
stages = ["Idea & Pitching", "Team Building", "Product Development", "Early Trials", "Market Penetration", "Series A Funding", "Scaling"]
startup_counts = [1000, 400, 200, 100, 50, 20, 10]
average_durations = [4, 8, 16, 10, 14, 24, 30]

widths = [count / max(startup_counts) for count in startup_counts]
colors = ['#3498db', '#1abc9c', '#9b59b6', '#e74c3c', '#f1c40f', '#e67e22', '#34495e']

polygon_points = []
for i, width in enumerate(widths):
    bottom_width = width if i == len(widths) - 1 else widths[i + 1]
    top_left = ((1 - width) / 2, i)
    top_right = ((1 + width) / 2, i)
    bottom_left = ((1 - bottom_width) / 2, i + 1)
    bottom_right = ((1 + bottom_width) / 2, i + 1)
    polygon_points.append([top_left, top_right, bottom_right, bottom_left])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 12))
plt.subplots_adjust(wspace=0.4)

# Left subplot: Startup Progression Funnel
for i, (points, color) in enumerate(zip(polygon_points, colors)):
    edge_color = tuple(map(lambda x: x * 0.5, matplotlib.colors.to_rgba(color)[:3])) + (1,)
    funnel_polygon = patches.Polygon(points, closed=True, facecolor='none', edgecolor=edge_color, linewidth=3, linestyle='-.', alpha=0.85)
    ax1.add_patch(funnel_polygon)

ax1.set_yticks([i + 0.5 for i in range(len(stages))])
ax1.set_yticklabels(['']*len(stages))
ax1.invert_yaxis()
ax1.set_xticks([])
ax1.set_xlim(0, 1)

# Right subplot: Horizontal Bar Chart
ax2.barh(stages, average_durations, color=colors, edgecolor='black', hatch='//', linestyle='-', linewidth=1.5)
ax2.set_yticklabels(['']*len(stages))
ax2.set_xticks([])
ax2.set_xlim(0, max(average_durations) + 5)
ax2.invert_yaxis()
ax2.grid(axis='x', linestyle='-.', alpha=0.9)

plt.tight_layout()
plt.show()