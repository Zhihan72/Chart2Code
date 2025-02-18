import matplotlib.pyplot as plt
import squarify

sectors = ['Residential Areas', 'Commercial Districts', 'Industrial Zones', 'Public Facilities', 'Transportation']
energy_sources = ['Solar', 'Wind', 'Bioenergy', 'Hydro']

data = {
    'Residential Areas': [50, 20, 20, 10],
    'Commercial Districts': [40, 30, 10, 20],
    'Industrial Zones': [15, 50, 10, 25],
    'Public Facilities': [30, 10, 40, 20],
    'Transportation': [30, 20, 10, 40]
}

sizes = []
for sector in sectors:
    for percent in data[sector]:
        sizes.append(percent)

single_color = '#FFD700'  # Gold

plt.figure(figsize=(14, 8))
squarify.plot(sizes=sizes, color=[single_color] * len(sizes), alpha=0.7, edgecolor="grey", linewidth=1.5)

plt.axis('off')
plt.tight_layout()
plt.show()