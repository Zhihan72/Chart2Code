import matplotlib.pyplot as plt
import networkx as nx

intersections = [
    'A', 'B', 'C', 'D', 'F'
]

traffic_routes = [
    ('A', 'B', 50),
    ('A', 'C', 30),
    ('B', 'D', 20),
    ('C', 'D', 25),
    ('D', 'F', 60)
]

G = nx.DiGraph()
G.add_nodes_from(intersections)

for route in traffic_routes:
    G.add_edge(route[0], route[1], weight=route[2])

edge_widths = [G[u][v]['weight'] / 10 for u, v in G.edges()]

pos = {
    'A': (0, 3),
    'B': (2, 3),
    'C': (0, 1),
    'D': (2, 1),
    'F': (4, 1)
}

plt.figure(figsize=(12, 8))

nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=3000, edgecolors='green')
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=25, edge_color='black', width=edge_widths, style='dashed')

plt.axis('off')
plt.tight_layout()
plt.show()