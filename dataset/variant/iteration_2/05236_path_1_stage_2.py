import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

stages = [
    "Introduction Phase",
    "User Attraction",
    "Community Building",
    "Prospect Collection",
    "Product Presentation",
    "Successful Turnovers"
]

audience_counts = [50000, 30000, 16000, 8000, 4000, 2000]
colors = ['#98df8a', '#ffbb78', '#ff9896', '#c5b0d5', '#c49c94', '#c7c7c7']

fig, ax = plt.subplots(figsize=(12, 10))
ax.set_xlim(0, max(audience_counts) + 5000)
ax.set_ylim(0, len(stages))

for i in range(len(stages) - 1):
    left = (max(audience_counts) - audience_counts[i])/2
    width_top = audience_counts[i]
    width_bottom = audience_counts[i + 1]
    height = 1
    
    trapezoid = patches.Polygon(
        [
            (left, i),
            (left + width_top, i),
            (left + (width_top + width_bottom)/2, i + height),
            (left + (width_top - width_bottom)/2, i + height)
        ],
        closed=True, color=colors[i]
    )
    ax.add_patch(trapezoid)

left = (max(audience_counts) - audience_counts[-1])/2
rectangle = patches.Rectangle(
    (left, len(stages) - 1), audience_counts[-1], 1, color=colors[-1]
)
ax.add_patch(rectangle)

for i, (stage, count) in enumerate(zip(stages, audience_counts)):
    ax.text(max(audience_counts)/2, i + 0.5, f'{stage}: {count}', va='center', ha='center',
            color='black', fontsize=12, fontweight='bold')

ax.set_xticks([])
ax.set_yticks([])
ax.set_title('Marketing Voyage Series\nUser Navigation Across Phases', 
             fontsize=16, fontweight='bold')

# Removing axis borders (spines)
for spine in ax.spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()