import matplotlib.pyplot as plt
import numpy as np
from math import pi

attributes = ['Military Strength', 'Economic Stability', 'Cultural Influence', 
              'Technological Innovation', 'Diplomatic Prowess']

eldoria_stats = [60, 65, 85, 70, 80]
dracoria_stats = [85, 80, 60, 65, 70]
lunaria_stats = [70, 60, 75, 85, 85]

data = [eldoria_stats, dracoria_stats, lunaria_stats]
colors = ['blue', 'green', 'purple']
num_vars = len(attributes)

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

def create_radar_chart(ax, data, color):
    data += data[:1]
    ax.plot(angles, data, color=color, linewidth=2, linestyle='solid')
    ax.fill(angles, data, color=color, alpha=0.25)

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

for i in range(len(data)):
    create_radar_chart(ax, data[i], colors[i])

ax.set_yticks([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(attributes, fontsize=10, color='darkslategray', weight='bold')

plt.tight_layout()
plt.show()