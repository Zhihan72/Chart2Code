import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2100, 2151)

mammals_population = 5000 + 80 * (years - 2100) - 0.5 * (years - 2100)**2
birds_population = 3000 + 50 * (years - 2100)
reptiles_population = 2000 * np.sin(0.1 * (years - 2100)) + 3000
amphibians_population = 1500 * np.exp(0.02 * (years - 2100))
fish_population = 7000 - 30 * (years - 2100)

mammals_population = np.clip(mammals_population, 0, None)
fish_population = np.clip(fish_population, 0, None)

species_data = np.vstack([mammals_population, birds_population, reptiles_population, amphibians_population, fish_population])

plt.figure(figsize=(16, 10))

plt.stackplot(years, species_data, labels=['Mammals', 'Birds', 'Reptiles', 'Amphibians', 'Fish'],
              colors=['#FFD700', '#8B4513', '#7B68EE', '#4682B4', '#228B22'], alpha=0.7)

plt.title("Species Population Trends (2100-2150)", fontsize=18, fontweight='medium', color='#555555')
plt.xlabel("Year", fontsize=13, fontstyle='italic')
plt.ylabel("Population (Thousands)", fontsize=13, fontstyle='italic')

plt.xticks(years[::5], rotation=30)
plt.yticks(np.arange(0, 21000, 2500))
plt.grid(False)

plt.legend(loc='upper right', fontsize=10, facecolor='white', edgecolor='#DDDDDD')

plt.annotate('Bird Peak', xy=(2130, birds_population[30]), xytext=(2110, 19000),
             arrowprops=dict(arrowstyle='-[', color='gray'), fontsize=10, color='darkblue')
plt.annotate('Fish Decline', xy=(2140, fish_population[40]), xytext=(2120, 4000),
             arrowprops=dict(arrowstyle='-[', color='gray'), fontsize=10, color='darkred')

plt.tight_layout()

plt.show()