import matplotlib.pyplot as plt
import numpy as np

categories = ['Cost', 'Env. Impact', 'Feas.', 'Output', 'Tech. Adv.']

solar_data = [7, 9, 8, 7, 8]
wind_data = [6, 8, 9, 8, 7]
hydro_data = [8, 8, 6, 9, 7]
geothermal_data = [6, 7, 7, 8, 6]
biomass_data = [7, 6, 6, 7, 7]
nuclear_data = [8, 7, 7, 9, 8]

labels = np.array(categories)

data_entries = {
    'Solar': np.array(solar_data + [solar_data[0]]),
    'Wind': np.array(wind_data + [wind_data[0]]),
    'Hydro': np.array(hydro_data + [hydro_data[0]]),
    'Geothermal': np.array(geothermal_data + [geothermal_data[0]]),
    'Biomass': np.array(biomass_data + [biomass_data[0]]),
    'Nuclear': np.array(nuclear_data + [nuclear_data[0]])
}

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

# Manually shuffled colors
colors = ['#4682B4', '#32CD32', '#FF6347', '#9370DB', '#FF1493', '#FFD700']

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

for (name, data), color in zip(data_entries.items(), colors):
    ax.fill(angles, data, color=color, alpha=0.25, label=name)
    ax.plot(angles, data, color=color, linewidth=2)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=12)
ax.set_yticklabels([])
ax.set_ylim(0, 10)
ax.set_title('Energy Efficiency Radar', size=15, weight='bold', pad=20)

ax.legend(loc='upper right', bbox_to_anchor=(1.25, 1.1), title="Sources", frameon=False)

plt.tight_layout()
plt.show()