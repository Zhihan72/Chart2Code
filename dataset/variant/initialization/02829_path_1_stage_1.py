import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()

nodes = {
    'A': 'Arithmetic',          # Original: Arithmetic
    'G': 'Shapes & Spaces',     # Original: Geometry
    'Al': 'Equations',          # Original: Algebra
    'C': 'Differential Study',  # Original: Calculus
    'S': 'Grouping Theory',     # Original: Set Theory
    'P': 'Chance Analysis',     # Original: Probability
    'T': 'Abstract Spaces',     # Original: Topology
    'CS': 'Digital Science'     # Original: Computer Science
}

G.add_nodes_from(nodes.keys())

edges = [
    ('A', 'Al'),  # Arithmetic influences Equations
    ('G', 'Al'),  # Shapes & Spaces influences Equations
    ('Al', 'C'),  # Equations influence Differential Study
    ('C', 'P'),   # Differential Study influences Chance Analysis
    ('P', 'CS'),  # Chance Analysis influences Digital Science
    ('Al', 'S'),  # Equations influence Grouping Theory
    ('S', 'T'),   # Grouping Theory influences Abstract Spaces
    ('T', 'CS')   # Abstract Spaces influence Digital Science
]

G.add_edges_from(edges)

pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(12, 10))

nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=3000, edgecolors='k')
nx.draw_networkx_labels(G, pos, labels=nodes, font_size=12, font_weight='bold')
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='gray', arrows=True, arrowsize=20, arrowstyle='-|>')

plt.title('Interconnected Influences in Mathematics\nHistorical Evolution of Mathematical Concepts', fontsize=16, fontweight='bold')
plt.axis('off')

plt.tight_layout()
plt.show()