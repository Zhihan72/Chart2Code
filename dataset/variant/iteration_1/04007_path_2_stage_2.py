import numpy as np
import matplotlib.pyplot as plt
from math import pi

spacecraft_types = ['Fighter', 'Bomber', 'Destroyer', 'Cruiser', 'Scout']
attributes = ['Spd', 'Armr', 'Wpns', 'Mnvr', 'Stlh', 'Crgo']

spacecraft_data = {
    'Fghtr': [9, 6, 8, 10, 7, 3],
    'Bmb': [6, 9, 10, 5, 4, 7],
    'Dstyr': [4, 10, 9, 3, 5, 6],
    'Crsr': [5, 8, 6, 4, 3, 10],
    'Sct': [10, 4, 5, 9, 8, 2]
}

num_attributes = len(attributes)
angles = np.linspace(0, 2 * pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
plt.xticks(angles[:-1], attributes, color='grey', size=12)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color='grey', size=10)
plt.ylim(0, 10)

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for idx, (spacecraft, values) in enumerate(spacecraft_data.items()):
    values += values[:1]
    ax.plot(angles, values, linewidth=2, linestyle='solid', color=colors[idx])
    ax.fill(angles, values, color=colors[idx], alpha=0.25)

plt.show()