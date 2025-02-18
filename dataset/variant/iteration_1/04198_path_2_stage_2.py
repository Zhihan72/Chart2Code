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
    ax.fill(angles, scores, color=colors[idx], alpha=0.4, label=agency_name)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(criteria, fontsize=11, fontweight='bold')
ax.set_ylim(0, 10)
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, color='grey')
ax.xaxis.grid(True, linestyle='--', linewidth=0.5, color='grey')
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(["2", "4", "6", "8", "10"], fontsize=9, bbox=dict(facecolor='white', alpha=0.5, boxstyle='round,pad=0.3'))

plt.title("Assessing Space Technology Advancements:\nA Comparative Analysis Across Leading Space Agencies", 
          size=16, color='darkred', y=1.1)

ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.2), fontsize=10, title="Space Agencies", title_fontsize=12)
plt.tight_layout()
plt.show()