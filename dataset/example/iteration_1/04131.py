import matplotlib.pyplot as plt
import numpy as np

# Backstory: This chart intends to visualize the performance of a set of robotic arms in an automated factory. 
# Each robot arm is measured by its operational speed and the number of items processed in a day.
# We have experimental results from 15 different robot arms.

# Data: Robot Arm IDs, their corresponding Operational Speeds (units per hour) and Items Processed per day.
robot_ids = np.arange(1, 16)
operational_speeds = np.array([40, 50, 55, 70, 80, 90, 100, 110, 120, 125, 130, 135, 140, 145, 150])
items_processed = np.array([320, 400, 450, 560, 640, 720, 800, 880, 960, 1025, 1080, 1120, 1180, 1220, 1260])

# Color based on a performance metric (speed to items ratio, higher is better)
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