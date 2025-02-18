import numpy as np
import matplotlib.pyplot as plt
from math import pi

spacecraft_types = ['Fighter', 'Bomber', 'Destroyer', 'Cruiser', 'Scout', 'Transporter', 'Interceptor']
attributes = ['Speed', 'Armor', 'Weaponry', 'Maneuverability', 'Stealth', 'Cargo']

spacecraft_data = {
    'Fighter': [9, 6, 8, 10, 7, 3],
    'Bomber': [6, 9, 10, 5, 4, 7],
    'Destroyer': [4, 10, 9, 3, 5, 6],
    'Cruiser': [5, 8, 6, 4, 3, 10],
    'Scout': [10, 4, 5, 9, 8, 2],
    'Transporter': [3, 5, 2, 4, 3, 10],
    'Interceptor': [8, 5, 7, 9, 9, 4]
}

num_attributes = len(attributes)
angles = np.linspace(0, 2 * pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
plt.xticks(angles[:-1], attributes, color='grey', size=12)

ax.set_rscale('linear')
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color='grey', size=10)
plt.ylim(0, 10)

colors = ['#d62728', '#e377c2', '#1f77b4', '#2ca02c', '#8c564b', '#9467bd', '#ff7f0e']
for idx, (spacecraft, values) in enumerate(spacecraft_data.items()):
    values += values[:1]
    ax.plot(angles, values, linewidth=2, linestyle='solid', color=colors[idx])

plt.title("Diagnostic Ratings of Intergalactic Fleet Spacecraft", size=15, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()