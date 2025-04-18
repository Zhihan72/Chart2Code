import numpy as np
import matplotlib.pyplot as plt

habitats = ["Raimforest Tropical", "Borest Foo", "Forest Temperate", "Grovesman", "Vasann"]
years = np.arange(2035, 2045)

# Create percentage data for different animal groups
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

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.18

species_data = [mammals, birds, amphibians, insects]
colors = ['#377eb8', '#4daf4a', '#ff7f00', '#984ea3']
x_indices = np.arange(len(years))

for i, species in enumerate(species_data):
    for j, habitat in enumerate(habitats):
        ax.bar(x_indices + (i * bar_width), species[j], bar_width, color=colors[i], alpha=0.8)

ax.set_xticks(x_indices + bar_width * (len(species_data) - 1) / 2)
ax.set_xticklabels(years, fontsize=10)
ax.set_xlabel('Yearly Progression', fontsize=13)
ax.set_ylabel('Bio (%) Index', fontsize=12)
ax.set_title("Decadal Shifts in Bio-vibrancy in Select Environments (2035-2044)", fontsize=15)

plt.tight_layout()
plt.show()