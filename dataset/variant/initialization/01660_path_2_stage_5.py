import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

nodes = [
    "Rainwater", "Solar Energy", "Compost", "Crop Fields", 
    "Irrigation System", "Biogas Plant", "Market"
]

G.add_nodes_from(nodes)

edges = [
    ("Rainwater", "Irrigation System"),
    ("Solar Energy", "Biogas Plant"),
    ("Solar Energy", "Crop Fields"),
    ("Compost", "Crop Fields"),
    ("Compost", "Biogas Plant"),
    ("Crop Fields", "Market"),
    ("Irrigation System", "Crop Fields"),
    ("Biogas Plant", "Crop Fields")
]

G.add_edges_from(edges)

pos = {
    "Rainwater": (0, 3),
    "Solar Energy": (2, 3),
    "Compost": (1, 1.5),
    "Crop Fields": (3, 2),
    "Irrigation System": (1, 4),
    "Biogas Plant": (2, 0.5),
    "Market": (4, 2),
}

plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, node_size=3500, node_color='lightgreen', edgecolors='darkgray', node_shape='s')
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='slateblue', style='dashed', width=2)

# Removed label and title code
plt.grid(linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()