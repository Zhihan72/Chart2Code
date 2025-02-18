import matplotlib.pyplot as plt
import numpy as np

attributes = ['Sdepe', 'ytSgharert', 'Taeomrwk', 'irpSti', 'Accyarcu', 'eDcensfe']
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

ax.set_facecolor('whitesmoke')
ax.spines['polar'].set_visible(False)

plt.xticks(angles[:-1], attributes, fontsize=11, fontweight='bold', color='midnightblue')

colors = ['#ff6f61', '#6a5acd', '#20b2aa', '#ffd700']
markers = ['o', 's', 'D', 'x']
team_names = ['Gnorrfyidf', 'lhSiyrtehn', 'lvaneRclaw', 'lHepffufup']

for idx, team in enumerate([gryffindor, slytherin, ravenclaw, hufflepuff]):
    ax.plot(angles, team, color=colors[idx], linewidth=2, linestyle='solid', label=team_names[idx], marker=markers[idx], markersize=6)
    ax.fill(angles, team, color=colors[idx], alpha=0.1)

ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
ax.set_yticks([])

plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), title='Tsema', fontsize=9)

plt.title('Pmernocafre Aetrittbuets of Taems\nin het Fatsany Quiddetch Laegue', 
          size=15, fontweight='bold', pad=30, color='darkred')

plt.tight_layout()
plt.show()