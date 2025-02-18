import matplotlib.pyplot as plt
import numpy as np

criteria = ['Communication', 'Shielding', 'Propulsion', 'Energy Efficiency', 'Navigation', 'Life Support']
num_criteria = len(criteria)

agency_scores = {
    'ESA': [7, 8, 7, 7, 8, 8],
    'NASA': [9, 8, 9, 8, 7, 9],
    'ISRO': [8, 7, 6, 7, 6, 8],
    'Roscosmos': [6, 5, 6, 7, 8, 7],
    'SpaceX': [9, 7, 8, 6, 7, 9],
    'Galactic Ventures': [8, 9, 7, 8, 9, 8],
    'LunarTech': [6, 5, 8, 7, 7, 6]
}

num_agencies = len(agency_scores)

angles = np.linspace(0, 2 * np.pi, num_criteria, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

colors = plt.cm.viridis(np.linspace(0, 1, num_agencies))

markers = ['o', 's', 'D', '^', 'v', 'p', 'h']

for idx, (agency_name, scores) in enumerate(agency_scores.items()):
    scores += scores[:1]
    ax.plot(angles, scores, color=colors[idx], linewidth=1.5, linestyle='-.', marker=markers[idx], markersize=5, label=agency_name)
    ax.fill(angles, scores, color=colors[idx], alpha=0.2)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(criteria, fontsize=10, fontweight='regular')

ax.set_ylim(0, 10)

ax.yaxis.grid(True, linestyle=':', linewidth=0.6, color='grey')
ax.xaxis.grid(False)

ax.set_yticks([3, 6, 9])
ax.set_yticklabels(["3", "6", "9"], fontsize=8, bbox=dict(facecolor='lightgrey', alpha=0.6, boxstyle='square'))

plt.title("Space Agency Tech Analysis", size=15, color='brown', y=1.1)

ax.legend(loc='lower left', bbox_to_anchor=(-0.2, 0), fontsize=9, title="Agencies", title_fontsize=11)

plt.tight_layout()
plt.show()