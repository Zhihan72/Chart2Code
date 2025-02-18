import numpy as np
import matplotlib.pyplot as plt
from math import pi

skill_areas = ['Preprocess', 'Design', 'Eval', 'Deploy', 'Comm']

alpha_team_skills = [8, 6, 7, 5, 9]
beta_team_skills = [5, 7, 8, 6, 7]
delta_team_skills = [6, 5, 8, 7, 6]

teams_data = {
    'Alpha': alpha_team_skills,
    'Beta': beta_team_skills,
    'Delta': delta_team_skills
}

consistent_color = 'purple'

def create_radar_chart(title, team_data, labels):
    num_vars = len(labels)
    angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
    team_data += team_data[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    plt.xticks(angles[:-1], labels, color='grey', size=9)
    plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=7)
    plt.ylim(0, 10)

    ax.plot(angles, team_data, linewidth=2, linestyle='solid')
    ax.fill(angles, team_data, color=consistent_color, alpha=0.3)
    
    plt.title(title, size=12, color=consistent_color, y=1.1)

for team_name, skill_levels in teams_data.items():
    create_radar_chart(f'{team_name}', skill_levels, skill_areas)

plt.tight_layout()
plt.show()