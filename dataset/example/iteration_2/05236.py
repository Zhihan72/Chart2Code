import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Backstory: This chart represents the stages of a digital marketing campaign for launching a new beverage product.
stages = [
    "Awareness Campaign",
    "Traffic Generation",
    "Engagement",
    "Lead Generation",
    "Sales Pitch",
    "Convert to Customers"
]

# Data corresponding to number of people reached or engaged at each stage
audience_counts = [50000, 30000, 16000, 8000, 4000, 2000]

# Colors for each stage
colors = ['#98df8a', '#ffbb78', '#ff9896', '#c5b0d5', '#c49c94', '#c7c7c7']

fig, ax = plt.subplots(figsize=(12, 10))
ax.set_xlim(0, max(audience_counts) + 5000)
ax.set_ylim(0, len(stages))

# Plot each section of the funnel
for i in range(len(stages) - 1):
    left = (max(audience_counts) - audience_counts[i])/2
    width_top = audience_counts[i]
    width_bottom = audience_counts[i + 1]
    height = 1
    
    # Draw trapezoids
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

# Last stage (rectangle)
left = (max(audience_counts) - audience_counts[-1])/2
rectangle = patches.Rectangle(
    (left, len(stages) - 1), audience_counts[-1], 1, color=colors[-1], edgecolor='grey'
)
ax.add_patch(rectangle)

# Label each section
for i, (stage, count) in enumerate(zip(stages, audience_counts)):
    ax.text(max(audience_counts)/2, i + 0.5, f'{stage}: {count}', va='center', ha='center',
            color='black', fontsize=12, fontweight='bold')

# Axis formatting
ax.set_xticks([])
ax.set_yticks([])
ax.set_title('Digital Marketing Campaign Funnel for New Beverage Launch\nAudience Journey Through Campaign Stages', 
             fontsize=16, fontweight='bold')

# Remove spines to enhance the funnel look
for spine in ax.spines.values():
    spine.set_visible(False)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()