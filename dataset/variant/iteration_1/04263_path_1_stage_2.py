import matplotlib.pyplot as plt
import networkx as nx

intersections = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

traffic_routes = [
    ('A', 'B', 50),
    ('A', 'C', 30),
    ('B', 'D', 20),
    ('C', 'D', 25),
    ('B', 'E', 40),
    ('D', 'F', 60),
    ('E', 'F', 30),
    ('E', 'G', 20),
    ('F', 'G', 10)
]

G = nx.DiGraph()
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

# Use predefined node colors for consistency
node_colors = ['lightgreen', 'skyblue', 'lightcoral', 'lightyellow', 'lightblue', 'lightpink', 'lightgray']
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=2500, edgecolors='k')

nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, edge_color='black', width=edge_widths)
nx.draw_networkx_labels(G, pos, font_size=14, font_weight='bold')

edge_labels = {(u, v): f"{G[u][v]['weight']} cars/h" for u, v in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12, font_color='red')

plt.title('Traffic Flow at Intersections', fontsize=16, weight='bold')
plt.axis('off')
plt.tight_layout()

plt.show()