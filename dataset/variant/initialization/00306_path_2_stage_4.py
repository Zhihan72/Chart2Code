import matplotlib.pyplot as plt
import numpy as np

# Static selection based on reference code - no randomness
title = 'Urban Wildlife Spots'
xlabel = 'Size of Park (hectares)'
ylabel = 'Sightings Per Month'

# Fixed park areas and stats per species
park_areas = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
species_data = {
    'Squirrels': {
        'sightings': np.array([20, 30, 50, 70, 65, 80, 75, 90, 100, 110]),
        'marker': 'o',
        'linestyle': '-'
    },
    'Pigeons': {
        'sightings': np.array([40, 50, 60, 80, 85, 100, 95, 105, 120, 130]),
        'marker': '^',
        'linestyle': '--'
    },
    'Raccoons': {
        'sightings': np.array([5, 15, 20, 30, 25, 40, 45, 60, 70, 80]),
        'marker': 's',
        'linestyle': ':'
    },
    'Coyotes': {
        'sightings': np.array([2, 5, 8, 12, 10, 15, 18, 25, 30, 35]),
        'marker': 'D',
        'linestyle': '-.'
    },
}

# Apply consistent color across all groups
common_color = 'blue'

plt.figure(figsize=(12, 7))
for species, data in species_data.items():
    plt.plot(park_areas, data['sightings'], label=species, marker=data['marker'],
             color=common_color, linestyle=data['linestyle'], linewidth=1, alpha=0.7)

plt.title(title, fontsize=16, color='darkgreen')
plt.xlabel(xlabel, fontsize=12)
plt.ylabel(ylabel, fontsize=12)
plt.grid(True, linestyle='-', linewidth=0.5)
plt.legend(title='Species Types', fontsize=10)
plt.tight_layout()
plt.show()