import matplotlib.pyplot as plt
import numpy as np
from math import pi

colonies = ['Space Haven', 'Orbital Station', 'Lunar Post']
attributes = ['Creativity', 'Social', 'Mindfulness', 'Fitness', 'Meditation']

data = [
    [7, 9, 8, 6, 8],
    [6, 8, 7, 7, 9],
    [9, 7, 8, 6, 7]
]

data = np.array(data)
num_attributes = len(attributes)

angles = np.linspace(0, 2 * pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

colors = ['#1f77b4', '#ff9896', '#98df8a']

# Altered styles for data representation and fill areas
for i, colony_data in enumerate(data):
    values = colony_data.tolist()
    values += values[:1]
    ax.plot(angles, values, color=colors[i], linestyle='--', linewidth=2, marker='o')
    ax.fill(angles, values, color=colors[i], alpha=0.2)

# Altered style for the xticks
plt.xticks(angles[:-1], attributes, color='navy', size=12, fontweight='bold')

# Altered grid and borders
ax.set_rlabel_position(45)
ax.grid(color='gray', linestyle='-', linewidth=0.8)
ax.spines['polar'].set_visible(False)

plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="navy", size=8)
plt.ylim(0, 10)

# Altered title
plt.title("Study of Interplanetary Habitats\nActivity Preferences", size=16, color='darkblue', pad=25)

# Altered legend placement and aesthetics
plt.legend(loc='best', fontsize='small', frameon=False)

plt.tight_layout()
plt.show()