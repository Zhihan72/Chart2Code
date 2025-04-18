import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Constructing the backstory and data
# Backstory: This funnel chart illustrates the progression of a tech startup from initial idea to acquiring Series A funding. 

# Stages of the funnel
stages = ["Idea & Pitching", "Team Building", "Product Development", "Early Trials", "Market Penetration", "Series A Funding"]
# Number of startups at each stage
startup_counts = [1000, 400, 200, 100, 50, 20]

# Proportion of startups at each stage relative to the initial count
widths = [count / max(startup_counts) for count in startup_counts]
colors = ['#3498db', '#1abc9c', '#9b59b6', '#e74c3c', '#f1c40f', '#e67e22']

# Calculating positions for each polygon to create a funnel effect
polygon_points = []
for i, width in enumerate(widths):
    bottom_width = width if i == len(widths) - 1 else widths[i + 1]
    top_left = ((1 - width) / 2, i)
    top_right = ((1 + width) / 2, i)
    bottom_left = ((1 - bottom_width) / 2, i + 1)
    bottom_right = ((1 + bottom_width) / 2, i + 1)
    polygon_points.append([top_left, top_right, bottom_right, bottom_left])

# Additional subplot data: average duration at each stage (in weeks)
average_durations = [4, 8, 16, 10, 14, 24] 

# Create the subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 12))
plt.subplots_adjust(wspace=0.4)

# Plotting the funnel chart
for i, (points, color) in enumerate(zip(polygon_points, colors)):
    edge_color = tuple(map(lambda x: x * 0.8, matplotlib.colors.to_rgba(color)[:3])) + (1,)
    funnel_polygon = patches.Polygon(points, closed=True, facecolor=color, edgecolor=edge_color, linewidth=2, alpha=0.85)
    ax1.add_patch(funnel_polygon)
    
    percentage = (startup_counts[i] / max(startup_counts)) * 100
    ax1.text(0.5, i + 0.5, f'{startup_counts[i]} Startups\n({percentage:.1f}%)', 
             va='center', ha='center', fontsize=12, color='black', fontweight='bold')

# Customizing the funnel chart
ax1.set_yticks([i + 0.5 for i in range(len(stages))])
ax1.set_yticklabels(stages, fontsize=14, fontweight='bold')
ax1.invert_yaxis()
ax1.set_xticks([])
ax1.set_xlim(0, 1)
ax1.set_title("Startup Progression Funnel:\nFrom Idea to Series A Funding", fontsize=18, fontweight='bold', pad=20)

# Plotting the bar chart for average durations
ax2.barh(stages, average_durations, color=colors, edgecolor='black')
ax2.set_xlabel('Duration (Weeks)', fontsize=14)
ax2.set_title("Average Duration per Stage", fontsize=18, fontweight='bold', pad=20)
ax2.set_xlim(0, max(average_durations) + 5)
ax2.invert_yaxis()
ax2.grid(axis='x', linestyle='--', alpha=0.7)

for i, v in enumerate(average_durations):
    ax2.text(v + 0.5, i, f'{v} weeks', va='center', fontsize=12, color='black', fontweight='bold')

# Optimize layout
plt.tight_layout()

# Display the combined chart
plt.show()