import numpy as np
import matplotlib.pyplot as plt

habitats = ["Tropical", "Temperate", "Boreal", "Mangroves", "Savanna"]
years = np.arange(2030, 2040)

mammals = np.array([30, 35, 20, 25, 15])
birds = np.array([25, 20, 35, 30, 30])
reptiles = np.array([10, 10, 5, 15, 5])
amphibians = np.array([20, 15, 10, 10, 30])
insects = np.array([15, 20, 30, 20, 20])
fish = np.array([12, 18, 25, 22, 17])

species_data = np.array([mammals, birds, reptiles, amphibians, insects, fish]) - 20

fig, ax = plt.subplots(figsize=(10, 6))

x_ticks = np.arange(len(habitats))
bar_width = 0.35

# Shuffled colors
colors = ['#9370DB', '#FFD700', '#32CD32', '#1E90FF', '#8B4513', '#FF4500']
species_names = ['Rptls', 'Inscts', 'Brds', 'Fish', 'Amphbs', 'Mam']

bottom_positive = np.zeros(len(habitats))
bottom_negative = np.zeros(len(habitats))

for i, species in enumerate(species_data):
    positive_values = np.clip(species, 0, None)
    negative_values = np.clip(species, None, 0)

    ax.bar(x_ticks, positive_values, width=bar_width, color=colors[i], alpha=0.8,
           bottom=bottom_positive, label=species_names[i], edgecolor='grey', linestyle='--')
    ax.bar(x_ticks, negative_values, width=bar_width, color=colors[i], alpha=0.8,
           bottom=bottom_negative, edgecolor='grey', linestyle='--')

    bottom_positive += positive_values
    bottom_negative += negative_values

ax.set_xticks(x_ticks)
ax.set_xticklabels(habitats, fontsize=10)

plt.title("Diverging Biodiversity Trends by Habitat", fontsize=16)
plt.xlabel('Habitats', fontsize=12)
plt.ylabel('Diverging from Base (%)', fontsize=12)
ax.axhline(0, color='black', linewidth=1.0, linestyle=':')

plt.legend(title='Groups', loc='lower right', fontsize=9)  # Adjusted legend position and font size
plt.grid(True, linestyle='-.', linewidth=0.7)
plt.tight_layout()

plt.show()