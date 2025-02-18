import matplotlib.pyplot as plt
import numpy as np
from math import pi

categories = ['Life Sciences', 'Navigation', 'Survival Skills', 'Engineering', 'Communication']
num_skills = len(categories)

apollo_astronauts = [7, 9, 9, 8, 6]
mars_rover_engineers = [8, 6, 6, 9, 5]
spacex_pilots = [5, 8, 8, 7, 9]

data = np.array([apollo_astronauts, mars_rover_engineers, spacex_pilots])
data = np.concatenate((data, data[:, [0]]), axis=1)

angles = np.linspace(0, 2 * pi, num_skills, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

labels = ["SpaceX Pilots", "Mars Rover Engineers", "Apollo Astronauts"]
colors = ['#33FF57', '#FF33A1', '#5733FF'] # Randomized color order

for i, color in enumerate(colors):
    linestyle_choices = ['-', ':', '-.'] # Modified line styles
    ax.plot(angles, data[i], color=color, linewidth=2, linestyle=linestyle_choices[i])
    ax.fill(angles, data[i], color=color, alpha=0.1, label=labels[i])

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10)

ax.yaxis.grid(True, linestyle='-', linewidth=0.7, color='black') # Altered grid style
ax.xaxis.grid(False) # Removed angular grid lines
ax.set_ylim(0, 10)
ax.set_yticks([3, 6, 9]) # Changed y-tick positions
ax.set_yticklabels(['3', '6', '9'], fontsize=10, color='blue') # Changed y-tick color

ax.set_title('Exploration Skills: Team Profiles', fontsize=14, fontweight='normal', pad=15) # Title modified
ax.legend(loc='lower left') # Changed legend location

plt.tight_layout()
plt.show()