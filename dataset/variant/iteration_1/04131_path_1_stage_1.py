import matplotlib.pyplot as plt
import numpy as np

# Data with modified order to preserve the dimensional structure
robot_ids = np.arange(1, 16)
operational_speeds = np.array([55, 125, 100, 90, 130, 80, 120, 70, 145, 110, 135, 50, 40, 150, 140])
items_processed = np.array([450, 1025, 800, 720, 1080, 640, 960, 560, 1220, 880, 1120, 400, 320, 1260, 1180])

performance_metric = items_processed / operational_speeds
colors = plt.cm.plasma((performance_metric - performance_metric.min()) / (performance_metric.max() - performance_metric.min()))

# Scatter plotting
plt.figure(figsize=(14, 9))
sc = plt.scatter(operational_speeds, items_processed, 
                 c=colors, s=100 + performance_metric * 20, 
                 alpha=0.8, edgecolors='w', linewidth=0.5, cmap='plasma')

# Title and labels
plt.title("Robot Arm Performance in Automated Factory", fontsize=18, fontweight='bold')
plt.xlabel("Operational Speed (units per hour)", fontsize=14)
plt.ylabel("Items Processed per Day", fontsize=14)

# Adding legend based on performance metric
cbar = plt.colorbar(sc)
cbar.set_label('Performance Metric (Items/Speed)', fontsize=12)

# Annotate each point with the robot ID
for i, txt in enumerate(robot_ids):
    plt.annotate(f"Arm {txt}", (operational_speeds[i], items_processed[i]), 
                 textcoords="offset points", xytext=(5, 5), ha='center', fontsize=9, color='darkred')

# Adding grid for better visualization
plt.grid(True, linestyle='--', alpha=0.6)

# Ensuring layout adjusts automatically
plt.tight_layout()

# Showing the plot
plt.show()