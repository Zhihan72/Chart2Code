import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

nodes = {
    'A': 'Computation',
    'G': 'Measure',
    'Al': 'Equation',
    'C': 'Derivatives',
    'P': 'Chance',
    'T': 'Shape',
    'CS': 'Coding'
}

G.add_nodes_from(nodes.keys())

edges = [
    ('A', 'Al'),
    ('G', 'Al'),
    ('Al', 'C'),
    ('C', 'P'),
    ('P', 'CS'),
    ('T', 'CS')
]

G.add_edges_from(edges)

pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(12, 10))

nx.draw_networkx_nodes(G, pos, node_color='orange', node_size=3000, edgecolors='k')
nx.draw_networkx_labels(G, pos, labels=nodes, font_size=12, font_weight='bold')
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='purple')

plt.title('The Unexpected Journey of Numbers\nWeb of Mathematical Thought', fontsize=16, fontweight='bold')
plt.axis('off')
plt.tight_layout()
plt.show()