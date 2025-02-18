import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()

nodes = {
    'A': 'Arithmetic',
    'G': 'Shapes & Spaces',
    'Al': 'Equations',
    'C': 'Differential Study',
    'S': 'Grouping Theory',
    'P': 'Chance Analysis',
    'T': 'Abstract Spaces',
    'CS': 'Digital Science'
}

G.add_nodes_from(nodes.keys())

edges = [
    ('A', 'Al'),
    ('G', 'Al'),
    ('Al', 'C'),
    ('C', 'P'),
    ('P', 'CS'),
    ('Al', 'S'),
    ('S', 'T'),
    ('T', 'CS')
]

G.add_edges_from(edges)

pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(12, 10))

# Shuffle the node colors manually
node_colors = ['lightcoral', 'lightseagreen', 'lightskyblue', 'lightpink', 
               'lightsteelblue', 'lightgoldenrodyellow', 'lightgreen', 'lightsalmon']

nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=3000, edgecolors='k')
nx.draw_networkx_labels(G, pos, labels=nodes, font_size=12, font_weight='bold')
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='gray', arrows=True, arrowsize=20, arrowstyle='-|>')

plt.title('Interconnected Influences in Mathematics\nHistorical Evolution of Mathematical Concepts', fontsize=16, fontweight='bold')
plt.axis('off')

plt.tight_layout()
plt.show()