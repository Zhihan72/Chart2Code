import matplotlib.pyplot as plt
import numpy as np

# Define categories/attributes and teams' performance data
categories = ['Combat', 'Intelligence', 'Leadership', 'Technology', 'Logistics', 'Teamwork']
team_data = {
    'Alpha Squad': [7, 8, 6, 9, 5, 7],
    'Bravo Brigade': [6, 7, 8, 6, 7, 8],
    'Charlie Crew': [9, 6, 7, 8, 6, 7],
    'Delta Division': [8, 7, 6, 7, 9, 6]
}

# Number of variables
num_vars = len(categories)

# Compute angle for each category
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Repeat first angle to close the radar chart

# Set up radar chart framework
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each team's data on the radar chart with filled areas
for team, values in team_data.items():
    values += values[:1]  # Repeat the first value to close the loop
    ax.fill(angles, values, alpha=0.25, label=team)

# Customize the chart's appearance
ax.set_ylim(0, 10)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], color='grey', size=9)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, size=10, color='darkred')

# Title and legend
plt.title('Superhero Teams Performance in Meta City', size=15, weight='bold', color='darkred', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()