import matplotlib.pyplot as plt
import numpy as np

continents = ['Africa', 'Europe', 'South America', 'Australia']
renewable_sources = ['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass']

renewable_data = np.array([
    [40, 25, 30, 3, 2],
    [20, 35, 25, 10, 10],
    [15, 20, 50, 5, 10],
    [45, 30, 10, 10, 5]
])

# Defining a new set of colors for each renewable source
new_colors = ['#FF5733', '#33FF57', '#3357FF', '#F5A623', '#8E44AD']

fig, ax = plt.subplots(figsize=(14, 8))

for i, (continent, data) in enumerate(zip(continents, renewable_data)):
    bottom = 0
    for j, (source, percent) in enumerate(zip(renewable_sources, data)):
        ax.barh(continent, percent, color=new_colors[j], edgecolor='black', left=bottom, label=source if i == 0 else "")
        ax.text(bottom + percent / 2, i, f'{percent}%', va='center', ha='center', fontsize=9, color='black', weight='bold')
        bottom += percent

ax.set_title("2023 Renewable Energy Adoption Across Continents\nPercentage Distribution by Source", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Percentage (%)", fontsize=12)
ax.set_ylabel("Continent", fontsize=12)

ax.set_xlim(0, 100)

handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(), loc='upper left', title="Energy Source", bbox_to_anchor=(1, 1))

ax.xaxis.grid(True, linestyle='--', alpha=0.6)
ax.yaxis.grid(False)

plt.tight_layout()
plt.show()