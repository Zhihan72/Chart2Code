import matplotlib.pyplot as plt
import networkx as nx

planets = ['Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']

travel_routes = [
    ('Earth', 'Mars', 700),
    ('Earth', 'Jupiter', 450),
    ('Mars', 'Saturn', 300),
    ('Saturn', 'Neptune', 550),
    ('Neptune', 'Earth', 600),
    ('Jupiter', 'Saturn', 350),
    ('Mars', 'Neptune', 500)
]

G = nx.DiGraph()
G.add_nodes_from(planets)

for source, dest, volume in travel_routes:
    G.add_edge(source, dest, weight=volume)

travel_volumes = {planet: sum(d['weight'] for u, v, d in G.edges(planet, data=True)) +
                               sum(d['weight'] for u, v, d in G.in_edges(planet, data=True)) for planet in planets}

node_sizes = [1500 + travel_volumes[planet] for planet in planets]

pos = nx.spring_layout(G)

edge_labels = {(u, v): f'{d["weight"]} travelers' for u, v, d in G.edges(data=True)}
edge_widths = [1 + G[u][v]['weight'] / 150 for u, v in G.edges()]

node_colors = ['#ff7f00', '#1f78b4', '#e31a1c', '#6a3d9a', '#33a02c']

plt.figure(figsize=(12, 10))
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.9, edgecolors='black')

nx.draw_networkx_edges(G, pos, edgelist=G.edges, edge_color='black', arrows=True, arrowsize=12, width=edge_widths)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='light', font_color="yellow")

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, label_pos=0.5, bbox=dict(facecolor='navy', alpha=0.5))

plt.title('Interstellar Travel Routes Among Coalition Planets', fontsize=14, fontweight='light')
plt.grid(True, linestyle='-.', alpha=0.3)
plt.axis('off')
plt.tight_layout()

legend_markers = [plt.Line2D([0], [0], marker='o', color='w', label=planet, markersize=10, markerfacecolor=node_colors[i]) for i, planet in enumerate(planets)]
plt.legend(handles=legend_markers, title="Planets", loc='lower left', bbox_to_anchor=(-0.1, -0.1))

plt.show()