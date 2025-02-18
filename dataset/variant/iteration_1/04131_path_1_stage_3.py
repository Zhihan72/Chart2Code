import matplotlib.pyplot as plt
import numpy as np

robot_ids = np.arange(1, 16)
operational_speeds = np.array([55, 125, 100, 90, 130, 80, 120, 70, 145, 110, 135, 50, 40, 150, 140])
items_processed = np.array([450, 1025, 800, 720, 1080, 640, 960, 560, 1220, 880, 1120, 400, 320, 1260, 1180])

performance_metric = items_processed / operational_speeds
colors = plt.cm.viridis((performance_metric - performance_metric.min()) / (performance_metric.max() - performance_metric.min()))

plt.figure(figsize=(14, 9))
sc = plt.scatter(operational_speeds, items_processed, 
                 c=colors, s=120 + performance_metric * 30, 
                 alpha=0.75, edgecolors='b', linewidth=1.0, cmap='viridis', marker='^')

# Randomly altered chart textual elements
plt.title("Efficiency of Automated Units (Styled Variance)", fontsize=18, fontweight='bold')
plt.xlabel("Pace", fontsize=14)
plt.ylabel("Output Generated", fontsize=14)

cbar = plt.colorbar(sc)
cbar.set_label('Efficiency Index', fontsize=12)

for i, txt in enumerate(robot_ids):
    plt.annotate(f"Bot{txt}", (operational_speeds[i], items_processed[i]), 
                 textcoords="offset points", xytext=(-10, -10), ha='right', fontsize=9, color='darkblue')

plt.grid(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.tight_layout()
plt.show()