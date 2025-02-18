import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

members = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Helen', 'Ian', 'Julia']
G.add_nodes_from(members)

modified_edges = [
    ('Alice', 'Eva'), ('Alice', 'Bob'), ('Alice', 'Charlie'),
    ('Bob', 'Grace'), ('Bob', 'Charlie'),
    ('Charlie', 'Frank'),
    ('David', 'Ian'), ('David', 'Eva'),
    ('Eva', 'Julia'),
    ('Grace', 'Frank'),
    ('Grace', 'Helen'),
    ('Ian', 'Helen')
]
G.add_edges_from(modified_edges)

pos = nx.spring_layout(G, seed=42)

node_sizes = [800 + 200 * G.degree(node) for node in G.nodes()]
node_colors = ['#FF5733' if G.degree(node) > 2 else '#33FF57' for node in G.nodes()]

plt.figure(figsize=(14, 12))

nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, edgecolors='black', linewidths=1.5)
nx.draw_networkx_edges(G, pos, edgelist=modified_edges, edge_color='gray', style='solid')

plt.axis('off')

plt.show()