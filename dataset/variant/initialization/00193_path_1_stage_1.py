import matplotlib.pyplot as plt
import networkx as nx

DG = nx.DiGraph()

# Define academic disciplines as nodes
disciplines = [
    "Computer Science", "Mathematics", "Physics", 
    "Biology", "Chemistry", "Economics", 
    "Psychology", "Philosophy"
]

DG.add_nodes_from(disciplines)

# Define the directed edges with weights indicating influence strength
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

DG.add_weighted_edges_from(edges_with_weights)

pos = nx.circular_layout(DG)

node_sizes = [600 * DG.out_degree(n) for n in DG.nodes()]
nx.draw_networkx_nodes(DG, pos, node_size=node_sizes, node_color='lightgreen', alpha=0.9)

edge_weights = [d['weight'] for u, v, d in DG.edges(data=True)]
nx.draw_networkx_edges(DG, pos, edgelist=DG.edges(), width=[w/2 for w in edge_weights], 
                       alpha=0.7, edge_color='royalblue', arrows=True, arrowsize=20)

nx.draw_networkx_labels(DG, pos, font_size=10, font_weight='bold', verticalalignment='center')

edge_labels = {(u, v): d['weight'] for u, v, d in DG.edges(data=True)}
nx.draw_networkx_edge_labels(DG, pos, edge_labels=edge_labels, font_size=8)

plt.title('Interdisciplinary Knowledge Flow in\nModern Academia', fontsize=14, weight='bold', pad=20)
plt.axis('off')
plt.tight_layout()

plt.show()