import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

stages = ["Conceptualization", "R&D", "Pilot Testing", "Market Testing", "Full Deployment"]
percentages = [100, 80, 65, 50, 40]
average_durations = [3, 6, 5, 4, 2]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
plt.subplots_adjust(wspace=0.3)

# Horizontal Bar Chart for Funnel Representation
ax1.barh(stages, percentages, color=['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00'], edgecolor='gray')
ax1.invert_yaxis()
ax1.set_xlim(0, 100)
ax1.set_xlabel("Percentage (%)", fontweight='bold')
ax1.set_title("Funnel Representation")

# Horizontal Bar Chart for Average Duration
ax2.barh(stages, average_durations, color='lightgreen', edgecolor='darkgreen', hatch='//')
ax2.invert_yaxis()
ax2.grid(axis='x', linestyle=':', alpha=0.5)
ax2.set_xlabel("Months", fontweight='bold')
ax2.set_title("Average Duration per Stage", style='italic')

plt.tight_layout()
plt.show()