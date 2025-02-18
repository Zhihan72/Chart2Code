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

# Manually shuffled colors
colors = ['#377EB8', '#8CBF26', '#59A9C8', '#E41A1C', '#F28E2B'] # The order was altered

for i, species in enumerate(tree_species):
    species_data = [climate[i] for climate in data]
    bp = ax.boxplot(species_data, positions=[i], widths=0.6, vert=True, patch_artist=True, 
                    boxprops=dict(facecolor=colors[i], color='black'),
                    whiskerprops=dict(color='black', linestyle='--'),
                    capprops=dict(color='black'),
                    flierprops=dict(marker='o', color='red', alpha=0.5),
                    medianprops=dict(color='black'),
                    notch=True)

ax.set_xticks(range(len(tree_species)))
ax.set_xticklabels(tree_species, fontsize=12, fontweight='bold')
ax.set_ylabel("Growth Rate (cm/year)", fontsize=12, fontweight='bold')
ax.set_title("Growth Rates of Different Tree Species in Various Climates", fontsize=16, fontweight='bold', pad=20)
ax.grid(axis='y', linestyle='--', alpha=0.5)

legend_labels = ['Tropical', 'Temperate', 'Boreal', 'Arid', 'Mediterranean']
handles = [plt.Line2D([0], [0], color=colors[i], lw=4) for i in range(len(tree_species))]
ax.legend(handles, legend_labels, title='Tree Species', loc='upper right', bbox_to_anchor=(1.25, 1), fontsize=12)

plt.tight_layout()
plt.show()