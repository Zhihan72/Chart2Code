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
nx.draw_networkx_nodes(G, pos, node_size=3500, node_color='lightblue', edgecolors='darkgray', node_shape='s')
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='lightcoral', style='dashed', width=2)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

edge_labels = {
    ("Rainwater", "Irrigation System"): "Water",
    ("Solar Energy", "Biogas Plant"): "Energy",
    ("Solar Energy", "Crop Fields"): "Energy",
    ("Compost", "Crop Fields"): "Nutrients",
    ("Compost", "Biogas Plant"): "Nutrients",
    ("Crop Fields", "Market"): "Crops",
    ("Irrigation System", "Crop Fields"): "Water",
    ("Biogas Plant", "Crop Fields"): "Energy"
}

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

plt.title('Sustainable Resource Flow in Green Acres Farm (without Livestock)', fontsize=16, fontweight='bold')
plt.grid(linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()