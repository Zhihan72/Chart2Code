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

# New color set
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
          '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#aec7e8', '#ffbb78']

fig, ax = plt.subplots(figsize=(10, 10))

y_start = 0

for i, (stage, value, color) in enumerate(zip(stages, values, colors)):
    width = value / float(max(values))
    left = (1 - width) / 2
    rect = Rectangle((left, y_start), width, 1, color=color, alpha=0.9)
    ax.add_patch(rect)
    
    ax.text(0.5, y_start + 0.5, f'{stage}\n{value} points', 
            fontsize=10, va='center', ha='center', color='black')
    
    if i < len(percentage_drops):
        ax.text(1.02, y_start + 0.5, f'{percentage_drops[i]:.1f}% decrease', 
                fontsize=9, va='center', ha='left', color='gray')
    
    y_start += 1

ax.set_xlim(0, 1)
ax.set_ylim(0, len(stages))
ax.set_yticks([])
ax.set_xticks([])

ax.set_title("Product Development Path:\nNavigating From Idea to Market Triumph", 
             fontsize=14, fontweight='bold', pad=15)

ax.yaxis.grid(True, which='major', linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.show()