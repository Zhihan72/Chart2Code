import matplotlib.pyplot as plt
import numpy as np

species = ['Sparrows', 'Hawks', 'Robins']
parks = ['Central Park', 'Urban Gardens', 'Riverside Reserve']

sparrows_sightings = [30, 28, 32, 31, 29, 27, 33, 34, 30, 29, 30, 31, 32, 28, 29, 34]
hawks_sightings = [5, 6, 7, 4, 5, 6, 7, 8, 5, 4, 6, 7, 8, 5, 5]
robins_sightings = [20, 21, 19, 22, 23, 21, 22, 23, 24, 20, 21, 22, 23, 24, 22, 21]

min_len_cp = min(len(sparrows_sightings[:5]), len(hawks_sightings[:5]), len(robins_sightings[:5]))
min_len_ug = min(len(sparrows_sightings[5:10]), len(hawks_sightings[5:10]), len(robins_sightings[5:10]))
min_len_rr = min(len(sparrows_sightings[10:15]), len(hawks_sightings[10:15]), len(robins_sightings[10:15]))

central_park_data = np.array([sparrows_sightings[:min_len_cp], hawks_sightings[:min_len_cp], robins_sightings[:min_len_cp]]).T
urban_gardens_data = np.array([sparrows_sightings[5:5 + min_len_ug], hawks_sightings[5:5 + min_len_ug], robins_sightings[5:5 + min_len_ug]]).T
riverside_reserve_data = np.array([sparrows_sightings[10:10 + min_len_rr], hawks_sightings[10:10 + min_len_rr], robins_sightings[10:10 + min_len_rr]]).T

avg_sightings = {
    "Sparrows": [np.mean(central_park_data[:, 0]), np.mean(urban_gardens_data[:, 0]), np.mean(riverside_reserve_data[:, 0])],
    "Hawks": [np.mean(central_park_data[:, 1]), np.mean(urban_gardens_data[:, 1]), np.mean(riverside_reserve_data[:, 1])],
    "Robins": [np.mean(central_park_data[:, 2]), np.mean(urban_gardens_data[:, 2]), np.mean(riverside_reserve_data[:, 2])]
}

fig, axes = plt.subplots(1, 2, figsize=(16, 8))

ax1 = axes[0]
bplot1 = ax1.boxplot(central_park_data, vert=False, patch_artist=True, positions=np.arange(3)*3, widths=0.6)
bplot2 = ax1.boxplot(urban_gardens_data, vert=False, patch_artist=True, positions=np.arange(3)*3 + 1, widths=0.6)
bplot3 = ax1.boxplot(riverside_reserve_data, vert=False, patch_artist=True, positions=np.arange(3)*3 + 2, widths=0.6)

consistent_color = 'lightblue'
for bplot in [bplot1, bplot2, bplot3]:
    for patch in bplot['boxes']:
        patch.set_facecolor(consistent_color)
    for median in bplot['medians']:
        median.set(color='darkred', linewidth=2)

ax1.set_title('Urban Birdwatching Trends:\nSightings Across Parks', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Number of Sightings', fontsize=14)
ax1.set_ylabel('Bird Species', fontsize=14)
ax1.set_yticks([0.5, 3.5, 6.5])
ax1.set_yticklabels(species)

ax2 = axes[1]
index = np.arange(len(parks))
bar_width = 0.25

for i, (species_name, averages) in enumerate(avg_sightings.items()):
    ax2.barh(index + i * bar_width, averages, bar_width, alpha=0.7, color=consistent_color)

ax2.set_title('Average Sightings Per Park\nFor Each Species', fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel('Average Number of Sightings', fontsize=14)
ax2.set_ylabel('Parks', fontsize=14)
ax2.set_yticks(index + bar_width)
ax2.set_yticklabels(parks)

plt.tight_layout()
plt.show()