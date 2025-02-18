import matplotlib.pyplot as plt
import numpy as np

# Data
regions = ['Solaris', 'Lunaria', 'Astoria', 'Nebula', 'Quasaris']
composition_percentages = [22, 18, 30, 15, 15]
elements_found = ['Plasma', 'Ether', 'Luminal Particles', 'Void Fragments', 'Astral Residue']
element_distributions = [
    [30, 20, 10, 25, 15], 
    [10, 25, 20, 30, 15], 
    [20, 30, 15, 10, 25], 
    [25, 10, 30, 15, 20], 
    [15, 25, 20, 15, 25], 
]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Pie chart for regional composition without borders
colors = plt.cm.plasma(np.linspace(0, 1, len(regions)))
ax1.pie(
    composition_percentages, 
    labels=regions, 
    autopct='%1.1f%%', 
    startangle=140,
    colors=colors,
    wedgeprops=dict(width=0.3)
)

ax1.set_title(
    "Composition of Stardust Collected from Various Celestial Regions (2023)", 
    fontsize=16, weight='bold', pad=20
)

# Stacked bar chart for detailed element distribution without legend
bar_width = 0.35
region_indices = np.arange(len(regions))
bottom_values = np.zeros(len(regions))

for i, element in enumerate(elements_found):
    ax2.bar(
        region_indices, 
        [dist[i] for dist in element_distributions], 
        bar_width, 
        bottom=bottom_values, 
        color=plt.cm.viridis(i / len(elements_found))
    )
    bottom_values += [dist[i] for dist in element_distributions]

ax2.set_title(
    "Detailed Element Distribution in Stardust by Regions", 
    fontsize=16, weight='bold', pad=20
)
ax2.set_xlabel('Regions')
ax2.set_ylabel('Percentage (%)')
ax2.set_xticks(region_indices)
ax2.set_xticklabels(regions)

# Adjust layout
plt.tight_layout(pad=3)

# Show plot
plt.show()