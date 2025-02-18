import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

nodes = {
    'A': 'Arithmetic',
    'G': 'Digital Science',
    'Al': 'Equations',
    'C': 'Chance Analysis',
    'S': 'Grouping Theory',
    'P': 'Shapes & Spaces',
    'T': 'Differential Study',
    'CS': 'Abstract Spaces'
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

pos = nx.spring_layout(G, seed=24)

plt.figure(figsize=(12, 10))

node_colors = ['skyblue', 'seagreen', 'darkorange', 'salmon', 
               'purple', 'gold', 'lime', 'navy']

nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=2800, edgecolors='lightgray')
nx.draw_networkx_labels(G, pos, labels=nodes, font_size=11, font_weight='medium', font_color='darkblue')
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='black', style='dashed')

plt.title('Interconnected Influences in Mathematics\nHistorical Evolution of Mathematical Concepts', fontsize=15, fontweight='regular')
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(['Node', 'Edge'], loc='lower left', fontsize=10, frameon=True)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.axis('on')

plt.tight_layout()
plt.show()