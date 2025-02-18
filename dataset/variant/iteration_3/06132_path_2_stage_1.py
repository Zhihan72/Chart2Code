import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Data for the stages and their respective values
stages = [
    "Initial Leads Captured",
    "Qualified Leads",
    "Product Demos Scheduled",
    "Interested Post-Demo",
    "Negotiation Phase",
    "Contracts Sent",
    "Contracts Signed",
    "Onboarding",
    "First Payment",
    "Continuous Subscription"
]

values = [1000, 750, 600, 500, 400, 350, 300, 250, 200, 150]
single_color = '#6baed6'  # Consistent color for all data groups

fig, ax = plt.subplots(figsize=(12, 9))

total_width = 12
width_ratios = [value / max(values) for value in values]
heights = 1.4

for i, (stage, value) in enumerate(zip(stages, values)):
    stage_width = width_ratios[i] * total_width
    x_offset = (total_width - stage_width) / 2
    y_position = -i * heights

    polygon = patches.FancyBboxPatch(
        (x_offset, y_position),
        stage_width, -heights,
        boxstyle="round,pad=0.05",
        edgecolor='black',
        facecolor=single_color,
        linewidth=1.5
    )
    ax.add_patch(polygon)

    annotation = f"{stage}\n{value} Leads"
    ax.text(total_width / 2, y_position - (heights / 2),
            annotation, ha='center', va='center',
            fontsize=10, color='white', fontweight='bold')

ax.set_xlim(0, total_width)
ax.set_ylim(-len(stages) * heights, 0)
ax.axis('off')

plt.title('Sales Journey Funnel of Tech Startup Gadget\nFrom Initial Leads to Continuous Subscription',
          fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()

plt.show()