import matplotlib.pyplot as plt
import numpy as np

cities = ['Selene', 'Zephyr', 'Aurora', 'Nyx', 'Lunaris', 'Aether', 'Solara', 'Eldoria']
years = ['2000', '1990', '2020', '2010']

population_data = {
    'Lunaris': [1.2, 1.5, 1.7, 2.0],
    'Selene': [0.8, 1.0, 1.3, 1.8],
    'Aurora': [1.7, 2.0, 2.2, 2.5],
    'Eldoria': [0.9, 1.1, 1.4, 1.6],
    'Nyx': [1.1, 1.3, 1.6, 2.1],
    'Solara': [1.4, 1.6, 1.9, 2.3],
    'Zephyr': [0.7, 0.9, 1.2, 1.5],
    'Aether': [1.0, 1.3, 1.5, 1.9]
}

fig, ax = plt.subplots(figsize=(14, 8))
bar_positions = np.arange(len(years))
colors = ['skyblue', 'gold', 'green', 'pink', 'orange', 'magenta', 'cyan', 'navy']

# Initialize bottom array with zeros
bottom = np.zeros(len(years))

for i, city in enumerate(cities):
    ax.bar(
        bar_positions,
        population_data[city],
        bottom=bottom,
        color=colors[i],
        edgecolor='gray',
        label=city,
        alpha=0.7
    )
    # Update the bottom position to stack the next bars on top of the current city’s bars
    bottom += np.array(population_data[city])

ax.set_title('City Population Dynamics in Elvarna (Different Periods)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Timeframes', fontsize=14)
ax.set_ylabel('Inhabitants Count (millions)', fontsize=14)
ax.set_xticks(bar_positions)
ax.set_xticklabels(years, fontsize=12)
ax.legend(title='Municipalities', title_fontsize='13', fontsize=11, loc='best')

ax.grid(True, linestyle='-', alpha=0.4)

plt.tight_layout()
plt.show()