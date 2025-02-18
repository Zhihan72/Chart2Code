import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

steps = [
    "Initial Inquiry", "Test Drive Scheduled", 
    "Price Negotiation", "Financing Options", 
    "Purchase Agreement Signed", "Vehicle Delivered", 
    "Ownership Beyond 6 Months"
]

consumer_counts = np.array([5000, 3800, 2900, 2600, 2200, 2000, 1700])
widths = consumer_counts / consumer_counts[0]
single_color = '#4575b4'  # Applying a single consistent color

fig, ax = plt.subplots(figsize=(12, 10))

for i in range(len(steps)):
    top_width = widths[i-1] if i > 0 else 1.0
    bottom_width = widths[i]
    trapezoid = patches.Polygon(
        [
            [(1 - top_width) / 2, i], [(1 + top_width) / 2, i], 
            [(1 + bottom_width) / 2, i + 1], [(1 - bottom_width) / 2, i + 1]
        ], closed=True, color=single_color  # Using the single consistent color
    )
    ax.add_patch(trapezoid)
    ax.text(0.5, i + 0.5, f"{steps[i]}\n{consumer_counts[i]} Consumers",
            ha='center', va='center', fontsize=11, color='black', weight='bold')

ax.set_xlim(0, 1)
ax.set_ylim(0, len(steps))
ax.axis('off')

plt.tight_layout()
plt.show()