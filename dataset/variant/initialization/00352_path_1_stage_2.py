import numpy as np
import matplotlib.pyplot as plt

# Updated island names and magical elements
islands = ['Avalon', 'Eldoria', 'Lumina', 'Noxterra', 'Vespera', 'Mystara']
elements = ['Mana', 'Ether', 'Elixir', 'Aura', 'Stardust']

# Updated percentage data
percentage_data = np.array([
    [30, 25, 20, 25, 10],  # Avalon
    [20, 30, 35, 15, 0],   # Eldoria
    [25, 25, 30, 20, 0],   # Lumina
    [15, 35, 25, 25, 0],   # Noxterra
    [35, 15, 20, 30, 0],   # Vespera
    [10, 20, 20, 40, 10]   # Mystara
])

# Calculate total abundance for each island
total_abundance = percentage_data.sum(axis=1)

# Sort data by total abundance
sorted_indices = np.argsort(total_abundance)
sorted_islands = [islands[i] for i in sorted_indices]
sorted_data = percentage_data[sorted_indices]

# Setup the figure
fig, ax = plt.subplots(figsize=(10, 6))

# Generate colors for each element
colors = plt.cm.tab20(np.arange(len(elements)))

# Plot sorted bar chart
bottom = np.zeros(len(islands))
for i, color in enumerate(colors):
    ax.bar(sorted_islands, sorted_data[:, i], bottom=bottom, color=color, alpha=0.7, label=elements[i])
    bottom += sorted_data[:, i]

# Add labels and title
ax.set_xlabel('Islands')
ax.set_ylabel('Total Abundance (%)')
ax.set_title('Sorted Magical Element Distribution Across Islands', fontsize=14, fontweight='bold')

# Customize xticks for better visualization
ax.set_xticks(np.arange(len(islands)))
ax.set_xticklabels(sorted_islands, rotation=45, ha='right')

# Exhibit the legend
ax.legend(title="Elements", loc='upper left', bbox_to_anchor=(1, 1))

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()