import matplotlib.pyplot as plt
import numpy as np

attributes = ['Military Strength', 'Economic Stability', 
              'Cultural Influence', 'Technological Innovation', 
              'Diplomatic Prowess']

eldoria_stats = [70, 60, 80, 85, 65]
dracoria_stats = [65, 70, 80, 60, 85]
lunaria_stats = [85, 70, 60, 75, 85]

data = [eldoria_stats, dracoria_stats, lunaria_stats]
colors = ['red', 'orange', 'cyan']

num_vars = len(attributes)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

def create_radar_chart(ax, data, color):
    data += data[:1]  # Close the loop for the radar chart
    ax.fill(angles, data, color=color, alpha=0.25)

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

for i in range(len(data)):
    create_radar_chart(ax, data[i], colors[i])

ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels([str(i) for i in range(20, 120, 20)], color='gray')
ax.set_xticks(angles[:-1])
ax.set_xticklabels(attributes, fontsize=10, color='darkslategray', weight='bold')

for label, angle in zip(ax.get_xticklabels(), angles):
    label.set_horizontalalignment('center')

plt.tight_layout()
plt.show()