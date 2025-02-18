import numpy as np
import matplotlib.pyplot as plt

categories = ['Renewable Energy', 'Biodiversity', 'Water Conservation', 'Green Transportation']
values = np.array([85, 65, 90, 60])
values = np.concatenate((values, [values[0]]))

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Randomly altering stylistic elements
fill_color = 'lightgreen'
line_style = '--'
marker_shape = 'o'
line_color = 'darkred'
legend_location = 'lower left'
grid_option = True

ax.fill(angles, values, color=fill_color, alpha=0.4)
ax.plot(angles, values, line_style + marker_shape, color=line_color, linewidth=2)

ax.set_yticklabels([])
ax.set_xticks([])  # Remove the tick marks as textual elements are not needed
ax.set_yticklabels([])  # Remove y-axis labels
ax.set_ylim(0, 100)

# Remove the title as it is a textual element
# plt.title("EcoVision: Sustainability Index 2040\nPerformance of EcoNation",
#           size=16, color='darkblue', weight='bold', pad=20)

# Remove the legend as it contains text
# ax.legend(['Performance Score'], loc=legend_location, fontsize='medium', frameon=True)

if grid_option:
    ax.grid(True)

plt.tight_layout()
plt.show()