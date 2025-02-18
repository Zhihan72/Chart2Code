import numpy as np
import matplotlib.pyplot as plt

islands = ['Avalon', 'Eldoria', 'Lumina', 'Noxterra', 'Vespera', 'Mystara']
elements = ['Mana', 'Ether', 'Elixir', 'Aura', 'Stardust']

percentage_data = np.array([
    [30, 25, 20, 25, 10],  # Avalon
    [20, 30, 35, 15, 0],   # Eldoria
    [25, 25, 30, 20, 0],   # Lumina
    [15, 35, 25, 25, 0],   # Noxterra
    [35, 15, 20, 30, 0],   # Vespera
    [10, 20, 20, 40, 10]   # Mystara
])

total_abundance = percentage_data.sum(axis=1)

sorted_indices = np.argsort(total_abundance)
sorted_islands = [islands[i] for i in sorted_indices]
sorted_data = percentage_data[sorted_indices]

fig, ax = plt.subplots(figsize=(10, 6))

# Use a single color across all data groups
single_color = '#3498db'  # A shade of blue

bottom = np.zeros(len(islands))
for i in range(len(elements)):
    ax.bar(sorted_islands, sorted_data[:, i], bottom=bottom, color=single_color, alpha=0.7)
    bottom += sorted_data[:, i]

ax.set_xlabel('Islands')
ax.set_ylabel('Total Abundance (%)')
ax.set_title('Sorted Magical Element Distribution Across Islands', fontsize=14, fontweight='bold')

ax.set_xticks(np.arange(len(islands)))
ax.set_xticklabels(sorted_islands, rotation=45, ha='right')

plt.tight_layout()
plt.show()