import matplotlib.pyplot as plt

tree_species = ['Oak', 'Pine', 'Maple', 'Birch', 'Redwood']

climate_tropical = [120, 140, 115, 130, 145]
climate_temperate = [80, 100, 95, 85, 110]
climate_boreal = [50, 70, 65, 55, 75]
climate_arid = [30, 50, 45, 35, 55]
climate_mediterranean = [70, 90, 85, 75, 95]
climate_rainforest = [130, 150, 125, 140, 155]

data = [
    climate_tropical,
    climate_temperate,
    climate_boreal,
    climate_arid,
    climate_mediterranean,
    climate_rainforest
]

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#E41A1C', '#377EB8', '#4DAF4A', '#984EA3', '#FF7F00', '#A65628']
linestyles = ['-', '--', '-.', ':', '-', '-']

for i, species in enumerate(tree_species):
    species_data = [climate[i] for climate in data]
    ax.boxplot(species_data, positions=[i], widths=0.5, vert=False, patch_artist=True,
               boxprops=dict(facecolor=colors[i], color='gray'),
               whiskerprops=dict(color='gray', linestyle=linestyles[i]),
               capprops=dict(color='gray'),
               flierprops=dict(marker='^', color='green', alpha=0.6),
               medianprops=dict(color='gray'),
               notch=False)

plt.tight_layout()
plt.show()