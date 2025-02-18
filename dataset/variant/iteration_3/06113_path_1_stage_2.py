import matplotlib.pyplot as plt
import numpy as np
from math import pi

categories = ['AI/ML', 'Security', 'DevOps', 'Database', 'Frontend', 'Backend']
num_vars = len(categories)

frontend_gurus = [9, 6, 3, 5, 4, 5]
backend_masters = [5, 9, 8, 6, 3, 4]
database_whizzes = [4, 7, 9, 5, 6, 5]
devops_ninjas = [6, 5, 4, 9, 3, 8]

proficiency_data = [frontend_gurus, backend_masters, database_whizzes, devops_ninjas]

teams = ["Frontend Experts", "Backend Professionals", "Database Specialists", "Ops Wizards"]

angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

for i, (team_data, team_name, color) in enumerate(zip(proficiency_data, teams, colors)):
    team_data += team_data[:1]
    ax.plot(angles, team_data, linewidth=2, linestyle='solid', label=team_name, color=color)
    ax.fill(angles, team_data, alpha=0.5, color=color)

ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=9)

ax.set_ylim(0, 10)
ax.set_yticks(range(0, 11, 2))
ax.set_yticklabels([str(x) for x in range(0, 11, 2)], fontsize=8)

plt.title("Skill Set Analysis Among Tech Divisions", fontsize=16, pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=12)

plt.tight_layout()
plt.show()