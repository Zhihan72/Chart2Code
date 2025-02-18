import matplotlib.pyplot as plt
import numpy as np

agencies = ['NASA', 'ESA', 'CNSA', 'ISRO']
domains = ['Satellite\nTechnology', 'Manned\nMissions', 'Planetary\nScience',
           'Propulsion\nSystems', 'International\nCollaborations']

competency_scores = np.array([
    [10, 9, 7, 8, 8],  # NASA
    [7, 8, 8, 6, 9],   # ESA
    [8, 7, 9, 6, 8],   # CNSA
    [6, 9, 6, 9, 7]    # ISRO
])

num_vars = len(domains)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.set_ylim(0, 10)

# Loop through each agency and fill the corresponding area
for i, agency in enumerate(agencies):
    values = competency_scores[i].tolist()
    values += values[:1]  # Close the loop
    
    ax.fill(angles, values, alpha=0.25, label=agency)  # Fill the area
    ax.plot(angles, values, linewidth=2, linestyle='-')  # Outline the area

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