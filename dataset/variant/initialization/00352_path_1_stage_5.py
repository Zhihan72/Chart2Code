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

colors = ['#2ecc71', '#e74c3c', '#9b59b6', '#f1c40f', '#34495e']
hatches = ['/', '\\', '|', '-', '+']

bottom = np.zeros(len(islands))
for i in range(len(elements)):
    ax.bar(
        sorted_islands, sorted_data[:, i], bottom=bottom, 
        color=colors[i], hatch=hatches[i], alpha=0.7
    )
    bottom += sorted_data[:, i]

ax.grid(True, linestyle='--', linewidth=0.5)
ax.spines['top'].set_color('red')
ax.spines['right'].set_color('red')

plt.tight_layout()
plt.show()