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

colors = ['#8B4513', '#1E90FF', '#32CD32', '#FFD700', '#FF4500', '#9370DB']
species_names = ['Mam', 'Brds', 'Rptls', 'Amphbs', 'Inscts', 'Fish']

bottom_positive = np.zeros(len(habitats))
bottom_negative = np.zeros(len(habitats))

for i, species in enumerate(species_data):
    positive_values = np.clip(species, 0, None)
    negative_values = np.clip(species, None, 0)

    ax.bar(x_ticks, positive_values, width=bar_width, color=colors[i], alpha=0.8,
           bottom=bottom_positive, label=species_names[i])
    ax.bar(x_ticks, negative_values, width=bar_width, color=colors[i], alpha=0.8,
           bottom=bottom_negative)

    bottom_positive += positive_values
    bottom_negative += negative_values

ax.set_xticks(x_ticks)
ax.set_xticklabels(habitats, fontsize=10)

plt.title("Diverging Biodiversity Trends by Habitat", fontsize=16)
plt.xlabel('Habitats', fontsize=12)
plt.ylabel('Diverging from Base (%)', fontsize=12)
ax.axhline(0, color='black', linewidth=0.8)

plt.legend(title='Groups', loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10)
plt.tight_layout()

plt.show()