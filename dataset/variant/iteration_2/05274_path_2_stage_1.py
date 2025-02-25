import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Defining the nodes (planets) and their positions
nodes = {
    'Earth': (1, 3), 
    'Mars': (0, 1), 
    'Jupiter': (2, 4), 
    'Venus': (1, 0), 
    'Saturn': (3, 1), 
    'Neptune': (4, 3), 
    'Pluto': (5, 1), 
    'Uranus': (3, 4), 
    'Mercury': (0, 3)
}

# Adding edges (trade routes) with trade volumes in tons
edges = [
    ('Earth', 'Mars', 300), 
    ('Earth', 'Jupiter', 500), 
    ('Earth', 'Venus', 200), 
    ('Mars', 'Jupiter', 150), 
    ('Jupiter', 'Saturn', 400),
    ('Saturn', 'Neptune', 600), 
    ('Neptune', 'Pluto', 100),
    ('Uranus', 'Neptune', 250), 
    ('Pluto', 'Jupiter', 180), 
    ('Venus', 'Saturn', 300),
    ('Mercury', 'Venus', 160), 
    ('Mercury', 'Earth', 140)
]

G = nx.Graph()
G.add_nodes_from(nodes.keys())
G.add_weighted_edges_from(edges)

pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(14, 10))

node_color_map = ['skyblue' if 'a' in planet.lower() else 'lightcoral' for planet in G.nodes]
nx.draw_networkx_nodes(G, pos, node_size=1200, node_color=node_color_map, alpha=0.9, edgecolors='black')

edge_width = [0.05 * G[u][v]['weight'] for u, v in G.edges]
nx.draw_networkx_edges(G, pos, width=edge_width, edge_color='gray', alpha=0.8)

nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif", font_weight='bold')

economic_significance = [120, 50, 180, 70, 130, 110, 60, 90, 100]
scatter_x = np.array([pos[node][0] for node in G.nodes])
scatter_y = np.array([pos[node][1] for node in G.nodes])
plt.scatter(scatter_x, scatter_y, s=economic_significance, c='gold', alpha=0.6)

plt.axis('off')
plt.tight_layout()
plt.show()