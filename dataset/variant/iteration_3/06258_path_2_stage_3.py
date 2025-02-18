import matplotlib.pyplot as plt
import numpy as np

regions = ['Amazon', 'Sahara', 'Taiga', 'Great Plains', 'Himalayas', 'Alps']
species = ['Tree', 'Shrub', 'Grass', 'Flower', 'Fern']
species_distribution = [
    [50, 5, 10, 30, 5], 
    [2, 15, 70, 5, 8],  
    [60, 10, 15, 5, 10],  
    [35, 5, 50, 8, 2],   
    [10, 20, 5, 60, 5],   
    [25, 10, 5, 50, 10] 
]

carbon_sequestration = [300, 20, 150, 100, 200, 120]

# Shuffle the colors manually
colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(species)))
colors = [colors[2], colors[0], colors[4], colors[1], colors[3]]  # Manually shuffled order

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

avg_distribution = np.mean(np.array(species_distribution), axis=0)

sequence_ids = np.arange(len(regions))
bottom_vals = np.zeros(len(regions))

for i, specie in enumerate(species):
    currentSpeciesDistribution = np.array([dist[i] - avg_distribution[i] for dist in species_distribution])
    ax1.bar(sequence_ids, currentSpeciesDistribution, 0.5, color=colors[i], bottom=bottom_vals)
    bottom_vals += currentSpeciesDistribution

ax1.set_xlabel('Regions', fontsize=12)
ax1.set_ylabel('Deviation from Average (%)', fontsize=12)
ax1.set_title('Diverging Plant Species Distribution', fontsize=14, fontweight='bold', pad=20)
ax1.set_xticks(sequence_ids)
ax1.set_xticklabels(regions)
ax1.axhline(0, color='black', linewidth=0.8, linestyle='--')

bars = ax2.barh(regions, carbon_sequestration, color='dodgerblue', edgecolor='black')

ax2.set_xlabel('Carbon Sequestration (Million Metric Tons)', fontsize=12)
ax2.set_title('Carbon Sequestration by Region', fontsize=14, fontweight='bold', pad=20)

for bar in bars:
    width = bar.get_width()
    ax2.annotate(f'{width}', 
                 xy=(width, bar.get_y() + bar.get_height()/2), 
                 xytext=(3, 0), 
                 textcoords='offset points', 
                 ha='left', va='center', fontsize=10)

plt.tight_layout()
plt.show()