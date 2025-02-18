import matplotlib.pyplot as plt
import numpy as np

cities = ['Lunaris', 'Selene', 'Aurora', 'Eldoria', 'Nyx', 'Solara']
years = ['1990', '2000', '2010', '2020']

# Randomly altered population data
population_data = {
    'Lunaris': [1.5, 1.2, 2.0, 1.7],  # Swapped some values
    'Selene': [1.0, 0.8, 1.8, 1.3],  # Swapped some values
    'Aurora': [2.2, 1.7, 2.5, 2.0],  # Swapped some values
    'Eldoria': [1.4, 0.9, 1.6, 1.1],  # Swapped some values
    'Nyx': [1.6, 1.1, 2.1, 1.3],  # Swapped some values
    'Solara': [1.9, 1.4, 2.3, 1.6],  # Swapped values
}

colors = ['darkblue', 'teal', 'purple', 'darkgreen', 'red', 'gold']

fig, ax = plt.subplots(figsize=(14, 8))

bottom = np.zeros(len(years))

for i, city in enumerate(cities):
    plt.bar(
        years,
        population_data[city],
        bottom=bottom,
        color=colors[i],
        edgecolor='black',
        label=city,
        alpha=0.8
    )
    bottom += np.array(population_data[city])

ax.set_title('Population Growth in Major Cities of Elvarna (1990-2020)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Years', fontsize=14)
ax.set_ylabel('Population (in millions)', fontsize=14)
ax.legend(title='Cities', title_fontsize='13', fontsize=11, loc='upper left', bbox_to_anchor=(1, 1))
ax.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()