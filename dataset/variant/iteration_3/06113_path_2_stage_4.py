import matplotlib.pyplot as plt
import numpy as np
from math import pi

categories = ['AI/ML', 'DevOps', 'Security', 'Database', 'Frontend', 'Backend']
num_vars = len(categories)

frontend_experts = [6, 5, 4, 9, 3, 8]
backend_enthusiasts = [4, 7, 9, 5, 6, 5]
database_geniuses = [9, 6, 3, 5, 4, 5]
devops_specialists = [5, 9, 8, 6, 3, 4]

proficiency_data = [frontend_experts, backend_enthusiasts, database_geniuses, devops_specialists]
teams = ["AI Aces", "Deployment Dynamos", "Cyber Sentinels", "Data Doctors"]

angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

def create_fill_area_radar_chart(ax, data, labels, color):
    for team_data, team_name in zip(data, teams):
        team_data += team_data[:1]
        ax.fill(angles, team_data, alpha=0.4, color=color, label=team_name)
    
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylim(0, 10)
    ax.set_yticks(range(0, 11, 2))

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
consistent_color = '#1f77b4'

create_fill_area_radar_chart(ax, proficiency_data, categories, consistent_color)

plt.title("Skill Proficiency Radar for Diverse IT Sectors", fontsize=16, pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=12)
plt.tight_layout()
plt.show()