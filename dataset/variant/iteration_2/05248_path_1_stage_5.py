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
line_styles = ['-', '--', '-.', ':', '-']
markers = ['o', 's', 'D', '^', 'p']

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

for (name, data), color, line_style, marker in zip(data_entries.items(), colors, line_styles, markers):
    data += data[:1]
    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, color=color, marker=marker, linestyle=line_style, linewidth=2)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10)
ax.set_yticklabels(['0', '2.5', '5', '7.5', '10'], fontsize=8)
ax.set_ylim(0, 10)
ax.grid(True, linestyle='--', linewidth=0.5)

ax.spines['polar'].set_visible(False)

ax.legend(loc='upper left', bbox_to_anchor=(1.1, 1.05), title="Energy Sources")

plt.tight_layout()
plt.show()