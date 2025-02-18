import matplotlib.pyplot as plt
import numpy as np

agencies = ['NASA', 'ESA', 'CNSA', 'ISRO']
domains = ['Satellite\nTechnology', 'Manned\nMissions', 'Planetary\nScience',
           'Propulsion\nSystems', 'International\nCollaborations']

# Altered competency scores for each agency
competency_scores = np.array([
    [10, 9, 7, 8, 8],  # NASA - Randomly changed
    [7, 8, 8, 6, 9],   # ESA - Randomly changed
    [8, 7, 9, 6, 8],   # CNSA - Randomly changed
    [6, 9, 6, 9, 7]    # ISRO - Randomly changed
])

num_vars = len(domains)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.set_ylim(0, 10)

for i, agency in enumerate(agencies):
    values = competency_scores[i].tolist()
    values += values[:1]
    
    ax.fill(angles, values, alpha=0.25, label=agency)
    ax.plot(angles, values, linewidth=2, linestyle='-')

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(domains, fontsize=10, ha='center')
ax.spines['polar'].set_visible(False)
ax.grid(color='grey', linestyle='--', linewidth=0.5)

plt.title('The Symphony of Space Exploration:\nCompetency Profile of Leading Space Agencies in 2025',
          fontsize=14, fontweight='bold', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)
plt.tight_layout()

plt.show()