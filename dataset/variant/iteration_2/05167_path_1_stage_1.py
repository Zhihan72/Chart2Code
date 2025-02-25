import matplotlib.pyplot as plt
import numpy as np

# Data
regions = ['Solaris', 'Lunaria', 'Astoria', 'Nebula', 'Quasaris']
elements_found = ['Plasma', 'Ether', 'Luminal Particles', 'Void Fragments', 'Astral Residue']
element_distributions = [
    [30, 20, 10, 25, 15],  # Solaris
    [10, 25, 20, 30, 15],  # Lunaria
    [20, 30, 15, 10, 25],  # Astoria
    [25, 10, 30, 15, 20],  # Nebula
    [15, 25, 20, 15, 25],  # Quasaris
]

# Create a stacked bar chart for detailed element distribution
fig, ax = plt.subplots(figsize=(8, 8))

bar_width = 0.35
region_indices = np.arange(len(regions))
bottom_values = np.zeros(len(regions))

for i, element in enumerate(elements_found):
    ax.bar(
        region_indices, 
        [dist[i] for dist in element_distributions], 
        bar_width, 
        bottom=bottom_values, 
        label=element, 
        color=plt.cm.viridis(i / len(elements_found))
    )
    bottom_values += [dist[i] for dist in element_distributions]

ax.set_title(
    "Detailed Element Distribution in Stardust by Regions", 
    fontsize=16, weight='bold', pad=20
)
ax.set_xlabel('Regions')
ax.set_ylabel('Percentage (%)')
ax.set_xticks(region_indices)
ax.set_xticklabels(regions)
ax.legend(title="Elements")

# Adjust layout
plt.tight_layout(pad=3)

# Show plot
plt.show()