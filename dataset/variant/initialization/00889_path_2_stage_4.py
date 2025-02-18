import matplotlib.pyplot as plt
import numpy as np

species = ['Sparrows', 'Hawks', 'Robins']
parks = ['Central Park', 'Urban Gardens']

sparrows_sightings = [30, 28, 32, 31, 29, 27, 33, 34, 30, 29, 30, 31, 32, 28, 29, 34]
hawks_sightings = [5, 6, 7, 4, 5, 6, 7, 8, 5, 4, 6, 7, 8, 5, 5]
robins_sightings = [20, 21, 19, 22, 23, 21, 22, 23, 24, 20, 21, 22, 23, 24, 22, 21]

min_len_cp = min(len(sparrows_sightings[:5]), len(hawks_sightings[:5]), len(robins_sightings[:5]))
min_len_ug = min(len(sparrows_sightings[5:10]), len(hawks_sightings[5:10]), len(robins_sightings[5:10]))

central_park_data = np.array([sparrows_sightings[:min_len_cp], hawks_sightings[:min_len_cp], robins_sightings[:min_len_cp]]).T
urban_gardens_data = np.array([sparrows_sightings[5:5 + min_len_ug], hawks_sightings[5:5 + min_len_ug], robins_sightings[5:5 + min_len_ug]]).T

fig, ax = plt.subplots(figsize=(8, 6))

bplot1 = ax.boxplot(central_park_data, vert=False, patch_artist=True, positions=np.arange(3)*2, widths=0.6)
bplot2 = ax.boxplot(urban_gardens_data, vert=False, patch_artist=True, positions=np.arange(3)*2 + 1, widths=0.6)

# Assign one consistent color across all data groups
consistent_color = 'lightblue'
for bplot in [bplot1, bplot2]:
    for patch in bplot['boxes']:
        patch.set_facecolor(consistent_color)
    for median in bplot['medians']:
        median.set(color='darkred', linewidth=2)

ax.set_yticks([0.5, 2.5, 4.5])
ax.set_yticklabels(species)

plt.tight_layout()
plt.show()