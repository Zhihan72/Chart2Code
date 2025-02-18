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

values = []
colors = []
# New color set to replace the original ones
new_colors = {
    'Solar': '#FF5733',
    'Wind': '#33FFBD',
    'Hydro': '#3380FF',
    'Biomass': '#FF33EC'
}

for continent, sources in renewable_data.items():
    for source, value in sources.items():
        values.append(value)
        colors.append(new_colors[source])

plt.figure(figsize=(14, 10))
squarify.plot(sizes=values, color=colors, alpha=0.6)

plt.grid(False)
plt.axis('off')
plt.tight_layout()
plt.show()