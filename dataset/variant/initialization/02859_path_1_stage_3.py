import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

stages = [
    "Ideation &\nConceptualization",
    "Initial Research",
    "Detailed R&D",
    "Prototype\nDevelopment",
    "Prototype\nTesting",
    "Focus Group\nAnalysis",
    "Marketing &\nPre-Launch Hype",
    "Product\nLaunch",
    "Initial Sales\nFeedback",
    "Market\nPenetration",
    "Customer Support\nSetup",
    "Scaling Up",
    "Feedback Loop\nImprovements"
]
values = [10000, 9000, 7500, 5000, 3000, 2500, 2000, 1500, 1200, 1000, 800, 600, 500]

percentage_drops = [(values[i] - values[i+1]) / values[i] * 100 for i in range(len(values) - 1)]

colors = ['#F15854', '#DECF3F', '#B276B2', '#B2912F', '#F17CB0', '#60BD68',
          '#FAA43A', '#5DA5DA', '#4D4D4D', '#1A85FF', '#FF6666', '#FFCC66', '#66FF66']

fig, ax = plt.subplots(figsize=(10, 12))

y_start = 0

for i, (stage, value, color) in enumerate(zip(stages, values, colors)):
    width = value / float(max(values))
    left = (1 - width) / 2

    rect = Rectangle((left, y_start), width, 1, color=color, alpha=0.7, linestyle='dotted', linewidth=2)
    ax.add_patch(rect)

    ax.text(0.5, y_start + 0.5, f'{stage}\n{value} engagements', 
            fontsize=10, va='center', ha='center', color='black')
    
    if i < len(percentage_drops):
        ax.text(1.02, y_start + 0.5, f'{percentage_drops[i]}:.1f% drop', 
                fontsize=9, va='center', ha='left', color='gray')
    
    y_start += 1

ax.set_xlim(0, 1)
ax.set_ylim(0, len(stages))
ax.set_yticks([])
ax.set_xticks([])
ax.set_title("Tech Product Journey:\nA Complex Funnel From Concept to Market Success", 
             fontsize=14, fontweight='bold', pad=15)

ax.yaxis.grid(False)

plt.tight_layout()
plt.show()