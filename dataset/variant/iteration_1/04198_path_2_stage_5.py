import matplotlib.pyplot as plt
import numpy as np

criteria = ['Thrust', 'Guidance', 'Talk', 'Living Conditions', 'Defense', 'Fuel Use']
num_criteria = len(criteria)

# Scores for each space agency
agency_scores = {
    'Galactic Federation': [9, 8, 9, 8, 7, 9],
    'Starfleet Command': [9, 7, 8, 6, 7, 9],
    'Cosmic Alliance': [8, 7, 6, 7, 6, 8]
}

angles = np.linspace(0, 2 * np.pi, num_criteria, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

colors = plt.cm.viridis(np.linspace(0, 1, len(agency_scores)))

for idx, (agency_name, scores) in enumerate(agency_scores.items()):
    scores += scores[:1]
    ax.fill(angles, scores, color=colors[idx], alpha=0.4)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(criteria, fontsize=11, fontweight='bold')
ax.set_ylim(0, 10)
ax.set_yticks([])
ax.set_yticklabels([])

plt.title("Intergalactic Systems Evaluation", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()