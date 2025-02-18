import matplotlib.pyplot as plt
import numpy as np
from math import pi

categories = ['Survival Skills', 'Navigation', 'Communication', 'Life Sciences', 'Engineering']
num_skills = len(categories)

team_1 = [9, 8, 7, 6, 9]
team_2 = [6, 9, 8, 5, 6]
team_3 = [5, 8, 9, 8, 5]
team_4 = [8, 7, 5, 9, 8]

data = np.array([team_1, team_2, team_3, team_4])
data = np.concatenate((data, data[:, [0]]), axis=1)

angles = np.linspace(0, 2 * pi, num_skills, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

for i in range(len(data)):
    ax.fill(angles, data[i], alpha=0.25, label=f'Team {i+1}')
    ax.plot(angles, data[i], linewidth=2)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, fontweight='bold')

plt.title('Multi-team Capability Assessment', fontsize=15, fontweight='bold')
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
plt.show()