import matplotlib.pyplot as plt
import numpy as np
from math import pi

attributes = ['Military Strength', 'Economic Stability', 'Cultural Influence', 
              'Technological Innovation', 'Diplomatic Prowess']

# Manually shuffle the data for each kingdom while preserving the list structure
eldoria_stats = [70, 60, 80, 85, 65]
dracoria_stats = [65, 70, 80, 60, 85]
lunaria_stats = [85, 70, 60, 75, 85]

data = [eldoria_stats, dracoria_stats, lunaria_stats]
kingdoms = ['Kingdom of Eldoria', 'Realm of Dracoria', 'Empire of Lunaria']
colors = ['blue', 'green', 'purple']

num_vars = len(attributes)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1] 

def create_radar_chart(ax, data, color, label):
    data += data[:1]
    ax.plot(angles, data, color=color, linewidth=2, linestyle='solid', label=label, marker='o')
    ax.fill(angles, data, color=color, alpha=0.25)

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

for i in range(len(kingdoms)):
    create_radar_chart(ax, data[i], colors[i], kingdoms[i])

ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels([str(i) for i in range(20, 120, 20)], color='gray')
ax.set_xticks(angles[:-1])
ax.set_xticklabels(attributes, fontsize=10, color='darkslategray', weight='bold')

ax.yaxis.grid(True, color='lightgray', linestyle='--')
ax.xaxis.grid(True, color='lightgray', linestyle='--')

plt.title('Attributes of Medieval Kingdoms\nA Comparative Analysis', size=14, weight='bold', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.25, 1.1), fontsize=10, frameon=True)

for label, angle in zip(ax.get_xticklabels(), angles):
    label.set_horizontalalignment('center')

plt.tight_layout()
plt.show()