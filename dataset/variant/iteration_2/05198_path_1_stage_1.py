import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2023)

# Artificial data for populations (in millions) of various races in the fantasy world
dwarfs = np.array([1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.82, 1.88, 1.92, 1.95, 1.99, 2.02, 2.05, 2.1, 2.15, 2.2, 2.3])
humans = np.array([3, 3.1, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4, 5.6, 5.8, 6, 6.2, 6.4, 6.6, 6.8, 7, 7.2])
orcs = np.array([0.5, 0.55, 0.6, 0.65, 0.7, 0.9, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6])

# Combine data into an array for stacking
population_data = np.vstack([dwarfs, humans, orcs])

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, population_data, labels=['Dwarfs', 'Humans', 'Orcs'],
             colors=['#FFB266', '#8FB266', '#4D7399'], alpha=0.8)

ax.set_title("Population Growth in Fantasia (2000-2022)\nHow Various Races Thrived", fontsize=16, weight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Population (in millions)', fontsize=12)

ax.legend(loc='upper left', title='Race', bbox_to_anchor=(1, 1))

ax.grid(True, linestyle='--', alpha=0.5)
ax.set_xlim(years[0], years[-1])
ax.set_xticks(years[::2])
ax.set_xticklabels(years[::2], rotation=45, ha='right')

highlighted_year = 2015
highlighted_values = [dwarfs[15], humans[15], orcs[15]]
annotations = ['Steady growth in Dwarfs population', 'Humans remain the largest race', 'Sharp rise in Orc population']
cumulative = np.cumsum(highlighted_values)
for race, y, label in zip(annotations, cumulative, highlighted_values):
    plt.annotate(race, xy=(highlighted_year, y), xytext=(highlighted_year + 2, y + 1),
                 bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='white'),
                 arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, ha='center')

plt.tight_layout()
plt.show()