import numpy as np
import matplotlib.pyplot as plt

# Backstory:
# "A study on the growth rates of different tree species in various climates over decades."

# Tree species and their growth rates (cm/year) in different climates
tree_species = ['Oak', 'Pine', 'Maple', 'Birch', 'Redwood']

# Constructed fictional growth rates for each tree species in five different climates:
climate_tropical = [120, 140, 115, 130, 145]
climate_temperate = [80, 100, 95, 85, 110]
climate_boreal = [50, 70, 65, 55, 75]
climate_arid = [30, 50, 45, 35, 55]
climate_mediterranean = [70, 90, 85, 75, 95]

# Organizing the data into a list of lists for each climate
data = [
    climate_tropical,     # Tropical
    climate_temperate,    # Temperate
    climate_boreal,       # Boreal
    climate_arid,         # Arid
    climate_mediterranean # Mediterranean
]

# Plotting the box plot
fig, ax = plt.subplots(figsize=(14, 8))

# Create vertical boxplots for each tree species across climates
colors = ['#8CBF26', '#377EB8', '#E41A1C', '#F28E2B', '#59A9C8']
for i, species in enumerate(tree_species):
    species_data = [climate[i] for climate in data]
    bp = ax.boxplot(species_data, positions=[i], widths=0.6, vert=True, patch_artist=True, 
                    boxprops=dict(facecolor=colors[i], color='black'),
                    whiskerprops=dict(color='black', linestyle='--'),
                    capprops=dict(color='black'),
                    flierprops=dict(marker='o', color='red', alpha=0.5),
                    medianprops=dict(color='black'),
                    notch=True)

# Customize x-axis and labels
ax.set_xticks(range(len(tree_species)))
ax.set_xticklabels(tree_species, fontsize=12, fontweight='bold')
ax.set_ylabel("Growth Rate (cm/year)", fontsize=12, fontweight='bold')
ax.set_title("Growth Rates of Different Tree Species in Various Climates", fontsize=16, fontweight='bold', pad=20)
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Adding a legend for climates
legend_labels = ['Tropical', 'Temperate', 'Boreal', 'Arid', 'Mediterranean']
handles = [plt.Line2D([0], [0], color=colors[i], lw=4) for i in range(len(tree_species))]
ax.legend(handles, legend_labels, title='Tree Species', loc='upper right', bbox_to_anchor=(1.25, 1), fontsize=12)

# Adjust layout for better fit and prevent overlap
plt.tight_layout()

# Show the plot
plt.show()