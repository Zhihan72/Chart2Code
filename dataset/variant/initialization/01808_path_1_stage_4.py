import matplotlib.pyplot as plt
import numpy as np

agencies = ['CNSA', 'NASA', 'ISRO', 'ESA']
domains = ['Planetary\nScience', 'International\nCollaborations', 
           'Manned\nMissions', 'Satellite\nTechnology', 'Propulsion\nSystems']

competency_scores = np.array([
    [8, 7, 9, 6, 8],   # CNSA
    [10, 9, 7, 8, 8],  # NASA
    [6, 9, 6, 9, 7],   # ISRO
    [7, 8, 8, 6, 9]    # ESA
])

num_vars = len(domains)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.set_ylim(0, 10)

colors = ['#d62728', '#1f77b4', '#2ca02c', '#ff7f0e']

for i, agency in enumerate(agencies):
    values = competency_scores[i].tolist()
    values += values[:1]
    
    ax.fill(angles, values, color=colors[i], alpha=0.25, label=agency)
    ax.plot(angles, values, color=colors[i], linewidth=2, linestyle='-')

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(domains, fontsize=10, ha='center')
ax.spines['polar'].set_visible(False)
ax.grid(color='grey', linestyle='--', linewidth=0.5)

plt.title('A Journey through\nIntergalactic Prowess:\nKey Space Agency Competencies',
          fontsize=14, fontweight='bold', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)
plt.tight_layout()

plt.show()