import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# Every year, the Astronomer's Guild of Eldoria releases a report on the composition of stardust collected from different regions of the celestial realm. Each region is known to contribute a unique blend of elements to the stardust, and these compositions are vital for the crafting of star-forged artifacts and potions in Eldoria. This year's report covers five major regions: Solaris, Lunaria, Astoria, Nebula, and Quasaris.

# Data
regions = ['Solaris', 'Lunaria', 'Astoria', 'Nebula', 'Quasaris']
composition_percentages = [22, 18, 30, 15, 15]  # As measured by the guild
elements_found = ['Plasma', 'Ether', 'Luminal Particles', 'Void Fragments', 'Astral Residue']
element_distributions = [
    [30, 20, 10, 25, 15],  # Solaris
    [10, 25, 20, 30, 15],  # Lunaria
    [20, 30, 15, 10, 25],  # Astoria
    [25, 10, 30, 15, 20],  # Nebula
    [15, 25, 20, 15, 25],  # Quasaris
]

# Chart details and plot creation
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Pie chart for regional composition
colors = plt.cm.plasma(np.linspace(0, 1, len(regions)))
wedges, texts, autotexts = ax1.pie(
    composition_percentages, 
    labels=regions, 
    autopct='%1.1f%%', 
    startangle=140,
    colors=colors,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

ax1.set_title(
    "Composition of Stardust Collected from Various Celestial Regions (2023)", 
    fontsize=16, weight='bold', pad=20
)
plt.setp(autotexts, size=12, weight='bold', color='white')

# Create a stacked bar chart for detailed element distribution
bar_width = 0.35
region_indices = np.arange(len(regions))
bottom_values = np.zeros(len(regions))

for i, element in enumerate(elements_found):
    ax2.bar(
        region_indices, 
        [dist[i] for dist in element_distributions], 
        bar_width, 
        bottom=bottom_values, 
        label=element, 
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
ax2.legend(title="Elements")

# Adjust layout
plt.tight_layout(pad=3)

# Show plot
plt.show()