import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()

# Simplified node names
nodes = ["Earth", "MCA", "MCB", "MCG", "MCD"]
G.add_nodes_from(nodes)

edges = [
    ("Earth", "MCA", "Tech"),
    ("Earth", "MCB", "Water"),
    ("Earth", "MCG", "Food"),
    ("MCA", "MCB", "Water"),
    ("MCB", "MCD", "Data"),
    ("MCD", "MCG", "Tech"),
    ("MCG", "MCA", "Food")
]

for source, target, resource in edges:
    G.add_edge(source, target, resource=resource)

pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(10, 8))
nx.draw_networkx_nodes(G, pos, node_size=3500, node_color='lightcoral', edgecolors='black')

nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

nx.draw_networkx_edges(G, pos, edgelist=G.edges(), arrowstyle='-|>', arrowsize=20, edge_color='gray', connectionstyle='arc3,rad=0.2')

edge_labels = nx.get_edge_attributes(G, 'resource')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, font_color='lightcoral')

# Simplified title
plt.title("Mars Supply Chain", fontsize=14, fontweight='bold')

plt.axis('off')
plt.tight_layout()
plt.show()