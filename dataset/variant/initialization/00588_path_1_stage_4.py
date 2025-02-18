import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Data for the funnel stages
stages = ["Launch", "Booking", "Pre-Launch Training"]
customers = np.array([1200, 4500, 3000])

# Normalize data for funnel width
funnel_widths = customers / float(max(customers))

# Reverse data order for plotting from top to bottom
stages = stages[::-1]
funnel_widths = funnel_widths[::-1]

# Define colors for the stages
colors = ['#ff9999', '#ffcc99', '#ffeb99']

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 7))

# Plotting the funnel using rectangles
for i in range(len(stages)):
    x1 = -funnel_widths[i] / 2
    ax.add_patch(patches.Rectangle((x1, i), funnel_widths[i], 1, color=colors[i], alpha=0.8))
    ax.text(0, i + 0.5, f"{stages[i]}: {customers[::-1][i]}", fontsize=12, va='center', ha='center', color='white')

# Hide x-ticks and set limits
plt.xticks([])
plt.xlim([-0.5, 0.5])

# Remove borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Ensure layout is optimal
plt.tight_layout()

# Show plot
plt.show()