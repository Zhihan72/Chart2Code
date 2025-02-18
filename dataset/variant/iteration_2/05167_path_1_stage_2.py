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

# Create a figure with subplots for each region
fig, ax = plt.subplots(figsize=(10, 10), nrows=2, ncols=3)
ax = ax.flatten()

# Plot each region's element distribution as a donut chart
for idx, region in enumerate(regions):
    wedges, texts, autotexts = ax[idx].pie(
        element_distributions[idx],
        labels=elements_found,
        autopct='%1.1f%%',
        startangle=90,
        colors=[plt.cm.viridis(i / len(elements_found)) for i in range(len(elements_found))],
        wedgeprops=dict(width=0.3)
    )
    ax[idx].set_title(region)

# Remove axis for any unused subplot
for a in ax[len(regions):]:
    a.remove()

# Set the title for the entire figure
fig.suptitle("Element Distribution by Region (Donut Chart)", fontsize=16, weight='bold')

# Adjust layout
plt.tight_layout(pad=3.0)

# Show plot
plt.show()