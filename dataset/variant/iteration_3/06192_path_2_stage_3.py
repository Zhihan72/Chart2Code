import matplotlib.pyplot as plt
import numpy as np

cities = ['Lunaris', 'Selene', 'Aurora', 'Eldoria', 'Nyx', 'Solara']
years = ['1990', '2000', '2010', '2020']

population_data = {
    'Lunaris': [1.5, 1.2, 2.0, 1.7],
    'Selene': [1.0, 0.8, 1.8, 1.3],
    'Aurora': [2.2, 1.7, 2.5, 2.0],
    'Eldoria': [1.4, 0.9, 1.6, 1.1],
    'Nyx': [1.6, 1.1, 2.1, 1.3],
    'Solara': [1.9, 1.4, 2.3, 1.6],
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
        alpha=0.8
    )
    bottom += np.array(population_data[city])

ax.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()