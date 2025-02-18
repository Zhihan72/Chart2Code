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

new_colors = ['#FF5733', '#33FF57', '#3357FF', '#F5A623', '#8E44AD']

fig, ax = plt.subplots(figsize=(14, 8))

x = np.arange(len(continents))
bar_width = 0.15

for i, (source, color) in enumerate(zip(renewable_sources, new_colors)):
    ax.bar(x + i * bar_width, renewable_data[:, i], bar_width, color=color, edgecolor='black', label=source)

ax.set_title("2023 Renewable Energy Adoption Across Continents\nPercentage Distribution by Source", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Continent", fontsize=12)
ax.set_ylabel("Percentage (%)", fontsize=12)
ax.set_xticks(x + bar_width * (len(renewable_sources) / 2 - 0.5))
ax.set_xticklabels(continents)

ax.legend(title="Energy Source", bbox_to_anchor=(1, 1), loc='upper left')
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()