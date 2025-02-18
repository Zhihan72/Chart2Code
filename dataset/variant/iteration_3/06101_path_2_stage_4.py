import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

kingdoms = [
    "North", "River", "High", "Wood",
    "Desert", "Coast", "Mid"
]

relationships = [
    ("North", "River", 8),
    ("River", "High", 5),
    ("High", "Wood", -7),
    ("Wood", "Desert", -5),
    ("Desert", "Coast", 7),
    ("Mid", "North", 4),
    ("River", "Coast", 9),
    ("High", "Desert", 5),
    ("North", "High", -8)
]

G = nx.DiGraph()
G.add_nodes_from(kingdoms)
G.add_weighted_edges_from(relationships)

pos = nx.spring_layout(G, seed=42)

fig, ax = plt.subplots(figsize=(14, 10))

nx.draw_networkx_nodes(G, pos, node_size=1600, node_color='lightblue', edgecolors='black', ax=ax)

# Manually shuffle the assigned color positions
edge_colors = ['red', 'green', 'green', 'green', 'red', 'red', 'green', 'green', 'red']
weights = np.abs([weight for u, v, weight in relationships])
nx.draw_networkx_edges(
    G, pos, edgelist=relationships, arrowstyle='-|>', arrowsize=15, 
    edge_color=edge_colors, width=weights, ax=ax, connectionstyle="arc3,rad=0.2"
)

nx.draw_networkx_labels(G, pos, font_size=12, verticalalignment='center', ax=ax)

plt.axis('off')
plt.show()