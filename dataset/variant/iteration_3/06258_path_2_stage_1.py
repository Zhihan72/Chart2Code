import matplotlib.pyplot as plt
import numpy as np

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

# Calculate average distribution to determine divergence
avg_distribution = np.mean(np.array(species_distribution), axis=0)

# Diverging bar chart for species distribution
sequence_ids = np.arange(len(regions))

# Initialize bottom values
bottom_vals = np.zeros(len(regions))

# Plotting each species
for i, specie in enumerate(species):
    # Calculate the deviation for each region
    currentSpeciesDistribution = np.array([dist[i] - avg_distribution[i] for dist in species_distribution])
    
    # Create a diverging bar chart with bottom_vals for previous species
    ax1.bar(sequence_ids, currentSpeciesDistribution, 0.5, label=specie, color=colors[i], bottom=bottom_vals)
    
    # Update bottom_vals for the next species
    bottom_vals += currentSpeciesDistribution

# Customize diverging bar chart    
ax1.set_xlabel('Regions', fontsize=12)
ax1.set_ylabel('Deviation from Average (%)', fontsize=12)
ax1.set_title('Diverging Plant Species Distribution', fontsize=14, fontweight='bold', pad=20)
ax1.set_xticks(sequence_ids)
ax1.set_xticklabels(regions)
ax1.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax1.legend(title='Species', loc='upper right')
ax1.grid(True, linestyle='--', alpha=0.5)

# Bar chart for carbon sequestration (unchanged)
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

# Adjust layout for visualization
plt.tight_layout()
plt.show()