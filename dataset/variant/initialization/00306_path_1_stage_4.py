import matplotlib.pyplot as plt
import numpy as np

park_areas = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

species_data = {
    'Squirrels': {
        'sightings': [20, 30, 50, 70, 65, 80, 75, 90, 100, 110],
        'marker': 'D',  # Diamond marker
    },
    'Pigeons': {
        'sightings': [40, 50, 60, 80, 85, 100, 95, 105, 120, 130],
        'marker': 'v',  # Triangle down marker
    },
    'Raccoons': {
        'sightings': [5, 15, 20, 30, 25, 40, 45, 60, 70, 80],
        'marker': 'p',  # Plus (filled) marker
    },
}

colors = ['#FF5733', '#339BFF', '#33FF57']  # Different colors per species
linestyles = ['-', ':', '--']  # Random line styles

plt.figure(figsize=(12, 7))

for idx, (species, data) in enumerate(species_data.items()):
    plt.scatter(park_areas, data['sightings'], marker=data['marker'],
                color=colors[idx], s=100, alpha=0.7, edgecolors='k',
                linestyle=linestyles[idx], label=species)

plt.legend(facecolor='#f0f0f0', frameon=True, shadow=True)  # Modified legend
plt.grid(False)  # Assuming randomness means no grid here
plt.tight_layout()

plt.show()