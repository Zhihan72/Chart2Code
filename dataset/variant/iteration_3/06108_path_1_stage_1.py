import numpy as np
import matplotlib.pyplot as plt

tree_species = ['Oak', 'Pine', 'Maple', 'Birch', 'Redwood']

climate_tropical = [120, 140, 115, 130, 145]
climate_temperate = [80, 100, 95, 85, 110]
climate_boreal = [50, 70, 65, 55, 75]
climate_arid = [30, 50, 45, 35, 55]
climate_mediterranean = [70, 90, 85, 75, 95]

data = [
    climate_tropical,
    climate_temperate,
    climate_boreal,
    climate_arid,
    climate_mediterranean
]

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#8CBF26', '#377EB8', '#E41A1C', '#F28E2B', '#59A9C8']
line_styles = ['--', '-.', '-', ':', '--']
marker_styles = ['o', 's', '^', 'd', '*']

for i, species in enumerate(tree_species):
    species_data = [climate[i] for climate in data]
    bp = ax.boxplot(species_data, positions=[i], widths=0.5, vert=True, patch_artist=True,
                    boxprops=dict(facecolor=colors[i], color='grey'),
                    whiskerprops=dict(color='grey', linestyle=line_styles[i]),
                    capprops=dict(color='grey'),
                    flierprops=dict(marker=marker_styles[i], color='red', alpha=0.6),
                    medianprops=dict(color='blue'),
                    notch=False)

ax.set_xticks(range(len(tree_species)))
ax.set_xticklabels(tree_species, fontsize=10, fontstyle='italic')
ax.set_ylabel("Growth Rate (cm/year)", fontsize=11, fontweight='light')
ax.set_title("Growth Rates of Tree Species in Climates", fontsize=15, fontweight='bold', color='darkgreen')
ax.grid(axis='y', linestyle=':', alpha=0.7)

handles = [plt.Line2D([0], [0], color=colors[i], lw=2, linestyle=line_styles[i]) for i in range(len(tree_species))]
ax.legend(handles, ['Tropical', 'Temperate', 'Boreal', 'Arid', 'Mediterranean'], title='Climates', loc='best', fontsize=11)

plt.tight_layout()
plt.show()