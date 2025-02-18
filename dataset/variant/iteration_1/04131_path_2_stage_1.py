import matplotlib.pyplot as plt
import numpy as np

# Data for robotic arms and their performance
robot_ids = np.arange(1, 16)
operational_speeds = np.array([40, 50, 55, 70, 80, 90, 100, 110, 120, 125, 130, 135, 140, 145, 150])
items_processed = np.array([320, 400, 450, 560, 640, 720, 800, 880, 960, 1025, 1080, 1120, 1180, 1220, 1260])

# Performance metric and color mapping
performance_metric = items_processed / operational_speeds
colors = plt.cm.viridis((performance_metric - performance_metric.min()) / (performance_metric.max() - performance_metric.min()))

# Scatter plot with varied marker styles and edge colors
plt.figure(figsize=(14, 9))
sc = plt.scatter(operational_speeds, items_processed, 
                 c=colors, s=100 + performance_metric * 20, 
                 alpha=0.7, edgecolors='gray', linewidth=0.8, cmap='viridis', marker='^')

# Title and labels with altered font styles
plt.title("Robot Arm Performance in Automated Factory", fontsize=17, fontstyle='italic')
plt.xlabel("Operational Speed (units per hour)", fontsize=13, fontweight='light')
plt.ylabel("Items Processed per Day", fontsize=13, fontweight='light')

# Legend: Manipulated colorbar
cbar = plt.colorbar(sc)
cbar.set_label('Performance Metric (Items/Speed)', fontsize=11, weight='bold')

# Annotate each point with the robot ID
for i, txt in enumerate(robot_ids):
    plt.annotate(f"Arm {txt}", (operational_speeds[i], items_processed[i]), 
                 textcoords="offset points", xytext=(2, -10), ha='right', fontsize=8, color='navy')

# Altered grid style
plt.grid(True, linestyle='-.', linewidth=0.7, alpha=0.3)

# Modify axes properties for stylistic changes
plt.gca().spines['top'].set_visible(True)
plt.gca().spines['right'].set_visible(True)
plt.gca().spines['left'].set_color('gray')
plt.gca().spines['bottom'].set_color('gray')

plt.tight_layout()
plt.show()