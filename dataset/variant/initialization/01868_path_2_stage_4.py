import matplotlib.pyplot as plt
import numpy as np

attributes = ['Intensity', 'Tactics', 'Harmony', 'Zest', 'Precision', 'Protection']
n_attributes = len(attributes)

gryffindor = [9, 8, 7, 10, 9, 6]
slytherin = [8, 9, 8, 7, 10, 7]
ravenclaw = [7, 9, 9, 6, 8, 9]
hufflepuff = [8, 7, 8, 8, 7, 9]

for team in [gryffindor, slytherin, ravenclaw, hufflepuff]:
    team += team[:1]

angles = np.linspace(0, 2 * np.pi, n_attributes, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

plt.xticks(angles[:-1], attributes, fontsize=11, fontweight='bold', color='midnightblue')

single_color = '#ff6f61'  # Use a single color for all groups
team_data = [gryffindor, slytherin, ravenclaw, hufflepuff]

for team in team_data:
    ax.fill(angles, team, color=single_color, alpha=0.25)

plt.title('Skills Display by Quidditch Groups\nin Magic Competitions', 
          size=15, fontweight='bold', pad=30, color='darkred')

plt.tight_layout()
plt.show()