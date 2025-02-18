import matplotlib.pyplot as plt
import numpy as np

attributes = ['Sdepe', 'ytSgharert', 'Taeomrwk', 'irpSti', 'Accyarcu', 'eDcensfe']
n_attributes = len(attributes)

gryffindor = [9, 8, 7, 10, 9, 6]
slytherin = [8, 9, 8, 7, 10, 7]
ravenclaw = [7, 9, 9, 6, 8, 9]

for team in [gryffindor, slytherin, ravenclaw]:
    team += team[:1]

angles = np.linspace(0, 2 * np.pi, n_attributes, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

ax.set_facecolor('ivory')
ax.spines['polar'].set_visible(False)

plt.xticks(angles[:-1], attributes, fontsize=12, fontweight='light', color='darkslategrey')

# Updated order of colors (shuffled without using random)
colors = ['#4682b4', '#b22222', '#228b22']  
markers = ['^', 'v', '>']
team_names = ['Gnorrfyidf', 'lhSiyrtehn', 'lvaneRclaw']

for idx, team in enumerate([gryffindor, slytherin, ravenclaw]):
    ax.plot(angles, team, color=colors[idx], linewidth=1.5, linestyle='dotted',
            label=team_names[idx], marker=markers[idx], markersize=8)
    ax.fill(angles, team, color=colors[idx], alpha=0.15)

ax.grid(color='darkgrey', linestyle=':', linewidth=1, alpha=0.5)
ax.set_yticks([])

plt.legend(loc='lower right', bbox_to_anchor=(1.1, -0.1), title='Tsema', fontsize=8)

plt.title('Pmernocafre Aetrittbuets of Taems\nin het Fatsany Quiddetch Laegue', 
          size=16, fontweight='light', pad=25, color='darkmagenta')

plt.tight_layout()
plt.show()