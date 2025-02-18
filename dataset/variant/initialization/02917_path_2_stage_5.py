import numpy as np
import matplotlib.pyplot as plt
from math import pi

skill_areas = [
    'Algorithm Design', 'Deployment', 'Collaboration &\nCommunication',
    'Model Evaluation', 'Data Preprocessing'
]

alpha_team_skills = [7, 5, 9, 6, 8]
beta_team_skills = [8, 6, 5, 7, 7]
gamma_team_skills = [6, 8, 4, 9, 6]
delta_team_skills = [9, 7, 6, 5, 8]

teams_data = {
    'Team Gamma': alpha_team_skills,
    'Squad Beta': beta_team_skills,
    'Delta Group': gamma_team_skills,
    'Alpha Crew': delta_team_skills
}

team_colors = {
    'Team Gamma': 'purple',
    'Squad Beta': 'teal',
    'Delta Group': 'magenta',
    'Alpha Crew': 'brown'
}

def create_radar_chart(title, team_data, labels, team_name, color):
    num_vars = len(labels)
    angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()

    team_data += team_data[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))
    plt.xticks(angles[:-1], labels, color='darkblue', size=10)
    ax.set_rlabel_position(-22.5)
    plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="black", size=8)
    plt.ylim(0, 10)

    ax.plot(angles, team_data, linewidth=1, linestyle='dashed', marker='o', markersize=5, label=team_name)
    ax.fill(angles, team_data, color=color)  # Removed alpha for full fill

    plt.title(title, size=16, color=color, y=1.1)
    plt.legend(loc='lower left')

for team_name, skill_levels in teams_data.items():
    create_radar_chart(f'{team_name} Skill Overview', skill_levels, skill_areas, team_name, team_colors[team_name])

plt.tight_layout()
plt.show()