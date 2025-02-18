import matplotlib.pyplot as plt
import networkx as nx

nodes = {
    'Solar Power': 5,
    'Turbine Winds': 4,
    'Water Power': 3,
    'Earth Heat': 2,
    'Biofuel': 4,
    'Storage': 6,
    'Distribution': 7,
    'Smart Lines': 5
}

edges = {
    ('Solar Power', 'Storage'): 5,
    ('Turbine Winds', 'Storage'): 4,
    ('Water Power', 'Distribution'): 6,
    ('Earth Heat', 'Distribution'): 4,
    ('Biofuel', 'Storage'): 3,
    ('Storage', 'Smart Lines'): 4,
    ('Smart Lines', 'Distribution'): 5,
    ('Solar Power', 'Distribution'): 2,
    ('Turbine Winds', 'Distribution'): 3,
    ('Biofuel', 'Distribution'): 2
}

G = nx.DiGraph()
G.add_nodes_from(nodes.keys())
for (start, end), weight in edges.items():
    G.add_edge(start, end, weight=weight)

pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(14, 10))

node_sizes = [nodes[node] * 500 for node in G.nodes]
node_colors = [plt.cm.plasma(nodes[node] / max(nodes.values())) for node in G.nodes]

nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, edgecolors='black', alpha=0.9)
nx.draw_networkx_edges(G, pos, edgelist=edges.keys(), arrowstyle='-|>', arrowsize=15,
                       width=[w for w in edges.values()], edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', verticalalignment='center')
nx.draw_networkx_edge_labels(G, pos, edge_labels={edge: f"{weight}" for edge, weight in edges.items()}, font_size=8)

plt.title('Renewable Energy Networks', fontsize=14, fontweight='bold', loc='center')
plt.axis('off')
plt.tight_layout()
plt.show()