import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Backstory:
# The chart represents the diagnostic ratings of different types of spacecraft used by the Intergalactic Fleet.
# The ratings are based on six critical parameters: Speed, Armor, Weaponry, Maneuverability, Stealth, and Cargo.

# Define the spacecraft types and their attributes
spacecraft_types = ['Fighter', 'Bomber', 'Destroyer', 'Cruiser', 'Scout']
attributes = ['Speed', 'Armor', 'Weaponry', 'Maneuverability', 'Stealth', 'Cargo']

# Define the attribute values for each spacecraft type
spacecraft_data = {
    'Fighter': [9, 6, 8, 10, 7, 3],
    'Bomber': [6, 9, 10, 5, 4, 7],
    'Destroyer': [4, 10, 9, 3, 5, 6],
    'Cruiser': [5, 8, 6, 4, 3, 10],
    'Scout': [10, 4, 5, 9, 8, 2]
}

# Number of attributes
num_attributes = len(attributes)

# Calculate angle for each attribute on the radar chart
angles = np.linspace(0, 2 * pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the circle

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw one axis per attribute and add labels
ax.set_theta_offset(pi / 2)  # Rotate chart so the first attribute is at the top
ax.set_theta_direction(-1)  # Draw the chart clockwise
plt.xticks(angles[:-1], attributes, color='grey', size=12)

# Draw ylabels
ax.set_rscale('linear')
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color='grey', size=10)
plt.ylim(0, 10)

# Plot data and fill
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']  # Colors for the respective spacecrafts
for idx, (spacecraft, values) in enumerate(spacecraft_data.items()):
    values += values[:1]  # Repeat the first value to close the circle
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=spacecraft, color=colors[idx])
    ax.fill(angles, values, color=colors[idx], alpha=0.25)

# Add a title and legend
plt.title("Diagnostic Ratings of Intergalactic Fleet Spacecraft", size=15, fontweight='bold', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()