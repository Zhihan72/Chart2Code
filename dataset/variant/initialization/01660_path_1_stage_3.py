import matplotlib.pyplot as plt
import networkx as nx

# Create an undirected graph
G = nx.Graph()

nodes = [
    "Rain", "Solar", "Compost", "Crops", 
    "Irrigation", "Biogas", "Livestock", "Market",
    "Greenhouse", "Wind", "Fertilizer"
]

# Add nodes to the graph
G.add_nodes_from(nodes)

edges = [
    ("Rain", "Irrigation"),
    ("Solar", "Biogas"),
    ("Solar", "Crops"),
    ("Compost", "Crops"),
    ("Compost", "Biogas"),
    ("Crops", "Market"),
    ("Irrigation", "Crops"),
    ("Biogas", "Crops"),
    ("Livestock", "Biogas"),
    ("Livestock", "Compost"),
    ("Crops", "Livestock"),
    ("Greenhouse", "Crops"),
    ("Wind", "Greenhouse"),
    ("Wind", "Fertilizer"),
    ("Fertilizer", "Crops"),
    ("Greenhouse", "Market")
]

# Add edges to the graph
G.add_edges_from(edges)

# Define node positions for better visualization
pos = {
    "Rain": (0, 3),
    "Solar": (2, 3),
    "Compost": (1, 1.5),
    "Crops": (3, 2),
    "Irrigation": (1, 4),
    "Biogas": (2, 0.5),
    "Livestock": (0, 0),
    "Market": (4, 2),
    "Greenhouse": (3, 0),
    "Wind": (1, 0),
    "Fertilizer": (3, 3.5)
}

# Draw the graph
plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='lightgreen', edgecolors='black')
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='gray')

# Shortened labels
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
edge_labels = {
    ("Rain", "Irrigation"): "Water",
    ("Solar", "Biogas"): "Energy",
    ("Solar", "Crops"): "Energy",
    ("Compost", "Crops"): "Nutr",
    ("Compost", "Biogas"): "Nutr",
    ("Crops", "Market"): "Crops",
    ("Irrigation", "Crops"): "Water",
    ("Biogas", "Crops"): "Energy",
    ("Livestock", "Biogas"): "Waste",
    ("Livestock", "Compost"): "Manure",
    ("Crops", "Livestock"): "Feed",
    ("Greenhouse", "Crops"): "Crops",
    ("Wind", "Greenhouse"): "Energy",
    ("Wind", "Fertilizer"): "Energy",
    ("Fertilizer", "Crops"): "Fert",
    ("Greenhouse", "Market"): "Prod"
}

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

plt.title('Sustainable Flow in Green Farm', fontsize=16, fontweight='bold')

plt.tight_layout()
plt.axis('off')
plt.show()