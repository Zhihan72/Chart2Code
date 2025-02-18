import matplotlib.pyplot as plt
import numpy as np

continents = ['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Australia']
flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Cookie Dough']

na_flavors = [35, 25, 15, 12, 13]
eu_flavors = [28, 30, 10, 20, 12]
asia_flavors = [20, 35, 25, 10, 10]
sa_flavors = [25, 20, 30, 10, 15]
africa_flavors = [15, 20, 10, 25, 30]
australia_flavors = [30, 25, 15, 10, 20]

flavor_data = [na_flavors, eu_flavors, asia_flavors, sa_flavors, africa_flavors, australia_flavors]
colors = ['#f3e5ab', '#8b4513', '#fc5a8d', '#98ff98', '#c0c0c0']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

bottoms = np.zeros(len(continents))
for idx, flavor in enumerate(flavors):
    ax1.bar(continents, [data[idx] for data in flavor_data],
            bottom=bottoms, color=colors[idx], edgecolor='black', alpha=0.7)
    bottoms += [data[idx] for data in flavor_data]

for cont_idx, cont_data in enumerate(flavor_data):
    bottom = 0
    for flavor_idx, value in enumerate(cont_data):
        ax1.text(cont_idx, bottom + value / 2, str(value) + '%', va='center', ha='center', color='white', fontweight='bold')
        bottom += value

ax1.set_xlabel("Continents", fontsize=12)
ax1.set_ylabel("Popularity Percentage (%)", fontsize=12)

years = np.arange(2013, 2024)
vanilla_growth = [20, 22, 23, 25, 26, 27, 29, 30, 32, 33, 34]

ax2.plot(years, vanilla_growth, marker='o', linestyle='-', color='#f3e5ab', linewidth=2, markersize=6)

for i, growth in enumerate(vanilla_growth):
    ax2.text(years[i], growth + 0.5, f'{growth}%', ha='center', fontsize=10)

ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Popularity Percentage (%)", fontsize=12)

fig.tight_layout()
plt.show()