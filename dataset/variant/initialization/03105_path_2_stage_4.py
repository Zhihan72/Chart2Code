import matplotlib.pyplot as plt
import numpy as np

eldoria_stats = [60, 65, 85, 70, 80]
dracoria_stats = [85, 80, 60, 65, 70]

data = [eldoria_stats, dracoria_stats]
colors = ['blue', 'green']
num_vars = 5

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

def create_filled_area_radar_chart(ax, data, color):
    data += data[:1]
    ax.fill(angles, data, color=color, alpha=0.25)

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

for i in range(len(data)):
    create_filled_area_radar_chart(ax, data[i], colors[i])

ax.set_yticks([])
ax.set_xticks([])

plt.tight_layout()
plt.show()