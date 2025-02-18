import matplotlib.pyplot as plt
import networkx as nx

# Change graph type from directed (DiGraph) to undirected (Graph)
G = nx.Graph()

nodes = ["Earth", "MCA", "MCB", "MCG", "MCD"]
G.add_nodes_from(nodes)

# Maintain original connections but change them to undirected edges
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

# Node and label appearance settings remain unchanged
nx.draw_networkx_nodes(G, pos, node_size=3500, node_color='skyblue', edgecolors='black')
nx.draw_networkx_labels(G, pos, font_size=12)

# Draw undirected edges: remove arrowstyle and other directed-related attributes
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='navy', style='--')

edge_labels = nx.get_edge_attributes(G, 'resource')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_color='skyblue')

plt.title("Mars Supply Chain", fontsize=16, fontweight='light', color='slategray')
plt.grid(True)
plt.gca().set_frame_on(True)

# Remove axis
plt.axis('off')
plt.tight_layout()
plt.show()