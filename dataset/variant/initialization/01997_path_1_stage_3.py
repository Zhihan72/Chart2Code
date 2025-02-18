import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

members = [
    'Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Helen', 
    'Ian', 'Julia', 'Kevin', 'Lisa', 'Mona', 'Nick', 'Oliver'
]
G.add_nodes_from(members)

edges = [
    ('Alice', 'Bob'), ('Alice', 'Charlie'), ('Alice', 'Eva'),
    ('Bob', 'Charlie'), ('Bob', 'Grace'), ('Charlie', 'Frank'),
    ('David', 'Eva'), ('David', 'Ian'), ('Eva', 'Julia'),
    ('Frank', 'Grace'), ('Grace', 'Helen'), ('Helen', 'Ian'),
    ('Kevin', 'Mona'), ('Mona', 'Bob'), ('Lisa', 'Oliver'),
    ('Nick', 'Alice'), ('Nick', 'David'), ('Oliver', 'Helen')
]
G.add_edges_from(edges)

pos = nx.spring_layout(G, seed=42)

node_sizes = [800 + 200 * G.degree(node) for node in G.nodes()]
node_colors = ['#4A90E2' if G.degree(node) > 2 else '#50E3C2' for node in G.nodes()]

plt.figure(figsize=(14, 12))

nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, edgecolors='black', linewidths=1.5)

edge_widths = [2.5 if 'Alice' in edge else 1.5 for edge in edges]
nx.draw_networkx_edges(G, pos, edgelist=edges, width=edge_widths, edge_color='gray', style='solid')

nx.draw_networkx_labels(G, pos, font_size=12, font_color='black', font_family='sans-serif')

plt.title("InnoTech Team Communication (Undirected Graph)", fontsize=16, fontweight='bold')

plt.tight_layout()

plt.show()