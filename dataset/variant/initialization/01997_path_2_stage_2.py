import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

# Add nodes representing team members
members = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Helen', 'Ian', 'Julia']
G.add_nodes_from(members)

# Add edges
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

# Customize node sizes and colors
node_sizes = [800 + 200 * G.degree(node) for node in G.nodes()]
node_colors = ['#4A90E2' if G.degree(node) > 2 else '#50E3C2' for node in G.nodes()]

plt.figure(figsize=(14, 12))

# Draw nodes with customized size and color
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, edgecolors='black', linewidths=1.5)

# Draw edges
nx.draw_networkx_edges(G, pos, edgelist=modified_edges, edge_color='gray', style='solid')

# Add labels
nx.draw_networkx_labels(G, pos, font_size=12, font_color='black')

plt.title("Social Connections in a Remote Working Environment", fontsize=16, fontweight='bold')
plt.axis('off')

plt.show()