import matplotlib.pyplot as plt
import numpy as np
from math import pi

attributes = ['Military Strength', 'Economic Stability', 'Cultural Influence', 
              'Technological Innovation', 'Diplomatic Prowess']

eldoria_stats = [60, 65, 85, 70, 80]
dracoria_stats = [85, 80, 60, 65, 70]
lunaria_stats = [70, 60, 75, 85, 85]
valoria_stats = [75, 70, 80, 90, 60]  # New data series for the Kingdom of Valoria

data = [eldoria_stats, dracoria_stats, lunaria_stats, valoria_stats]
kingdoms = ['Kingdom of Eldoria', 'Realm of Dracoria', 'Empire of Lunaria', 'Dominion of Valoria']
colors = ['cyan', 'olive', 'fuchsia', 'orange']  # Added new color for Valoria

num_vars = len(attributes)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

def create_radar_chart(ax, data, color, label):
    data += data[:1]
    ax.plot(angles, data, color=color, linewidth=1.5, linestyle='--', marker='o', label=label)
    ax.fill(angles, data, color=color, alpha=0.1)

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

for i in range(len(kingdoms)):
    create_radar_chart(ax, data[i], colors[i], kingdoms[i])

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(attributes, fontsize=11, color='darkred')
plt.title('Attributes of Medieval Kingdoms\nComparative Analysis', size=14, weight='bold', pad=20)

ax.legend(loc='upper left', bbox_to_anchor=(1.3, 0.9), fontsize=9, frameon=False)

ax.grid(color='grey', linestyle=':', linewidth=0.5) 

plt.tight_layout()
plt.show()