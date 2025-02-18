import matplotlib.pyplot as plt
import numpy as np

# Define the criteria
criteria = ['Propulsion', 'Navigation', 'Communication', 'Life Support', 'Shielding', 'Energy Efficiency']
num_criteria = len(criteria)

# Scores for each space agency
agency_scores = {
    'NASA': [9, 8, 9, 8, 7, 9],
    'ESA': [7, 8, 7, 7, 8, 8],
    'SpaceX': [9, 7, 8, 6, 7, 9],
    'Roscosmos': [6, 5, 6, 7, 8, 7],
    'ISRO': [8, 7, 6, 7, 6, 8]
}

# Calculate the angles for each criteria
angles = np.linspace(0, 2 * np.pi, num_criteria, endpoint=False).tolist()
angles += angles[:1]

# Create a figure for plotting
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Define a dynamic color palette using a colormap
colors = plt.cm.plasma(np.linspace(0, 1, len(agency_scores)))

# Plot each agency's technology data with filled areas
for idx, (agency_name, scores) in enumerate(agency_scores.items()):
    scores += scores[:1]  # Repeat the first score to close the loop
    ax.fill(angles, scores, color=colors[idx], alpha=0.4, label=agency_name)

# Set criteria labels and configure angular ticks
ax.set_xticks(angles[:-1])
ax.set_xticklabels(criteria, fontsize=11, fontweight='bold')

# Set the range of each axis
ax.set_ylim(0, 10)

# Style the grid lines
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, color='grey')
ax.xaxis.grid(True, linestyle='--', linewidth=0.5, color='grey')

# Customization of y-tick labels
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(["2", "4", "6", "8", "10"], fontsize=9, bbox=dict(facecolor='white', alpha=0.5, boxstyle='round,pad=0.3'))

# Add a multi-line title to the radar chart
plt.title("Assessing Space Technology Advancements:\nA Comparative Analysis Across Leading Space Agencies", 
          size=16, color='darkred', y=1.1)

# Adjust legend location and aesthetics
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.2), fontsize=10, title="Space Agencies", title_fontsize=12)

# Improve layout to prevent overlap
plt.tight_layout()

# Show the radar chart
plt.show()