import numpy as np
import matplotlib.pyplot as plt

categories = ['Renewable Energy', 'Biodiversity', 'Water Conservation', 'Green Transportation']
values = np.array([85, 65, 90, 60])
values = np.concatenate((values, [values[0]]))

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Define a new set of colors for the radar chart
new_fill_color = 'cornflowerblue'

# Fill the area within the radar chart with the new color
ax.fill(angles, values, color=new_fill_color, alpha=0.4)

ax.set_xticks([])  # Remove the tick marks
ax.set_yticklabels([])  # Remove y-axis labels
ax.set_ylim(0, 100)

ax.grid(True)

plt.tight_layout()
plt.show()