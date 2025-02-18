import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# We are comparing the strategic performance attributes of different superhero teams in a hypothetical city named "Meta City". 
# Each team is evaluated across different parameters such as Combat, Intelligence, Leadership, Technology, Logistics, and Teamwork.

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
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot each team's data on the radar chart
for team, values in team_data.items():
    values += values[:1]  # Repeat the first value to close the loop
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=team)
    ax.fill(angles, values, alpha=0.25)

# Customize the chart's appearance
ax.set_ylim(0, 10)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], color='grey', size=9)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, size=10, color='darkred')

# Title and legend
plt.title('Superhero Teams Performance in Meta City', size=15, weight='bold', color='darkred', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10)

def create_bar_chart(ax, team_data, categories):
    index = np.arange(len(categories))
    bar_width = 0.2
    opacity = 0.8

    for i, (team, values) in enumerate(team_data.items()):
        ax.bar(index + i * bar_width, values[:-1], bar_width, 
               alpha=opacity, label=team, color=plt.cm.tab10(i))

    ax.set_xlabel('Performance Attributes', fontsize=10)
    ax.set_ylabel('Performance Level', fontsize=10)
    ax.set_title('Teams Performance Breakdown', fontsize=12, pad=20)
    ax.set_xticks(index + bar_width * (len(team_data) / 2 - 0.5))
    ax.set_xticklabels(categories, rotation=45, ha='right', fontsize=9)
    ax.set_ylim(0, 10)
    ax.legend()

# Create a subplot for bar chart next to the radar chart
ax2 = fig.add_subplot(122)
create_bar_chart(ax2, team_data, categories)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()