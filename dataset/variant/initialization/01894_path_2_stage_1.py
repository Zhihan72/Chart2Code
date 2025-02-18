import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Energy sources and their corresponding usage percentages
energy_sources = ['Wind', 'Fusion', 'Solar', 'Geothermal', 'Hydrogen', 'Fossil Fuels']
energy_usage = np.array([15, 20, 25, 10, 20, 10])

# Colors and patterns for each section of the donut pie chart
colors = ['#4682B4', '#FF6347', '#FFD700', '#32CD32', '#9400D3', '#D2691E']
patterns = ["||", "\\\\", "//", "-", "+", "x"]

# Explode the third and fourth slice
explode = (0, 0, 0.1, 0.1, 0, 0)

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

# Plot the pie chart with a hole in the center
wedges, texts, autotexts = ax.pie(
    energy_usage,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    explode=explode,
    wedgeprops=dict(width=0.3, edgecolor='w', linestyle='--', hatch=patterns[2]),
    shadow=True
)

plt.setp(autotexts, size=10, weight="bold", color='black')
plt.setp(texts, size=10, weight='bold')

plt.title(
    'Intergalactic Power Landscape:\nExploration of Energy Utilization in the 22nd Century',
    fontsize=16, weight='bold', pad=20
)

custom_patches = [Patch(facecolor=colors[i], hatch=patterns[i]) for i in range(len(colors))]
ax.legend(
    custom_patches, energy_sources, title="Energy Types",
    loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10
)

# Add a secondary pie chart inset
ax_inset = fig.add_axes([0.75, 0.7, 0.15, 0.15], aspect='equal')
inset_data = np.array([30, 20, 15, 25, 10])
inset_labels = ['2025', '2030', '2020', '2040', '2035']
inset_colors = ['#87CEFA', '#FFB6C1', '#FFE4B5', '#D8BFD8', '#98FB98']
ax_inset.pie(
    inset_data, labels=inset_labels, startangle=90, colors=inset_colors, 
    autopct='%1.0f%%', wedgeprops=dict(width=0.3, edgecolor='w')
)
ax_inset.set_title('Projection Trajectory', fontsize=8, weight='bold')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()