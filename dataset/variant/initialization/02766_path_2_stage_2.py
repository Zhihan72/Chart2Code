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
# New set of colors for visualization
base_colors = {
    'Solar': '#FFA07A',  # Light Salmon
    'Wind': '#8FBC8F',   # Dark Sea Green
    'Hydro': '#4682B4',  # Steel Blue
    'Biomass': '#D8BFD8' # Thistle
}

for continent, sources in renewable_data.items():
    for source, value in sources.items():
        labels.append(f'{source}\n{continent}\n{value}GWh')
        values.append(value)
        colors.append(base_colors[source])

plt.figure(figsize=(14, 10))
squarify.plot(sizes=values, label=labels, color=colors, alpha=0.8, text_kwargs={'fontsize': 10, 'weight': 'bold', 'wrap': True})

plt.title('Continent Energy Distribution\nAlternate Sources Overview', fontsize=18, fontweight='bold', pad=30)
plt.axis('off')

plt.tight_layout()
plt.show()