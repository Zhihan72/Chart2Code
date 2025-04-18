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

angles = np.linspace(0, 2 * np.pi, num_criteria, endpoint=False).tolist()
angles += angles[:1]  # Closing the plot by adding start angle to end

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

colors = [
    [0.267004, 0.004874, 0.329415, 1.     ],
    [0.993248, 0.906157, 0.143936, 1.     ],
    [0.190631, 0.407061, 0.556089, 1.     ],
    [0.992898, 0.706145, 0.115681, 1.     ],
    [0.127568, 0.566949, 0.550556, 1.     ],
    [0.993248, 0.769364, 0.317163, 1.     ],
    [0.163625, 0.471133, 0.558148, 1.     ]
]

for idx, (agency_name, scores) in enumerate(agency_scores.items()):
    scores += scores[:1]  # Closing plot by repeating start value
    ax.fill(angles, scores, color=colors[idx], alpha=0.25, label=agency_name)  # Fill area

ax.set_xticks(angles[:-1])
ax.set_xticklabels(criteria)

ax.set_ylim(0, 10)
ax.yaxis.grid(True, linestyle=':', linewidth=0.6, color='grey')
ax.xaxis.grid(False)
ax.set_yticks([3, 6, 9])
ax.set_yticklabels(["3", "6", "9"], fontsize=8, bbox=dict(facecolor='lightgrey', alpha=0.6, boxstyle='square'))

plt.title("Space Agency Tech Analysis", size=15, color='brown', y=1.1)
ax.legend(loc='lower left', bbox_to_anchor=(-0.2, 0), fontsize=9, title="Agencies", title_fontsize=11)

plt.tight_layout()
plt.show()