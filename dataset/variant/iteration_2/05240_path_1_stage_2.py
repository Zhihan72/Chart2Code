import matplotlib.pyplot as plt
import numpy as np

continents = ['South America', 'Asia', 'Europe', 'North America', 'Africa']
animals = ['Condors', 'Pandas', 'Tigers', 'Elephants', 'Bears']

data = [
    [0, 0, 0, 0, 1.5],
    [0, 1.5, 1.2, 0, 0],
    [0, 0, 0, 0.4, 0],
    [1.2, 0, 0, 1.8, 0.5],
    [10, 0.7, 0, 0.2, 0]
]
data_transposed = np.array(data).T

# Change: Altered color scheme
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

fig, ax = plt.subplots(figsize=(12, 8))

bottom_values = np.zeros(len(continents))
# Change: Different marker styles and border properties
markers = ['x', 'o', 's', '^', 'D']  # Different markers
line_styles = ['-', '--', '-.', ':', (0, (5, 1))]  # Different line styles
for idx, (animal_data, color) in enumerate(zip(data_transposed, colors)):
    ax.bar(continents, animal_data, label=animals[idx], color=color, bottom=bottom_values, edgecolor='gray', linestyle=line_styles[idx % len(line_styles)], hatch=markers[idx % len(markers)])
    bottom_values += animal_data

for continent_idx, continent_data in enumerate(data):
    bottom = 0
    for animal_idx, value in enumerate(continent_data):        
        if value > 0:
            ax.text(continent_idx, bottom + value / 2, f'{value}', ha='center', va='center', color='white', fontsize=9, fontweight='bold')
        bottom += value

# Change: Modified chart aesthetic elements
ax.set_title('Animal Revival Numbers by Continent (2015-2025)', fontsize=14, fontweight='bold', pad=20, loc='center')
ax.set_xlabel('Continents', fontsize=12, labelpad=15)
ax.set_ylabel('Population Increase (Thousands)', fontsize=12, labelpad=15)
ax.legend(title='Animals', loc='best')  # Changed legend location
ax.yaxis.grid(True, linestyle=':', alpha=0.5)  # Changed grid style

plt.tight_layout()
plt.show()