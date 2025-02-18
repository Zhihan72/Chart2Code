import matplotlib.pyplot as plt
import numpy as np

# Population data in millions over three decades for cities in Elvarna
cities = ['Lunaris', 'Selene', 'Aurora', 'Eldoria', 'Nyx', 'Solara']
years = ['1990', '2000', '2010', '2020']

population_data = {
    'Lunaris': [1.2, 1.5, 1.7, 2.0],
    'Selene': [0.8, 1.0, 1.3, 1.8],
    'Aurora': [1.7, 2.0, 2.2, 2.5],
    'Eldoria': [0.9, 1.1, 1.4, 1.6],
    'Nyx': [1.1, 1.3, 1.6, 2.1],
    'Solara': [1.4, 1.6, 1.9, 2.3],
}

colors = ['darkblue', 'teal', 'purple', 'darkgreen', 'red', 'gold']

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Initialize a list with zeros to use as the base for the stacking
bottom = np.zeros(len(years))

# Plotting data for each city as stacked bars
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
    # Update the bottom to be the top of the current city's bars for stacking
    bottom += np.array(population_data[city])

# Titles and Labels
ax.set_title('Population Growth in Major Cities of Elvarna (1990-2020)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Years', fontsize=14)
ax.set_ylabel('Population (in millions)', fontsize=14)
ax.legend(title='Cities', title_fontsize='13', fontsize=11, loc='upper left', bbox_to_anchor=(1, 1))

# Customize the grid
ax.grid(True, linestyle='--', alpha=0.6)

# Make layout adjustments to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()