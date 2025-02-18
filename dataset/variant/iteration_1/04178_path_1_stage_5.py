import matplotlib.pyplot as plt
import networkx as nx

planets = ['Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']

travel_routes = [
    ('Earth', 'Mars', 700),
    ('Earth', 'Jupiter', 450),
    ('Mars', 'Saturn', 300),
    ('Saturn', 'Neptune', 550),
    ('Neptune', 'Earth', 600),
    ('Mars', 'Neptune', 500)
]

G = nx.Graph()
G.add_nodes_from(planets)

for source, dest, volume in travel_routes:
    G.add_edge(source, dest, weight=volume)

travel_volumes = {planet: sum(d['weight'] for u, v, d in G.edges(planet, data=True)) for planet in planets}

node_sizes = [1500 + travel_volumes[planet] for planet in planets]

pos = nx.spring_layout(G)

edge_widths = [1 + G[u][v]['weight'] / 150 for u, v in G.edges()]
node_colors = ['#33a02c', '#6a3d9a', '#1f78b4', '#e31a1c', '#ff7f00']

plt.figure(figsize=(12, 10))
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.9, edgecolors='black')
nx.draw_networkx_edges(G, pos, edgelist=G.edges, edge_color='black', width=edge_widths)  

plt.grid(True, linestyle='-.', alpha=0.3)
plt.axis('off')
plt.tight_layout()

plt.show()