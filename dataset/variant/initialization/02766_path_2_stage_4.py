import matplotlib.pyplot as plt
import squarify

renewable_data = {
    'North America': {'Solar': 300, 'Wind': 500, 'Hydro': 700, 'Biomass': 200, 'Geothermal': 100},
    'South America': {'Solar': 200, 'Wind': 300, 'Hydro': 600, 'Biomass': 150, 'Geothermal': 70},
    'Europe': {'Solar': 400, 'Wind': 700, 'Hydro': 500, 'Biomass': 250, 'Geothermal': 120},
    'Africa': {'Solar': 250, 'Wind': 150, 'Hydro': 300, 'Biomass': 100, 'Geothermal': 50},
    'Asia': {'Solar': 600, 'Wind': 800, 'Hydro': 900, 'Biomass': 300, 'Geothermal': 200},
    'Oceania': {'Solar': 150, 'Wind': 100, 'Hydro': 250, 'Biomass': 80, 'Geothermal': 40}
}

labels = []
values = []
colors = []
base_colors = {
    'Solar': '#FFA07A',
    'Wind': '#8FBC8F',
    'Hydro': '#4682B4',
    'Biomass': '#D8BFD8',
    'Geothermal': '#FFD700'
}

for continent, sources in renewable_data.items():
    for source, value in sources.items():
        labels.append(f'{source}\n{continent}\n{value}GWh')
        values.append(value)
        colors.append(base_colors[source])

plt.figure(figsize=(14, 10))
squarify.plot(sizes=values, label=labels, color=colors, alpha=0.8, text_kwargs={'fontsize': 10, 'weight': 'bold', 'wrap': True})

plt.axis('off')
plt.show()