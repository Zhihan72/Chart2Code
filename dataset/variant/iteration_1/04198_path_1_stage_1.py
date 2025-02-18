import matplotlib.pyplot as plt
import numpy as np

# Altered criteria labels
criteria = ['Communication', 'Shielding', 'Propulsion', 'Energy Efficiency', 'Navigation', 'Life Support']
num_criteria = len(criteria)

# Scores for each space agency
agency_scores = {
    'ESA': [7, 8, 7, 7, 8, 8],
    'NASA': [9, 8, 9, 8, 7, 9],
    'ISRO': [8, 7, 6, 7, 6, 8],
    'Roscosmos': [6, 5, 6, 7, 8, 7],
    'SpaceX': [9, 7, 8, 6, 7, 9]
}

# Number of agencies
num_agencies = len(agency_scores)

# Calculate the angles for each criteria
angles = np.linspace(0, 2 * np.pi, num_criteria, endpoint=False).tolist()
angles += angles[:1]

# Create a figure for plotting
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Define a dynamic color palette using a colormap
colors = plt.cm.plasma(np.linspace(0, 1, num_agencies))

# Plot each agency's technology data with enhancements
for idx, (agency_name, scores) in enumerate(agency_scores.items()):
    scores += scores[:1]
    ax.plot(angles, scores, color=colors[idx], linewidth=2, linestyle='-', label=agency_name)
    ax.fill(angles, scores, color=colors[idx], alpha=0.25)

    max_score_idx = np.argmax(scores[:-1])
    ax.text(angles[max_score_idx], scores[max_score_idx] + 0.5, f'{scores[max_score_idx]}', 
            horizontalalignment='center', color=colors[idx], fontsize=10)

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

# Altered chart title
plt.title("Space Agency Tech Survey:\nA Novel Examination", size=16, color='darkblue', y=1.1)

# Adjust legend location and aesthetics
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.2), fontsize=10, title="Agencies", title_fontsize=12)

# Improve layout to prevent overlap
plt.tight_layout()

# Show the radar chart
plt.show()