import matplotlib.pyplot as plt
import networkx as nx

planets = ['Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']

# Altered travel routes with weights, direction is ignored in undirected graph
travel_routes = [
    ('Earth', 'Saturn', 620),
    ('Mars', 'Jupiter', 480),
    ('Jupiter', 'Neptune', 510),
    ('Saturn', 'Earth', 370),
    ('Neptune', 'Mars', 440),
    ('Earth', 'Neptune', 290),
    ('Jupiter', 'Mars', 530)
]

# Create an undirected graph
G = nx.Graph()
G.add_nodes_from(planets)

# Add edges to the graph
for source, dest, volume in travel_routes:
    G.add_edge(source, dest, weight=volume)

# Calculate travel volumes for node sizes
travel_volumes = {planet: sum(d['weight'] for u, v, d in G.edges(planet, data=True)) for planet in planets}
node_sizes = [1500 + travel_volumes[planet] for planet in planets]

# Define layout
pos = nx.spring_layout(G)

# Create edge labels
edge_labels = {(u, v): f'{d["weight"]} passengers' for u, v, d in G.edges(data=True)}
edge_widths = [1 + G[u][v]['weight'] / 150 for u, v in G.edges()]

node_colors = ['#1f78b4', '#33a02c', '#e31a1c', '#ff7f00', '#6a3d9a']

plt.figure(figsize=(12, 10))
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.9, edgecolors='black')
nx.draw_networkx_edges(G, pos, edgelist=G.edges, edge_color='gray', width=edge_widths)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', font_color="white")

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, label_pos=0.3, bbox=dict(facecolor='white', alpha=0.7))

plt.title('Galactic Passageways:\nTrade and Travel in the Cosmos', fontsize=16, fontweight='bold')
plt.axis('off')
plt.tight_layout()

legend_lines = [plt.Line2D([0], [0], color=node_colors[i], lw=4) for i in range(len(planets))]
plt.legend(legend_lines, ['Gaia', 'Ares', 'Zeus', 'Kronos', 'Poseidon'], title="Celestial Bodies", loc='upper right', bbox_to_anchor=(1.2, 1))

plt.show()