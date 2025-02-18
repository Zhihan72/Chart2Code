import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()

# Add nodes for Earth and Mars colonies
nodes = ["Earth", "Mars Colony Alpha", "Mars Colony Beta", "Mars Colony Gamma", "Mars Colony Delta"]
G.add_nodes_from(nodes)

edges = [
    ("Earth", "Mars Colony Alpha", "Water"),
    ("Earth", "Mars Colony Beta", "Food"),
    ("Earth", "Mars Colony Gamma", "Tech"),
    ("Mars Colony Alpha", "Mars Colony Beta", "Data"),
    ("Mars Colony Beta", "Mars Colony Delta", "Tech"),
    ("Mars Colony Delta", "Mars Colony Gamma", "Water"),
    ("Mars Colony Gamma", "Mars Colony Alpha", "Food")
]

for source, target, resource in edges:
    G.add_edge(source, target, resource=resource)

pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(10, 8))
nx.draw_networkx_nodes(G, pos, node_size=3500, node_color='lightcoral', edgecolors='black')

nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

nx.draw_networkx_edges(G, pos, edgelist=G.edges(), arrowstyle='-|>', arrowsize=20, edge_color='lightcoral', connectionstyle='arc3,rad=0.2')

edge_labels = nx.get_edge_attributes(G, 'resource')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, font_color='darkgreen')

# Remove axes
plt.axis('off')

plt.tight_layout()

plt.show()