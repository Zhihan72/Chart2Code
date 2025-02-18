import matplotlib.pyplot as plt
import numpy as np

categories = ['Cost Efficiency', 'Environmental Impact', 'Feasibility', 'Energy Output', 'Technological Advancement']
solar_data = [7, 9, 8, 7, 8]
wind_data = [6, 8, 9, 8, 7]
hydro_data = [8, 8, 6, 9, 7]
geothermal_data = [6, 7, 7, 8, 6]
biomass_data = [7, 6, 6, 7, 7]

labels = np.array(categories)
data_entries = {
    'Solar Power': np.array(solar_data + [solar_data[0]]),
    'Wind Power': np.array(wind_data + [wind_data[0]]),
    'Hydro Power': np.array(hydro_data + [hydro_data[0]]),
    'Geothermal Energy': np.array(geothermal_data + [geothermal_data[0]]),
    'Biomass Energy': np.array(biomass_data + [biomass_data[0]])
}

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

# New set of colors
colors = ['#FF4500', '#1E90FF', '#3CB371', '#FFA500', '#8A2BE2']

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

for (name, data), color in zip(data_entries.items(), colors):
    ax.fill(angles, data, color=color, alpha=0.25, label=name)
    ax.plot(angles, data, color=color, linewidth=2)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=12)
ax.set_yticklabels([])
ax.set_ylim(0, 10)
ax.set_title('Efficiency Assessment of Renewable Energy Sources\nA Comparative Study by Eco Consortium', size=15, weight='bold', pad=20)

ax.legend(loc='upper right', bbox_to_anchor=(1.25, 1.1), title="Energy Sources", frameon=False)

plt.tight_layout()
plt.show()