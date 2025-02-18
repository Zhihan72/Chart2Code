import matplotlib.pyplot as plt
import numpy as np

agencies = ['NASA', 'ESA', 'CNSA', 'ISRO']
domains = ['Satellite\nTechnology', 'Manned\nMissions', 'Planetary\nScience', 
           'Propulsion\nSystems', 'International\nCollaborations']

competency_scores = np.array([
    [10, 7, 9, 9, 8],  # NASA
    [9, 8, 6, 8, 9],   # ESA
    [9, 9, 8, 6, 8],   # CNSA
    [6, 8, 7, 7, 9]    # ISRO
])

num_vars = len(domains)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.set_ylim(0, 10)

# Manually assigned shuffled colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # Blue, Orange, Green, Red

for i, agency in enumerate(agencies):
    values = competency_scores[i].tolist()
    values += values[:1]
    
    ax.fill(angles, values, alpha=0.3, label=agency, color=colors[i])

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(domains, fontsize=10, ha='center')

ax.spines['polar'].set_color('blue')
ax.grid(True, color='black', linestyle='-.', linewidth=0.3)

plt.title('The Symphony of Space Exploration:\nCompetency Profile of Leading Space Agencies in 2025',
          fontsize=14, fontweight='bold', pad=20)
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.1), fontsize=10)

plt.tight_layout()
plt.show()