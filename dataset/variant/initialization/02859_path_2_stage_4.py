import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

stages = [
    "Brainstorming &\nStrategy",
    "Preliminary Study",
    "Intensive R&D",
    "Model Drafting",
    "Trial Assessments",
    "Consumer Insight",
    "Campaign &\nBuzz Building",
    "Grand Opening",
    "Preliminary Client\nReactions",
    "Growth Burst",
    "User Trials",
    "Full-Scale Output"
]
values = [10000, 9000, 7500, 5000, 3000, 2500, 2000, 1500, 1200, 1000, 800, 500]
percentage_drops = [(values[i] - values[i+1]) / values[i] * 100 for i in range(len(values) - 1)]

# Altered color set and additional properties
colors = ['#e377c2', '#8c564b', '#1f77b4', '#ff7f0e', '#bcbd22', '#2ca02c', 
          '#9467bd', '#d62728', '#7f7f7f', '#17becf', '#aec7e8', '#ffbb78']

fig, ax = plt.subplots(figsize=(10, 10), facecolor='#f2f2f2')

y_start = 0

for i, (stage, value, color) in enumerate(zip(stages, values, colors)):
    width = value / float(max(values))
    left = (1 - width) / 2
    rect = Rectangle((left, y_start), width, 1, edgecolor='black', 
                     linestyle='-', linewidth=1.5, color=color, alpha=0.9)
    ax.add_patch(rect)
    
    ax.text(0.5, y_start + 0.5, f'{stage}\n{value} points', 
            fontsize=10, va='center', ha='center', color='black', fontstyle='italic')
    
    if i < len(percentage_drops):
        ax.text(1.02, y_start + 0.5, f'{percentage_drops[i]:.1f}% decrease', 
                fontsize=9, va='center', ha='left', color='gray')

    y_start += 1

ax.set_xlim(0, 1)
ax.set_ylim(0, len(stages))
ax.set_yticks([])
ax.set_xticks([])

ax.set_title("Product Development Path:\nNavigating From Idea to Market Triumph", 
             fontsize=16, fontweight='bold', pad=20, color='#333333')

ax.yaxis.grid(True, which='major', linestyle='-.', linewidth=0.7, color='lightgrey')

# Legend
handles = [Rectangle((0,0),1,1, color=color, alpha=0.9) for color in colors[:2]]
labels = ["Early Phase", "Later Phase"]
ax.legend(handles, labels, loc='upper right', fontsize=8, frameon=False)

plt.tight_layout()
plt.show()