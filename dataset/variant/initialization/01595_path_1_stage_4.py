import numpy as np
import matplotlib.pyplot as plt

habitats = ["Trop Rain", "Temp Forest", "Boreal", "Mangroves", "Savanna"]
years = np.arange(2030, 2040)

# Data arrays
mammals = np.array([
    [30, 28, 27, 26, 25, 24, 24, 23, 22, 21],
    [35, 34, 33, 32, 32, 31, 30, 29, 29, 28],
    [20, 20, 21, 21, 22, 22, 23, 24, 24, 25],
    [25, 25, 24, 24, 23, 23, 22, 22, 21, 20],
    [15, 16, 17, 18, 19, 20, 21, 21, 22, 23]
])

birds = np.array([
    [25, 26, 27, 28, 28, 29, 30, 30, 31, 32],
    [20, 20, 21, 21, 22, 23, 24, 25, 26, 27],
    [35, 34, 33, 32, 32, 31, 30, 29, 29, 28],
    [30, 31, 31, 31, 32, 32, 33, 34, 34, 35],
    [30, 29, 28, 28, 27, 27, 26, 25, 25, 24]
])

reptiles = np.array([
    [10, 11, 12, 13, 13, 14, 15, 15, 16, 17],
    [10, 10, 11, 11, 12, 13, 13, 14, 14, 15],
    [5, 6, 7, 8, 9, 10, 10, 11, 12, 13],
    [15, 14, 14, 13, 13, 12, 12, 11, 10, 10],
    [5, 5, 5, 6, 6, 7, 7, 8, 8, 9]
])

amphibians = np.array([
    [20, 19, 19, 18, 17, 17, 16, 16, 15, 14],
    [15, 14, 14, 13, 13, 12, 11, 11, 10, 10],
    [10, 11, 11, 12, 13, 13, 14, 15, 15, 16],
    [10, 10, 11, 12, 12, 13, 14, 14, 15, 16],
    [30, 31, 31, 32, 32, 33, 33, 34, 34, 35]
])

insects = np.array([
    [15, 16, 15, 15, 17, 16, 15, 16, 16, 16],
    [20, 22, 21, 23, 21, 21, 22, 21, 21, 20],
    [30, 29, 28, 27, 24, 24, 23, 22, 20, 18],
    [20, 19, 19, 20, 20, 20, 19, 19, 20, 19],
    [20, 19, 19, 18, 16, 16, 13, 12, 11, 9]
])

species = [mammals, birds, reptiles, amphibians, insects]
species_names = ['Mammals', 'Birds', 'Reptiles', 'Amphibians', 'Insects']
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF66B3']  # Different color for each species

fig, ax = plt.subplots(figsize=(14, 8))

# Bar width and positions
bar_width = 0.1
index = np.arange(len(years))

for i, species_data in enumerate(species):
    for j, habitat in enumerate(habitats):
        plt.bar(index + (i - len(species) / 2) * bar_width + j, species_data[j], bar_width, label=species_names[i] if j == 0 else "", color=colors[i], alpha=0.8)

ax.set_xlabel('Years')
ax.set_ylabel('Biodiversity')
ax.set_title('Biodiversity Trends (2030-2039)')
ax.set_xticks(index + (0.5 * (len(species) - 1) * bar_width))
ax.set_xticklabels(years)
ax.legend(title="Species")

plt.tight_layout()
plt.show()