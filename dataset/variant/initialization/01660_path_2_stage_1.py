import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()

# Define nodes excluding "Livestock"
nodes = [
    "Rainwater", "Solar Energy", "Compost", "Crop Fields", 
    "Irrigation System", "Biogas Plant", "Market"
]

G.add_nodes_from(nodes)

# Define edges excluding those linked with "Livestock"
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

# Define new positions for visualization
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
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='lightgreen', edgecolors='black')
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='gray', arrows=True, arrowsize=20, arrowstyle='-|>')
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
plt.tight_layout()
plt.axis('off')
plt.show()