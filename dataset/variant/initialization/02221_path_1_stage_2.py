import matplotlib.pyplot as plt
import squarify

sectors = ['Residential Areas', 'Commercial Districts', 'Industrial Zones', 'Transportation']
energy_sources = ['Solar', 'Wind', 'Bioenergy', 'Hydro']

data = {
    'Residential Areas': [50, 20, 20, 10],
    'Commercial Districts': [40, 30, 10, 20],
    'Industrial Zones': [15, 50, 10, 25],
    'Transportation': [30, 20, 10, 40]
}

labels = []
sizes = []

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