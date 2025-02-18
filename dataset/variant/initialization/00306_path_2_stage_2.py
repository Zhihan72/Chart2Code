import matplotlib.pyplot as plt
import numpy as np

# Randomly change the titles and labels
titles = ['Urban Wildlife Spots', 'City Nature Alerts', 'Species Encounters in Town']
x_labels = ['Size of Park (hectares)', 'Park Space (ha)', 'Land Measurement (hectares)']
y_labels = ['Sightings Per Month', 'Monthly Observations', 'Creatures Counted Monthly']

title = np.random.choice(titles)
xlabel = np.random.choice(x_labels)
ylabel = np.random.choice(y_labels)

park_areas = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

species_data = {
    'Squirrels': {
        'sightings': np.array([20, 30, 50, 70, 65, 80, 75, 90, 100, 110]),
        'marker': 'o',
        'color': '#FF5733'
    },
    'Pigeons': {
        'sightings': np.array([40, 50, 60, 80, 85, 100, 95, 105, 120, 130]),
        'marker': '^',
        'color': '#1F618D'
    },
    'Raccoons': {
        'sightings': np.array([5, 15, 20, 30, 25, 40, 45, 60, 70, 80]),
        'marker': 's',
        'color': '#239B56'
    },
    'Coyotes': {
        'sightings': np.array([2, 5, 8, 12, 10, 15, 18, 25, 30, 35]),
        'marker': 'D',
        'color': '#F4D03F'
    },
}

plt.figure(figsize=(12, 7))

for species, data in species_data.items():
    np.random.shuffle(data['sightings'])
    plt.scatter(park_areas, data['sightings'], label=species, marker=data['marker'],
                color=data['color'], s=100, alpha=0.7, edgecolors='k')

plt.title(title, fontsize=16, color='darkgreen')
plt.xlabel(xlabel, fontsize=12)
plt.ylabel(ylabel, fontsize=12)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend(title='Species Types', fontsize=10)
plt.tight_layout()

plt.show()