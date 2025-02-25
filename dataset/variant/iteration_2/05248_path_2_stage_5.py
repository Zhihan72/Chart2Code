import matplotlib.pyplot as plt
import numpy as np

categories = ['Cost', 'Env. Impact', 'Feas.', 'Output', 'Tech. Adv.']

data_entries = {
    'Solar': [7, 9, 8, 7, 8, 7],
    'Wind': [6, 8, 9, 8, 7, 6],
    'Hydro': [8, 8, 6, 9, 7, 8],
    'Geothermal': [6, 7, 7, 8, 6, 6],
    'Biomass': [7, 6, 6, 7, 7, 7],
    'Nuclear': [8, 7, 7, 9, 8, 8]
}

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

colors = ['#4682B4', '#32CD32', '#FF6347', '#9370DB', '#FF1493', '#FFD700']

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

for (name, data), color in zip(data_entries.items(), colors):
    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, color=color, linewidth=2)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12)
ax.set_yticklabels([])
ax.set_ylim(0, 10)
ax.set_title('Energy Efficiency Radar', size=15, weight='bold', pad=20)

ax.spines['polar'].set_visible(False)

plt.tight_layout()
plt.show()