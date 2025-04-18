import matplotlib.pyplot as plt
import networkx as nx

planets = ['Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']

travel_routes = [
    ('Earth', 'Saturn', 620),
    ('Mars', 'Jupiter', 480),
    ('Jupiter', 'Neptune', 510),
    ('Saturn', 'Earth', 370),
    ('Neptune', 'Mars', 440),
    ('Earth', 'Neptune', 290),
    ('Jupiter', 'Mars', 530)
]

G = nx.Graph()
G.add_nodes_from(planets)

for source, dest, volume in travel_routes:
    G.add_edge(source, dest, weight=volume)

travel_volumes = {planet: sum(d['weight'] for u, v, d in G.edges(planet, data=True)) for planet in planets}
node_sizes = [1500 + travel_volumes[planet] for planet in planets]

pos = nx.spring_layout(G)

edge_labels = {(u, v): f'{d["weight"]} passengers' for u, v, d in G.edges(data=True)}
edge_widths = [1 + G[u][v]['weight'] / 150 for u, v in G.edges()]

single_color = '#1f78b4'  # Using the same color for all nodes

plt.figure(figsize=(12, 10))
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=single_color, alpha=0.9, edgecolors='black')
nx.draw_networkx_edges(G, pos, edgelist=G.edges, edge_color='gray', width=edge_widths)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', font_color="white")

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, label_pos=0.3, bbox=dict(facecolor='white', alpha=0.7))

plt.title('Galactic Passageways:\nTrade and Travel in the Cosmos', fontsize=16, fontweight='bold')
plt.axis('off')
plt.tight_layout()

plt.show()