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

pos = nx.spring_layout(G, seed=24)  # Changed seed for slight variation

plt.figure(figsize=(12, 10))

node_colors = ['skyblue', 'seagreen', 'darkorange', 'salmon', 
               'purple', 'gold', 'lime', 'navy']  # Changed colors

nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=2800, edgecolors='lightgray')  # Changed edge colors
nx.draw_networkx_labels(G, pos, labels=nodes, font_size=11, font_weight='medium', font_color='darkblue')  # Changed font style & color
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='black', arrows=True, arrowsize=15, arrowstyle='->', style='dashed')  # Changed edge style

plt.title('Interconnected Influences in Mathematics\nHistorical Evolution of Mathematical Concepts', fontsize=15, fontweight='regular')
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)  # Added grid
plt.legend(['Node', 'Edge'], loc='lower left', fontsize=10, frameon=True)  # Added legend
plt.gca().spines['top'].set_visible(False)  # Modified borders by hiding top spine
plt.gca().spines['right'].set_visible(False)  # Modified borders by hiding right spine

plt.axis('on')  # Changed axis to on to make grid visible

plt.tight_layout()
plt.show()