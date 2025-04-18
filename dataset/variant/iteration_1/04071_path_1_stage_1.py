import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

steps = [
    "Initial Inquiry", "Test Drive Scheduled", "Test Drive Completed", 
    "Price Negotiation", "Financing Options", "Purchase Agreement Signed", 
    "Vehicle Delivered", "Ownership Beyond 6 Months"
]

consumer_counts = np.array([5000, 3800, 3500, 2900, 2600, 2200, 2000, 1700])
widths = consumer_counts / consumer_counts[0]
colors = ['#91bfdb', '#4575b4', '#91bfdb', '#74add1', '#abd9e9', '#e0f3f8', '#fee090', '#fc8d59']

fig, ax = plt.subplots(figsize=(12, 10))

for i in range(len(steps)):
    top_width = widths[i-1] if i > 0 else 1.0
    bottom_width = widths[i]
    trapezoid = patches.Polygon(
        [
            [(1 - top_width) / 2, i], [(1 + top_width) / 2, i], 
            [(1 + bottom_width) / 2, i + 1], [(1 - bottom_width) / 2, i + 1]
        ], closed=True, color=colors[i]
    )
    ax.add_patch(trapezoid)
    ax.text(0.5, i + 0.5, f"{steps[i]}\n{consumer_counts[i]} Consumers",
            ha='center', va='center', fontsize=11, color='black', weight='bold')

ax.set_xlim(0, 1)
ax.set_ylim(0, len(steps))
ax.axis('off')

plt.tight_layout()
plt.show()