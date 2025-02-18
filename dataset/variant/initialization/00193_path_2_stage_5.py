import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

disciplines = [
    "Computer Science", "Mathematics", "Physics", 
    "Biology", "Chemistry", "Economics", 
    "Psychology", "Philosophy"
]

G.add_nodes_from(disciplines)

edges_with_weights = [
    ("Computer Science", "Economics", 8),
    ("Mathematics", "Psychology", 9),
    ("Physics", "Philosophy", 6),
    ("Biology", "Psychology", 5),
    ("Psychology", "Mathematics", 7),
    ("Philosophy", "Chemistry", 4),
    ("Economics", "Biology", 3),
    ("Physics", "Economics", 2),
    ("Chemistry", "Computer Science", 4),
    ("Computer Science", "Biology", 6),
    ("Chemistry", "Physics", 3)
]

G.add_weighted_edges_from(edges_with_weights)

pos = nx.shell_layout(G)

node_sizes = [600 * G.degree(n) for n in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='blue', alpha=0.8, node_shape='s')

nx.draw_networkx_edges(G, pos, edgelist=G.edges(), alpha=0.6, edge_color='blue', style='dashed')

plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.axis('on')
plt.tight_layout()

plt.show()