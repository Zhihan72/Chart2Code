import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Original stages and values
stages_main = [
    "Leads",
    "Qualified",
    "Demos",
    "Interested",
    "Negotiation",
    "Sent",
    "Signed",
    "Onboard",
    "Payment",
    "Subscription"
]

values_main = [1000, 750, 600, 500, 400, 350, 300, 250, 200, 150]

# Additional stages and values for a new series
stages_followup = [
    "Recontacted",
    "Reviewed",
    "Proposal Sent",
    "Final Negotiation",
    "Deal Closed"
]

values_followup = [80, 70, 60, 40, 30]

# Colors for the two different series
color_main = '#3182bd'
color_followup = '#e6550d'

# Prepare the plotting area
fig, ax = plt.subplots(figsize=(12, 12))

# Scaling parameters
total_width = 12
heights = 1.4

# Function to plot a set of stages and values
def plot_series(stages, values, color, start_offset):
    width_ratios = [value / max(values) for value in values]
    
    for i, (stage, value) in enumerate(zip(stages, values)):
        stage_width = width_ratios[i] * total_width
        x_offset = (total_width - stage_width) / 2
        y_position = -(i + start_offset) * heights

        polygon = patches.FancyBboxPatch(
            (x_offset, y_position),
            stage_width, -heights,
            boxstyle="round,pad=0.05",
            edgecolor='black',
            facecolor=color,
            linewidth=1.5
        )
        ax.add_patch(polygon)

        annotation = f"{stage}\n{value}"
        ax.text(total_width / 2, y_position - (heights / 2),
                annotation, ha='center', va='center',
                fontsize=10, color='white', fontweight='bold')

# Plot the main series
plot_series(stages_main, values_main, color_main, 0)

# Plot the follow-up series
plot_series(stages_followup, values_followup, color_followup, len(stages_main))

ax.set_xlim(0, total_width)
ax.set_ylim(-(len(stages_main) + len(stages_followup)) * heights, 0)
ax.axis('off')

plt.tight_layout()
plt.show()