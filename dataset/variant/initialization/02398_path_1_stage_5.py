import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

features = [
    "Playground", "Picnic Area", "Fountain", "Walking Path", 
    "Dog Park", "Garden", "Amphitheater", "Restrooms", "Food Stall",
    "Lake", "Sports Field"
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
    ("Dog Park", "Playground"),
    ("Fountain", "Lake"),
    ("Lake", "Sports Field"),
    ("Sports Field", "Playground")
]

G = nx.DiGraph()
G.add_nodes_from(features)
G.add_edges_from(connections)

pos = nx.spring_layout(G, seed=42)
node_color = '#1e90ff'  # Using a single color for all nodes
node_sizes = [1000, 1150, 750, 920, 1020, 1000, 1100, 850, 950, 1300, 1400]

visitor_interactions = np.array([
    [80, 85, 90, 85, 95, 80, 70],
    [50, 60, 70, 60, 80, 90, 100],
    [60, 65, 70, 75, 80, 85, 90],
    [90, 85, 80, 85, 90, 100, 105],
    [70, 75, 80, 85, 80, 75, 70],
    [25, 30, 35, 40, 30, 25, 20],
    [100, 105, 110, 115, 120, 125, 130],
    [40, 45, 50, 45, 40, 35, 30],
    [30, 35, 40, 45, 50, 55, 60],
    [110, 115, 120, 125, 130, 135, 140],
    [65, 70, 75, 80, 85, 90, 95]
])

fig, axes = plt.subplots(1, 2, figsize=(18, 10))

nx.draw(G, pos, with_labels=True, node_color=node_color, node_size=node_sizes,
        edge_color='blue', width=2, alpha=0.6, ax=axes[0], arrows=False,
        style='dashed', font_weight='bold', font_size=12)

axes[0].grid(True, linestyle=':', linewidth=0.5, color='orange')

axes[1].imshow(visitor_interactions, cmap='BuPu', aspect='auto')

fig.colorbar(axes[1].images[0], ax=axes[1], orientation='vertical')
axes[1].set_xticks([i for i in range(len(visitor_interactions[0]))])
axes[1].set_xticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], rotation=45)
axes[1].set_yticks(range(len(features)))
axes[1].set_yticklabels(features)

plt.tight_layout()
for ax in axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

plt.show()