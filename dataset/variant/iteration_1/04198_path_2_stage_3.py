import matplotlib.pyplot as plt
import numpy as np

criteria = ['Propulsion', 'Navigation', 'Communication', 'Life Support', 'Shielding', 'Energy Efficiency']
num_criteria = len(criteria)

# Scores for each space agency
agency_scores = {
    'NASA': [9, 8, 9, 8, 7, 9],
    'SpaceX': [9, 7, 8, 6, 7, 9],
    'ISRO': [8, 7, 6, 7, 6, 8]
}

angles = np.linspace(0, 2 * np.pi, num_criteria, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

colors = plt.cm.plasma(np.linspace(0, 1, len(agency_scores)))

for idx, (agency_name, scores) in enumerate(agency_scores.items()):
    scores += scores[:1]
    ax.fill(angles, scores, color=colors[idx], alpha=0.4)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(criteria, fontsize=11, fontweight='bold')
ax.set_ylim(0, 10)
ax.set_yticks([])
ax.set_yticklabels([])

plt.tight_layout()
plt.show()