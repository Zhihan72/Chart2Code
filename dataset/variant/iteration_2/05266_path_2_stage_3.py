import matplotlib.pyplot as plt
import matplotlib.patches as patches

stages = ["Idea & Pitching", "Team Building", "Product Development", "Early Trials", "Market Penetration", "Series A Funding", "Scaling & Expansion"]
startup_counts = [1000, 400, 200, 100, 50, 20, 10]

widths = [count / max(startup_counts) for count in startup_counts]
colors = ['#3498db', '#1abc9c', '#9b59b6', '#e74c3c', '#f1c40f', '#e67e22', '#2ecc71']

polygon_points = []
for i, width in enumerate(widths):
    bottom_width = width if i == len(widths) - 1 else widths[i + 1]
    top_left = ((1 - width) / 2, i)
    top_right = ((1 + width) / 2, i)
    bottom_left = ((1 - bottom_width) / 2, i + 1)
    bottom_right = ((1 + bottom_width) / 2, i + 1)
    polygon_points.append([top_left, top_right, bottom_right, bottom_left])

average_durations = [4, 8, 16, 10, 14, 24, 30] 

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 14))
plt.subplots_adjust(wspace=0.4)

for i, (points, color) in enumerate(zip(polygon_points, colors)):
    funnel_polygon = patches.Polygon(points, closed=True, facecolor=color, linewidth=2, alpha=0.85)
    ax1.add_patch(funnel_polygon)

ax1.set_yticks([])
ax1.invert_yaxis()
ax1.set_xticks([])
ax1.set_xlim(0, 1)

ax2.barh(range(len(stages)), average_durations, color=colors)
ax2.set_xlim(0, max(average_durations) + 5)
ax2.invert_yaxis()
ax2.set_yticks([])

plt.tight_layout()
plt.show()