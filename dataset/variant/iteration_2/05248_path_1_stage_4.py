import matplotlib.pyplot as plt
import numpy as np

categories = ['Cost Efficiency', 'Environmental Impact', 'Feasibility', 'Energy Output', 'Technological Advancement']
solar_data = [8, 7, 9, 8, 7]
wind_data = [9, 6, 7, 8, 8]
hydro_data = [6, 8, 7, 9, 8]
geothermal_data = [7, 8, 6, 6, 7]
biomass_data = [6, 7, 6, 7, 7]

data_entries = {
    'Solar Power': solar_data,
    'Wind Power': wind_data,
    'Hydro Power': hydro_data,
    'Geothermal Energy': geothermal_data,
    'Biomass Energy': biomass_data
}

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

colors = ['#FF4500', '#1E90FF', '#3CB371', '#FFA500', '#8A2BE2']

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

for (name, data), color in zip(data_entries.items(), colors):
    data += data[:1]
    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, color=color, linewidth=2)

ax.set_xticks(angles[:-1])
ax.set_xticklabels([])  # Remove category labels
ax.set_yticklabels([])  # Keep y-tick labels removed
ax.set_ylim(0, 10)

# Remove title and legend
# ax.set_title('Efficiency Assessment of Renewable Energy Sources\nA Comparative Study by Eco Consortium', size=15, weight='bold', pad=20)
# ax.legend(loc='upper right', bbox_to_anchor=(1.25, 1.1), title="Energy Sources", frameon=False)

plt.tight_layout()
plt.show()