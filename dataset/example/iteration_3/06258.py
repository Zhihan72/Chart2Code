import matplotlib.pyplot as plt
import numpy as np

# Backstory: Analysis of Plant Species Distribution and Carbon Sequestration in Various Regions
# This study focuses on understanding how different regions contribute to carbon sequestration through various plant species. 

# Data
regions = ['Amazon', 'Sahara', 'Taiga', 'Great Plains', 'Himalayas', 'Alps']
species = ['Tree', 'Shrub', 'Grass', 'Flower', 'Fern']
species_distribution = [
    [50, 5, 10, 30, 5],    # Amazon
    [2, 15, 70, 5, 8],     # Sahara
    [60, 10, 15, 5, 10],   # Taiga
    [35, 5, 50, 8, 2],     # Great Plains
    [10, 20, 5, 60, 5],    # Himalayas
    [25, 10, 5, 50, 10]    # Alps
]

carbon_sequestration = [300, 20, 150, 100, 200, 120]  # in Million Metric Tons

# Bar colors
colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(species)))

# Initialize figure and axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Bar chart for species distribution
bar_width = 0.1
sequence_ids = np.arange(len(regions))

# Stacked bar chart for species distribution
for i, specie in enumerate(species):
    currentSpeciesDistribution = [dist[i] for dist in species_distribution]
    bottom_vals = np.sum([list(species_distribution[j][:i]) for j in range(len(regions))], axis=1) if i > 0 else None
    ax1.bar(sequence_ids + i * bar_width, currentSpeciesDistribution, bar_width, label=specie, color=colors[i], bottom=bottom_vals)

# Customize bar chart    
ax1.set_xlabel('Regions', fontsize=12)
ax1.set_ylabel('Species Distribution (%)', fontsize=12)
ax1.set_title('Plant Species Distribution Across Various Regions', fontsize=14, fontweight='bold', pad=20)
ax1.set_xticks(sequence_ids + bar_width * 2.5)
ax1.set_xticklabels(regions)
ax1.legend(title='Species', loc='upper right')
ax1.grid(True, linestyle='--', alpha=0.5)

# Bar chart for carbon sequestration
bars = ax2.barh(regions, carbon_sequestration, color='dodgerblue', edgecolor='black')

# Customize carbon sequestration chart
ax2.set_xlabel('Carbon Sequestration (Million Metric Tons)', fontsize=12)
ax2.set_title('Carbon Sequestration by Region', fontsize=14, fontweight='bold', pad=20)

# Add annotations for the carbon sequestration chart
for bar in bars:
    width = bar.get_width()
    ax2.annotate(f'{width}', 
                 xy=(width, bar.get_y() + bar.get_height()/2), 
                 xytext=(3, 0), 
                 textcoords='offset points', 
                 ha='left', va='center', fontsize=10)

# Adjust layout for better readability
plt.tight_layout()

# Show the plot
plt.show()