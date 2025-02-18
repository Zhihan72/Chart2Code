import matplotlib.pyplot as plt
import networkx as nx

intersections = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

traffic_routes = [
    ('A', 'B', 50),
    ('A', 'C', 30),
    ('B', 'D', 20),
    ('C', 'D', 25),
    ('D', 'F', 60),
    ('E', 'F', 30),
    ('F', 'G', 10)
]

G = nx.Graph()
G.add_nodes_from(intersections)

for route in traffic_routes:
    G.add_edge(route[0], route[1], weight=route[2])

edge_widths = [G[u][v]['weight'] / 10 for u, v in G.edges()]

pos = {
    'A': (0, 3), 'B': (2, 3), 'C': (0, 1),
    'D': (2, 1), 'E': (4, 3), 'F': (4, 1),
    'G': (6, 2)
}

plt.figure(figsize=(12, 8))

# Altered node colors and sizes
node_colors = ['orange', 'pink', 'cyan', 'limegreen', 'violet', 'lightblue', 'khaki']
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=2000, edgecolors='k')

# Altered edge color and style
nx.draw_networkx_edges(G, pos, edge_color='purple', width=edge_widths, style='dashed')
nx.draw_networkx_labels(G, pos, font_size=14, font_weight='bold')

# Altered edge label color
edge_labels = {(u, v): f"{G[u][v]['weight']} cars/h" for u, v in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12, font_color='blue')

plt.title('Traffic Flow at Intersections', fontsize=16, weight='bold')

# Added grid and border alterations
plt.grid(True, linestyle='--', color='gray', alpha=0.5)
plt.gca().spines['top'].set_color('none')
plt.gca().spines['right'].set_color('none')

plt.axis('on')
plt.tight_layout()

plt.show()