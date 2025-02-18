import matplotlib.pyplot as plt
import numpy as np
from math import pi

categories = ['AI/ML', 'Security', 'DevOps', 'Database', 'Frontend', 'Backend']
num_vars = len(categories)

frontend_gurus = [9, 6, 3, 5, 4, 5]
backend_masters = [5, 9, 8, 6, 3, 4]
devops_ninjas = [6, 5, 4, 9, 3, 8]

proficiency_data = [frontend_gurus, backend_masters, devops_ninjas]

angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Use a consistent color for all plots
single_color = '#1f77b4'

for i, team_data in enumerate(proficiency_data):
    team_data += team_data[:1]
    ax.plot(angles, team_data, linewidth=2, linestyle='solid', color=single_color)
    ax.fill(angles, team_data, alpha=0.5, color=single_color)

ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=9)

ax.set_ylim(0, 10)
ax.set_yticks(range(0, 11, 2))
ax.set_yticklabels([str(x) for x in range(0, 11, 2)], fontsize=8)

# Remove grid and borders
ax.grid(False)
ax.spines["polar"].set_visible(False)

plt.title("Skill Set Analysis Among Tech Divisions", fontsize=16, pad=20)

plt.tight_layout()
plt.show()