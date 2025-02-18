import matplotlib.pyplot as plt
import matplotlib.patches as patches

stages = [
    "Engagement",
    "Awareness Campaign",
    "Traffic Generation",
    "Convert to Customers",
    "Sales Pitch",
    "Lead Generation"
]

audience_counts = [16000, 50000, 30000, 2000, 4000, 8000]
colors = ['#ff9896', '#98df8a', '#ffbb78', '#c7c7c7', '#c49c94', '#c5b0d5']

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
        closed=True, color=colors[i], edgecolor='grey'
    )
    ax.add_patch(trapezoid)

left = (max(audience_counts) - audience_counts[-1])/2
rectangle = patches.Rectangle(
    (left, len(stages) - 1), audience_counts[-1], 1, color=colors[-1], edgecolor='grey'
)
ax.add_patch(rectangle)

ax.set_xticks([])
ax.set_yticks([])

for spine in ax.spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()