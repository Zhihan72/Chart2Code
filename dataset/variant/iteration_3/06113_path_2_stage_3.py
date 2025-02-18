import matplotlib.pyplot as plt
import numpy as np
from math import pi

categories = ['Frontend', 'Backend', 'Database', 'DevOps', 'AI/ML', 'Security']
num_vars = len(categories)

# Randomly altering the data within each group while preserving the structure
frontend_gurus = [6, 5, 4, 9, 3, 8]  # Altered data from DevOps Ninjas
backend_masters = [4, 7, 9, 5, 6, 5] # Altered data from Database Whizzes
database_whizzes = [9, 6, 3, 5, 4, 5] # Altered data from Frontend Gurus
devops_ninjas = [5, 9, 8, 6, 3, 4]    # Altered data from Backend Masters

proficiency_data = [frontend_gurus, backend_masters, database_whizzes, devops_ninjas]
teams = ["Frontend Gurus", "Backend Masters", "Database Whizzes", "DevOps Ninjas"]

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

plt.title("Tech Stack Proficiency Comparison Among IT Teams", fontsize=16, pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=12)
plt.tight_layout()
plt.show()