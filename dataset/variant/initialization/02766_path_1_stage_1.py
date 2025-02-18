import matplotlib.pyplot as plt
import squarify

renewable_data = {
    'North America': {'Solar': 300, 'Wind': 500, 'Hydro': 700, 'Biomass': 200},
    'South America': {'Solar': 200, 'Wind': 300, 'Hydro': 600, 'Biomass': 150},
    'Europe': {'Solar': 400, 'Wind': 700, 'Hydro': 500, 'Biomass': 250},
    'Africa': {'Solar': 250, 'Wind': 150, 'Hydro': 300, 'Biomass': 100},
    'Asia': {'Solar': 600, 'Wind': 800, 'Hydro': 900, 'Biomass': 300},
    'Oceania': {'Solar': 150, 'Wind': 100, 'Hydro': 250, 'Biomass': 80}
}

labels = []
values = []
colors = []
base_colors = {
    'Solar': '#99AA88',
    'Wind': '#FFDD44',
    'Hydro': '#77CCAA',
    'Biomass': '#44BBFF'
}

for continent, sources in renewable_data.items():
    for source, value in sources.items():
        labels.append(f'{continent}\n{source}\n{value} GWh')
        values.append(value)
        colors.append(base_colors[source])

plt.figure(figsize=(14, 10))
squarify.plot(sizes=values, label=labels, color=colors, alpha=0.6, text_kwargs={'fontsize': 12, 'style': 'italic', 'wrap': True})

plt.title('Renewable Energy Distribution by Continent\nEnergy Generation in GWh', fontsize=16, fontweight='light', pad=15)
plt.grid(False)
plt.axis('on')
plt.xticks([], [])
plt.yticks([], [])

plt.tight_layout()
plt.show()