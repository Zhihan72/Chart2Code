import matplotlib.pyplot as plt
import numpy as np
from math import pi

categories = ['Life Sciences', 'Navigation', 'Survival Skills', 'Engineering', 'Communication']
num_skills = len(categories)

apollo_astronauts = [7, 9, 9, 8, 6]
mars_rover_engineers = [8, 6, 6, 9, 5]
iss_scientists = [9, 5, 5, 8, 8]
spacex_pilots = [5, 8, 8, 7, 9]

data = np.array([apollo_astronauts, mars_rover_engineers, iss_scientists, spacex_pilots])
data = np.concatenate((data, data[:, [0]]), axis=1)

angles = np.linspace(0, 2 * pi, num_skills, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

labels = ["SpaceX Pilots", "ISS Scientists", "Mars Rover Engineers", "Apollo Astronauts"]
colors = ['#FF33A1', '#3357FF', '#33FF57', '#FF5733']

for i, color in enumerate(colors):
    ax.fill(angles, data[i], color=color, alpha=0.3, label=labels[i])  # Fill the area within the radar chart

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, fontweight='bold')

ax.yaxis.grid(True, linestyle='--', linewidth=0.5, color='grey')
ax.xaxis.grid(True, linestyle='--', linewidth=0.5, color='grey')
ax.set_ylim(0, 10)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', 4, '6', '8', '10'], fontsize=10, color='grey')

ax.set_title('Exploration Skills Assessment\nTeam Competency Profiles by Skill Sets', 
             fontsize=16, fontweight='bold', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

plt.tight_layout()
plt.show()