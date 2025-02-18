import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

values = [10000, 9000, 7500, 5000, 3000, 2500, 2000, 1500, 1200, 1000, 800, 600, 500]

colors = ['#F15854', '#DECF3F', '#B276B2', '#B2912F', '#F17CB0', '#60BD68',
          '#FAA43A', '#5DA5DA', '#4D4D4D', '#1A85FF', '#FF6666', '#FFCC66', '#66FF66']

fig, ax = plt.subplots(figsize=(10, 12))

y_start = 0

for i, (value, color) in enumerate(zip(values, colors)):
    width = value / float(max(values))
    left = (1 - width) / 2

    rect = Rectangle((left, y_start), width, 1, color=color, alpha=0.7, linestyle='dotted', linewidth=2)
    ax.add_patch(rect)

    y_start += 1

ax.set_xlim(0, 1)
ax.set_ylim(0, len(values))
ax.set_yticks([])
ax.set_xticks([])

ax.yaxis.grid(False)

plt.tight_layout()
plt.show()