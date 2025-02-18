import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

features = [
    "Playground", "Picnic Area", "Fountain", "Walking Path", 
    "Dog Park", "Garden", "Amphitheater", "Restrooms", "Food Stall"
]

connections = [
    ("Playground", "Picnic Area"),
    ("Picnic Area", "Garden"),
    ("Garden", "Fountain"),
    ("Fountain", "Walking Path"),
    ("Walking Path", "Amphitheater"),
    ("Amphitheater", "Restrooms"),
    ("Restrooms", "Food Stall"),
    ("Food Stall", "Dog Park"),
    ("Dog Park", "Playground")
]

G = nx.Graph()
G.add_nodes_from(features)
G.add_edges_from(connections)

pos = nx.spring_layout(G, seed=42)
node_colors = ['#9acd32', '#ff6347', '#1e90ff', '#ffeb3b', '#f4a460', '#adff2f', '#dda0dd', '#8b4513', '#ff69b4']
node_sizes = [1200, 1000, 800, 1100, 900, 950, 1050, 850, 800]

visitor_interactions = np.array([
    [50, 60, 70, 60, 80, 90, 100],
    [80, 85, 90, 85, 95, 80, 70],
    [30, 35, 40, 45, 50, 55, 60],
    [90, 85, 80, 85, 90, 100, 105],
    [25, 30, 35, 40, 30, 25, 20],
    [60, 65, 70, 75, 80, 85, 90],
    [100, 105, 110, 115, 120, 125, 130],
    [40, 45, 50, 45, 40, 35, 30],
    [70, 75, 80, 85, 80, 75, 70]
])

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

fig, axes = plt.subplots(1, 2, figsize=(18, 10))

nx.draw(G, pos, with_labels=False, node_color=node_colors, node_size=node_sizes,
        edge_color='gray', width=2.0, alpha=0.7, ax=axes[0])

axes[1].imshow(visitor_interactions, cmap='YlGnBu', aspect='auto')

fig.colorbar(axes[1].images[0], ax=axes[1], orientation='vertical')

for ax in axes:
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()