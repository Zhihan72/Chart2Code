import matplotlib.pyplot as plt
import squarify

sectors = ['Residential Areas', 'Commercial Districts', 'Industrial Zones', 'Public Facilities', 'Transportation']
energy_sources = ['Solar', 'Wind', 'Bioenergy', 'Hydro']

# Data is shuffled to randomly alter content while maintaining dimensional structure
data = {
    'Residential Areas': [20, 50, 10, 20],
    'Commercial Districts': [10, 20, 30, 40],
    'Industrial Zones': [50, 25, 15, 10],
    'Public Facilities': [40, 20, 30, 10],
    'Transportation': [40, 10, 20, 30]
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