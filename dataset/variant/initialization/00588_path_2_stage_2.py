import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

stages = ["Initial Interest", "Booking", "Launch"]
customers = np.array([10000, 4500, 1200])
funnel_widths = customers / float(max(customers))
stages = stages[::-1]
funnel_widths = funnel_widths[::-1]

# Apply a single color consistently across all stages
single_color = '#6699cc'

fig, ax = plt.subplots(figsize=(10, 5))

for i in range(len(stages)):
    x1 = -funnel_widths[i] / 2
    x2 = funnel_widths[i] / 2
    y1 = i
    y2 = i + 1
    ax.add_patch(patches.Rectangle((x1, y1), funnel_widths[i], 1, color=single_color, alpha=0.8))
    ax.text(0, i + 0.5, f"{stages[i]}: {customers[::-1][i]}", fontsize=12, va='center', ha='center', color='white')

plt.title("Galactic Adventures Customer Journey\nSpace Travel Experience", fontsize=16, fontweight='bold')
plt.xlabel('Proportion of Customers', fontsize=12)
plt.ylabel('Stages', fontsize=12)
plt.yticks(np.arange(0.5, len(stages) + 0.5), stages)
plt.xticks([])
plt.xlim([-0.5, 0.5])
plt.tight_layout()
plt.show()