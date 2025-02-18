import matplotlib.pyplot as plt
import numpy as np
from math import pi

attributes = ['Cultural Reach', 'Tech Advancement', 'Military Force', 
              'Economic Power', 'Diplomatic Skills']

eldoria_stats = [60, 65, 85, 70, 80]
lunaria_stats = [70, 60, 75, 85, 85]

data = [eldoria_stats, lunaria_stats]
kingdoms = ['Lunaria Coalition', 'Eldoria Dominion']
colors = ['purple', 'green']

num_vars = len(attributes)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

def create_radar_chart(ax, data, color, label):
    data += data[:1]
    ax.fill(angles, data, color=color, alpha=0.25, label=label)

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

for i in range(len(kingdoms)):
    create_radar_chart(ax, data[i], colors[i], kingdoms[i])

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(attributes, fontsize=10, color='gray')

plt.title('Medieval Kingdoms Overview\nRandomized Attributes', size=14, weight='bold', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)

plt.tight_layout()
plt.show()