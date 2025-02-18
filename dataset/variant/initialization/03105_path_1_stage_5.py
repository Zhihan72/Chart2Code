import matplotlib.pyplot as plt
import numpy as np

eldoria_stats = [70, 60, 80, 85, 65]
dracoria_stats = [65, 70, 80, 60, 85]
lunaria_stats = [85, 70, 60, 75, 85]

data = [eldoria_stats, dracoria_stats, lunaria_stats]
colors = ['red', 'orange', 'cyan']

num_vars = len(eldoria_stats)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

def create_radar_chart(ax, data, color):
    data += data[:1]
    ax.fill(angles, data, color=color, alpha=0.25)

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

for i in range(len(data)):
    create_radar_chart(ax, data[i], colors[i])

ax.set_yticks([20, 40, 60, 80, 100])
ax.set_xticks(angles[:-1])

plt.tight_layout()
plt.show()