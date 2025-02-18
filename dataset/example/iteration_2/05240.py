import matplotlib.pyplot as plt
import numpy as np

# Backstory: An analysis of wildlife population recovery in various regions over a decade after implementing conservation programs.
regions = ['North America', 'Africa', 'Asia', 'Europe', 'South America']
species = ['Elephants', 'Tigers', 'Pandas', 'Bears', 'Condors']

# Population recovery data (in thousands)
north_america = [1.2, 0, 0, 1.8, 0.5]
africa = [10, 0.7, 0, 0.2, 0]
asia = [0, 1.5, 1.2, 0, 0]
europe = [0, 0, 0, 0.4, 0]
south_america = [0, 0, 0, 0, 1.5]

# Compile data
data = [north_america, africa, asia, europe, south_america]
data_transposed = np.array(data).T

# Colors for each species
colors = ['#c94c4c', '#4c8ec9', '#52c94c', '#c9b34c', '#8e44ad']

# Setup subplots
fig, ax = plt.subplots(figsize=(12, 8))

# Plot stacked bar chart
bottom_values = np.zeros(len(regions))
for idx, (species_data, color) in enumerate(zip(data_transposed, colors)):
    ax.bar(regions, species_data, label=species[idx], color=color, bottom=bottom_values, edgecolor='black')
    bottom_values += species_data

# Add value labels to the bars
for region_idx, region_data in enumerate(data):
    bottom = 0
    for species_idx, value in enumerate(region_data):
        if value > 0:
            ax.text(region_idx, bottom + value / 2, f'{value}', ha='center', va='center', color='white', fontsize=9, fontweight='bold')
        bottom += value

# Chart configurations
ax.set_title('Wildlife Population Recovery From Conservation Programs (2010-2020)', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Regions', fontsize=12, labelpad=15)
ax.set_ylabel('Population Recovered (Thousands)', fontsize=12, labelpad=15)
ax.legend(title='Species', loc='upper left', bbox_to_anchor=(1.05, 1))
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()