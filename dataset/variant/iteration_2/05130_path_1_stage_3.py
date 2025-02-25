import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2100, 2151)

mammals_population = 5000 + 80 * (years - 2100) - 0.5 * (years - 2100)**2
birds_population = 3000 + 50 * (years - 2100)
reptiles_population = 2000 * np.sin(0.1 * (years - 2100)) + 3000
amphibians_population = 1500 * np.exp(0.02 * (years - 2100))
fish_population = 7000 - 30 * (years - 2100)
insects_population = 1000 * np.log1p(years - 2099) + 5000
plankton_population = 8000 + 300 * np.cos(0.2 * (years - 2100)) - 20 * (years - 2100)

mammals_population = np.clip(mammals_population, 0, None)
fish_population = np.clip(fish_population, 0, None)
plankton_population = np.clip(plankton_population, 0, None)

species_data = np.vstack([
    mammals_population, birds_population, reptiles_population,
    amphibians_population, fish_population, insects_population, plankton_population
])

plt.figure(figsize=(16, 10))

plt.stackplot(years, species_data, labels=[
    'Mammal Group', 'Avian Species', 'Scaly Creatures', 'Frogs and Toads', 'Sea Life', 'Creepy Crawlies', 'Microbiota'
], alpha=0.8)

plt.title("Species Forecast: Populations in Flux\n(2100-2150)", fontsize=20, fontweight='bold')
plt.xlabel("Calendar Year", fontsize=14)
plt.ylabel("Total Count (thousands)", fontsize=14)

plt.xticks(years[::5], rotation=45)
plt.yticks(np.arange(0, 21000, 2000))
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.legend(loc='upper left', fontsize=12, frameon=True)

plt.annotate('Critical Bird Rise', xy=(2130, birds_population[30]), xytext=(2115, 22000),
             arrowprops=dict(arrowstyle='->', color='black'), fontsize=12, color='black')
plt.annotate('Declining Fish Numbers', xy=(2140, fish_population[40]), xytext=(2120, 7000),
             arrowprops=dict(arrowstyle='->', color='black'), fontsize=12, color='black')

plt.tight_layout()
plt.show()