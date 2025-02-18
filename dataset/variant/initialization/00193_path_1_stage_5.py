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
    ("Mathematics", "Computer Science", 8),
    ("Chemistry", "Physics", 9),
    ("Physics", "Mathematics", 6),
    ("Biology", "Philosophy", 5),
    ("Philosophy", "Psychology", 7),
    ("Psychology", "Chemistry", 4),
    ("Economics", "Biology", 3),
    ("Computer Science", "Economics", 2),
    ("Biology", "Physics", 4),
    ("Physics", "Computer Science", 6),
    ("Psychology", "Biology", 3)
]

G.add_weighted_edges_from(edges_with_weights)

pos = nx.circular_layout(G)

node_sizes = [600 * G.degree(n) for n in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='royalblue', alpha=0.9)

edge_weights = [d['weight'] for u, v, d in G.edges(data=True)]
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=[w/2 for w in edge_weights], alpha=0.7, edge_color='royalblue')

plt.axis('off')

plt.show()