import matplotlib.pyplot as plt
import squarify

# Manually shuffled sector and energy source names
sectors = ['Industrial Sectors', 'Transit Areas', 'Housing Zones', 'Business Centers']
energy_sources = ['Wind', 'Solar', 'Hydro', 'Bioenergy']

data = {
    'Industrial Sectors': [15, 50, 10, 25],
    'Transit Areas': [30, 20, 10, 40],
    'Housing Zones': [50, 20, 20, 10],
    'Business Centers': [40, 30, 10, 20]
}

labels = []
sizes = []

# Updated labels based on the new manual shuffle
for sector in sectors:
    for energy, percent in zip(energy_sources, data[sector]):
        labels.append(f'{sector}\n{energy}: {percent}%')
        sizes.append(percent)

colors = ['#FFD700', '#1E90FF', '#3CB371', '#8B4513']

plt.figure(figsize=(14, 8))
squarify.plot(sizes=sizes, label=labels, color=colors * len(sectors), alpha=0.7)

plt.axis('off')
plt.tight_layout()
plt.show()