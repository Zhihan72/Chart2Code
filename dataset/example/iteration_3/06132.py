import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Backstory:
# The chart will depict the sales journey of a tech startup's new gadget, from initial leads to finalized sales.

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
colors = ['#6baed6', '#3182bd', '#08519c', '#bdd7e7', '#bae4b3', '#74c476', '#31a354', '#006d2c', '#fd8d3c', '#e6550d']

# Create the funnel chart
fig, ax = plt.subplots(figsize=(12, 9))

# Calculate the width ratio for each stage (funnel effect)
total_width = 12
width_ratios = [value / max(values) for value in values]
heights = 1.4

# Plot each stage
for i, (stage, value) in enumerate(zip(stages, values)):
    stage_width = width_ratios[i] * total_width
    x_offset = (total_width - stage_width) / 2
    y_position = -i * heights

    polygon = patches.FancyBboxPatch(
        (x_offset, y_position),
        stage_width, -heights,
        boxstyle="round,pad=0.05",
        edgecolor='black',
        facecolor=colors[i],
        linewidth=1.5
    )
    ax.add_patch(polygon)

    # Annotate each stage
    annotation = f"{stage}\n{value} Leads"
    ax.text(total_width / 2, y_position - (heights / 2),
            annotation, ha='center', va='center',
            fontsize=10, color='white', fontweight='bold')

# Customize layout
ax.set_xlim(0, total_width)
ax.set_ylim(-len(stages) * heights, 0)
ax.axis('off')

# Title for the chart
plt.title('Sales Journey Funnel of Tech Startup Gadget\nFrom Initial Leads to Continuous Subscription',
          fontsize=16, fontweight='bold', pad=20)

# Automatically adjust layout to avoid text overlap and enhance visualization
plt.tight_layout()

# Display the plot
plt.show()