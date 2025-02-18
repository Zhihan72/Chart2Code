import matplotlib.pyplot as plt
import numpy as np

# Data
regions = ['Nile', 'Gobi Desert', 'Arctic', 'Savannah', 'Andes', 'Rockies']
species = ['Bush', 'Herb', 'Vine', 'Epiphyte', 'Lichen']
species_distribution = [
    [50, 5, 10, 30, 5],   
    [2, 15, 70, 5, 8],     
    [60, 10, 15, 5, 10],   
    [35, 5, 50, 8, 2],     
    [10, 20, 5, 60, 5],    
    [25, 10, 5, 50, 10]    
]

carbon_sequestration = [300, 20, 150, 100, 200, 120]

colors = ['#E63946', '#F1FAEE', '#A8DADC', '#457B9D', '#1D3557']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
bar_width = 0.1
sequence_ids = np.arange(len(regions))

# Stacked bar chart for species distribution
for i, specie in enumerate(species):
    currentSpeciesDistribution = [dist[i] for dist in species_distribution]
    bottom_vals = np.sum([list(species_distribution[j][:i]) for j in range(len(regions))], axis=1) if i > 0 else None
    ax1.bar(sequence_ids + i * bar_width, currentSpeciesDistribution, bar_width, color=colors[i], bottom=bottom_vals)

ax1.set_xlabel('Territories', fontsize=12)
ax1.set_ylabel('Biodiversity Percentage (%)', fontsize=12)
ax1.set_title('Diversity Patterns in Different Territories', fontsize=14, fontweight='bold', pad=20)
ax1.set_xticks(sequence_ids + bar_width * 2.5)
ax1.set_xticklabels(regions)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['bottom'].set_visible(False)

# Bar chart for carbon sequestration
bars = ax2.barh(regions, carbon_sequestration, color='orange', edgecolor='black')

ax2.set_xlabel('CO2 Capture (M Metric Tons)', fontsize=12)
ax2.set_title('CO2 Capture Efficiency by Zone', fontsize=14, fontweight='bold', pad=20)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['bottom'].set_visible(False)

for bar in bars:
    width = bar.get_width()
    ax2.annotate(f'{width}', 
                 xy=(width, bar.get_y() + bar.get_height()/2), 
                 xytext=(3, 0), 
                 textcoords='offset points', 
                 ha='left', va='center', fontsize=10)

plt.tight_layout()
plt.show()