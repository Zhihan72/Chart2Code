import matplotlib.pyplot as plt
import numpy as np

# Backstory: Space Missions Duration Comparison
# The chart compares the mission durations of different space agencies over the past decade.

# Data: Mission durations (in days) for different space agencies
nasa = [180, 250, 320, 150, 200, 280, 210]
esa = [220, 270, 180, 190, 240, 260, 230]
roscosmos = [150, 180, 210, 170, 140, 230, 200]
spacex = [110, 190, 270, 250, 210, 280, 200]
cnes = [90, 130, 110, 150, 160, 200, 170]

# Compile data into a list
data = [nasa, esa, roscosmos, spacex, cnes]
agencies = ['NASA', 'ESA', 'ROSCOSMOS', 'SpaceX', 'CNES']

# Create vertical box plot
fig, ax = plt.subplots(figsize=(12, 7))
box_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Plot with custom box colors and styles
bp = ax.boxplot(data, vert=True, patch_artist=True, notch=True, whis=1.5)

# Customize each box color
for patch, color in zip(bp['boxes'], box_colors):
    patch.set_facecolor(color)

# Set x-axis labels to match the space agencies
ax.set_xticklabels(agencies, fontsize=11)
ax.set_ylabel('Mission Duration (Days)', fontsize=12)
ax.set_title('Comparison of Space Missions Duration by Agency Over the Past Decade', fontsize=14, pad=20)

# Add grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap and enhance clarity
plt.tight_layout()

# Show plot
plt.show()