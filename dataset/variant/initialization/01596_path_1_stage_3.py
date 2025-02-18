import numpy as np
import matplotlib.pyplot as plt

# Define habitat names and dummy year range for labels
habitats = ["TropRF", "TempF", "BorF", "Mangr", "Savn"]
years = np.arange(2030, 2040)

# Sample data arrays
mammals = np.array([
    [24, 22, 21, 30, 28, 27, 26, 25, 24, 23],
    [28, 29, 35, 29, 32, 31, 30, 34, 33, 32],
    [21, 23, 20, 24, 21, 25, 20, 22, 24, 22],
    [24, 22, 21, 20, 25, 24, 25, 23, 24, 23],
    [19, 21, 17, 23, 20, 21, 18, 16, 22, 15]
])
birds = np.array([
    [30, 31, 27, 25, 28, 30, 26, 29, 28, 32],
    [27, 22, 21, 20, 23, 24, 26, 21, 25, 20],
    [34, 32, 29, 35, 31, 28, 30, 32, 29, 33],
    [31, 33, 31, 35, 31, 34, 34, 30, 32, 32],
    [27, 25, 29, 30, 25, 28, 26, 24, 28, 30]
])
reptiles = np.array([
    [17, 13, 10, 16, 14, 15, 15, 11, 12, 13],
    [11, 10, 14, 13, 10, 12, 15, 11, 11, 10],
    [9, 12, 5, 13, 8, 6, 10, 11, 7, 10],
    [12, 13, 10, 15, 12, 13, 14, 14, 11, 10],
    [5, 8, 6, 5, 5, 7, 9, 7, 6, 8]
])
amphibians = np.array([
    [17, 19, 15, 14, 16, 16, 19, 20, 18, 17],
    [13, 10, 13, 15, 14, 12, 11, 10, 14, 11],
    [13, 10, 12, 10, 15, 11, 13, 11, 16, 14],
    [12, 11, 16, 14, 12, 10, 15, 14, 13, 10],
    [34, 33, 31, 31, 32, 33, 30, 35, 34, 32]
])
insects = np.array([
    [15, 16, 17, 16, 15, 15, 16, 16, 15, 16],
    [21, 20, 23, 22, 21, 21, 22, 21, 20, 21],
    [20, 30, 24, 22, 28, 18, 29, 23, 27, 24],
    [19, 20, 20, 20, 19, 19, 19, 20, 19, 19],
    [19, 11, 16, 14, 9, 12, 18, 16, 20, 13]
])

species_data = [mammals, birds, reptiles, amphibians, insects]
species_names = ['Mammals', 'Birds', 'Reptiles', 'Amphibians', 'Insects']
colors = plt.cm.Set3(np.linspace(0, 1, len(species_data)))

fig, ax = plt.subplots(figsize=(12, 7))

left_offset = np.zeros(len(habitats))

for i, species in enumerate(species_data):
    species_sum = species.sum(axis=1)
    ax.barh(habitats, species_sum, color=colors[i], left=left_offset, edgecolor='grey', label=species_names[i])
    left_offset += species_sum

ax.axvline(0, color='black', lw=1)
ax.set_xticks(np.arange(-500, 500, 50))
ax.set_xlabel('Biodiv Contribution', fontsize=12)
ax.set_title("Diverging Biodiv Contributions Across Habitats", fontsize=14)
ax.legend(title='Species')

plt.tight_layout()
plt.show()