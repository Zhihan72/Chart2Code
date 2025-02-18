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

# Changed color set
new_colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']

for idx, (spacecraft, values) in enumerate(spacecraft_data.items()):
    values += values[:1]
    ax.plot(angles, values, linewidth=2, linestyle='solid', color=new_colors[idx])

plt.show()