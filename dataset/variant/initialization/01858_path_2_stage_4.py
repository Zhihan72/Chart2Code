import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()

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
# Changed node color and added a different edge color
nx.draw_networkx_nodes(G, pos, node_size=3500, node_color='skyblue', edgecolors='black')

# Altered font size and removed font weight
nx.draw_networkx_labels(G, pos, font_size=12)

# Changed arrowstyle, color and connection style
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), arrowstyle='->', arrowsize=15, edge_color='navy', connectionstyle='arc3,rad=0.1', style='--')

edge_labels = nx.get_edge_attributes(G, 'resource')
# Altered font color to match nodes
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_color='skyblue')

# Stylistic changes for title
plt.title("Mars Supply Chain", fontsize=16, fontweight='light', color='slategray')

# Added grid and frame
plt.grid(True)
plt.gca().set_frame_on(True)

plt.axis('off')
plt.tight_layout()
plt.show()