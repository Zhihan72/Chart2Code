import matplotlib.pyplot as plt
import numpy as np

continents = ['Europe', 'Asia', 'North America', 'South America', 'Africa']
sources = ['Solar', 'Wind', 'Hydro']

energy_data = np.array([
    [200, 150, 100],
    [300, 200, 250],
    [250, 220, 180],
    [120, 100, 300],
    [180, 90, 70]
])

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define new bar colors
colors = ['#e6194b', '#3cb44b', '#ffe119']

xpos, ypos = np.meshgrid(np.arange(energy_data.shape[0]), np.arange(energy_data.shape[1]), indexing='ij')
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

dx = dy = 0.7

for i in range(len(sources)):
    dz = energy_data[:, i]
    ax.bar3d(xpos[i::energy_data.shape[1]], ypos[i::energy_data.shape[1]], zpos[i::energy_data.shape[1]],
             dx, dy, dz, color=colors[i], alpha=0.8, label=sources[i])
    zpos[i::energy_data.shape[1]] += dz

ax.set_xlabel('Continents', fontsize=12)
ax.set_ylabel('Energy Sources', fontsize=12)
ax.set_zlabel('Energy Generation (GW)', fontsize=12)

ax.set_xticks(np.arange(len(continents)))
ax.set_xticklabels(continents, rotation=30, ha='right')
ax.set_yticks(np.arange(len(sources)))
ax.set_yticklabels(sources)

ax.set_title('2030 Renewable Energy Generation Across Continents', fontsize=16, fontweight='bold', pad=20)
ax.legend(title='Energy Sources', loc='upper left', fontsize=10, bbox_to_anchor=(0.9, 1))

ax.view_init(elev=30, azim=120)

plt.tight_layout()
plt.show()