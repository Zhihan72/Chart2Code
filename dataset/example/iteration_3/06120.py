import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from math import pi

# Define categories for astrological qualities
categories = ['Intellect', 'Physical', 'Emotional', 'Spiritual', 'Social']

# Data for different zodiac signs (scores ranging from 1 to 10)
aries = [8, 7, 5, 6, 7]
taurus = [6, 6, 8, 7, 7]
gemini = [9, 6, 5, 6, 8]
cancer = [5, 5, 9, 6, 8]
leo = [7, 8, 6, 5, 8]

# Combine all zodiac data
zodiac_data = np.array([aries, taurus, gemini, cancer, leo])
labels = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo']

# Number of variables
num_vars = len(categories)

# Compute angle of each axis (in radians)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
# Complete the loop
angles += angles[:1]

# Function to plot radar charts
def plot_radar(ax, data, colors, labels):
    for idx, d in enumerate(data):
        values = d.tolist()
        values += values[:1]
        ax.plot(angles, values, color=colors[idx], linewidth=2, linestyle='solid')
        ax.fill(angles, values, color=colors[idx], alpha=0.25, label=labels[idx])

# Initialize the radar plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot radar chart for different zodiac signs
colors = ['#ff5733', '#4CAF50', '#2196F3', '#FFC107', '#9C27B0']
plot_radar(ax, zodiac_data, colors, labels)

# Add variable labels
plt.xticks(angles[:-1], categories, color='dimgray', size=10)

# Add custom radial range labels
ax.set_yticklabels([])
ax.set_ylim(0, 10)
for y in range(2, 11, 2):
    ax.add_patch(Circle((0,0), y, transform=ax.transData._b, color='lightgrey', alpha=0.2, zorder=0))
    ax.text(y, -y*0.05, str(y), horizontalalignment='center', color='grey', size=10)

# Add a title
ax.set_title('Astrological Qualities Analysis\nRadar Chart of Zodiac Signs', size=14, fontweight='bold', pad=30)

# Add a legend with adjusted location
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=9)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the radar chart
plt.show()