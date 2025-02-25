import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define the nodes with their positions, shuffled
nodes = {
    'Earth': (5, 1), 
    'Mars': (3, 1), 
    'Jupiter': (0, 1), 
    'Venus': (1, 3), 
    'Saturn': (4, 3), 
    'Neptune': (0, 3), 
    'Pluto': (3, 4), 
    'Uranus': (2, 4), 
    'Mercury': (1, 0)
}

# Randomly altered edges with new weights
edges = [
    ('Earth', 'Mars', 180), 
    ('Earth', 'Jupiter', 140), 
    ('Earth', 'Venus', 300), 
    ('Mars', 'Jupiter', 400), 
    ('Jupiter', 'Saturn', 300),
    ('Saturn', 'Neptune', 150), 
    ('Neptune', 'Pluto', 600),
    ('Uranus', 'Neptune', 160), 
    ('Pluto', 'Jupiter', 250), 
    ('Venus', 'Saturn', 100),
    ('Mercury', 'Venus', 500), 
    ('Mercury', 'Earth', 200)
]

G = nx.Graph()
G.add_nodes_from(nodes.keys())
G.add_weighted_edges_from(edges)

pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(14, 10))

# Shuffled node color map
new_node_color_map = ['lightcyan', 'lightblue', 'orange', 'pink', 'lightyellow', 'lightgreen', 'beige', 'lightgray', 'lightpink']
nx.draw_networkx_nodes(G, pos, node_size=1200, node_color=new_node_color_map, alpha=0.9, edgecolors='black')

edge_width = [0.05 * G[u][v]['weight'] for u, v in G.edges]
nx.draw_networkx_edges(G, pos, width=edge_width, edge_color='gray', alpha=0.8)

# Randomly altered economic significance values
economic_significance = [100, 180, 50, 120, 60, 70, 130, 110, 90]
scatter_x = np.array([pos[node][0] for node in G.nodes])
scatter_y = np.array([pos[node][1] for node in G.nodes])
plt.scatter(scatter_x, scatter_y, s=economic_significance, c='gold', alpha=0.6)

plt.axis('off')
plt.tight_layout()
plt.show()