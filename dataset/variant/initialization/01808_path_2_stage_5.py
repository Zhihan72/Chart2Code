import matplotlib.pyplot as plt
import numpy as np

agencies = ['NASA', 'ESA', 'CNSA', 'ISRO']
domains = ['Satellite\nTechnology', 'Manned\nMissions', 'Planetary\nScience', 
           'Propulsion\nSystems', 'International\nCollaborations']

competency_scores = np.array([
    [10, 7, 9, 9, 8],  
    [9, 8, 6, 8, 9],   
    [9, 9, 8, 6, 8],   
    [6, 8, 7, 7, 9]    
])

num_vars = len(domains)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.set_ylim(0, 10)

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

for i, agency in enumerate(agencies):
    values = competency_scores[i].tolist()
    values += values[:1]
    
    ax.fill(angles, values, alpha=0.3, color=colors[i])

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels([''] * num_vars)

ax.spines['polar'].set_color('blue')
ax.grid(True, color='black', linestyle='-.', linewidth=0.3)

plt.tight_layout()
plt.show()