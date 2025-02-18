import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

# Updated stage labels
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

colors = ['#FF5733', '#FF6F33', '#FF8D33', '#FFA833', '#FFC733', '#E1FF33', 
          '#8DFF33', '#33FF57', '#33FF8D', '#33FFC7', '#33E1FF', '#33B8FF']

fig, ax = plt.subplots(figsize=(10, 10))

y_start = 0

# Updating text elements in the chart
for i, (stage, value, color) in enumerate(zip(stages, values, colors)):
    width = value / float(max(values))
    left = (1 - width) / 2

    rect = Rectangle((left, y_start), width, 1, color=color, alpha=0.9)
    ax.add_patch(rect)
    
    # Random alteration of the group label text
    ax.text(0.5, y_start + 0.5, f'{stage}\n{value} points', 
            fontsize=10, va='center', ha='center', color='black')
    
    if i < len(percentage_drops):
        # Slight change in the drop description
        ax.text(1.02, y_start + 0.5, f'{percentage_drops[i]:.1f}% decrease', 
                fontsize=9, va='center', ha='left', color='gray')
    
    y_start += 1

ax.set_xlim(0, 1)
ax.set_ylim(0, len(stages))
ax.set_yticks([])
ax.set_xticks([])

# Altered title text
ax.set_title("Product Development Path:\nNavigating From Idea to Market Triumph", 
             fontsize=14, fontweight='bold', pad=15)

ax.yaxis.grid(True, which='major', linestyle='--', linewidth=0.5)

plt.tight_layout()

plt.show()