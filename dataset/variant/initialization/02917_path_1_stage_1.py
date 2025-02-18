import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the skill areas
skill_areas = [
    'Data Preprocessing', 'Algorithm Design', 'Model Evaluation',
    'Deployment', 'Collaboration &\nCommunication'
]

# Define the skill levels for each team
alpha_team_skills = [8, 6, 7, 5, 9]
beta_team_skills = [5, 7, 8, 6, 7]
gamma_team_skills = [7, 9, 6, 4, 8]
delta_team_skills = [6, 5, 8, 7, 6]

# Combine data into a dictionary for easy plotting
teams_data = {
    'Alpha Team': alpha_team_skills,
    'Beta Team': beta_team_skills,
    'Gamma Team': gamma_team_skills,
    'Delta Team': delta_team_skills
}

# Define colors for each team
team_colors = {
    'Alpha Team': 'red',
    'Beta Team': 'blue',
    'Gamma Team': 'green',
    'Delta Team': 'orange'
}

# Create a radar chart function
def create_radar_chart(title, team_data, labels, color):
    num_vars = len(labels)
    angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
    team_data += team_data[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    plt.xticks(angles[:-1], labels, color='grey', size=9)
    plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=7)
    plt.ylim(0, 10)

    ax.plot(angles, team_data, linewidth=2, linestyle='solid')
    ax.fill(angles, team_data, color=color, alpha=0.3)

    plt.title(title, size=14, color=color, y=1.1)

# Plot for each team
for team_name, skill_levels in teams_data.items():
    create_radar_chart(f'{team_name} Skill Set', skill_levels, skill_areas, team_colors[team_name])

plt.tight_layout()
plt.show()