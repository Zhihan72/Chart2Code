import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

cities = ["Dragon's Keep", "Elvenwood", "Stromgarde", "Moonshade", "Stonehaven", "Rivendell", "Blackrock"]

connections = [
    ("Dragon's Keep", "Elvenwood", 150),
    ("Dragon's Keep", "Stromgarde", 120),
    ("Elvenwood", "Moonshade", 180),
    ("Moonshade", "Stonehaven", 100),
    ("Stonehaven", "Stromgarde", 130),
    ("Stonehaven", "Dragon's Keep", 110),
    ("Moonshade", "Dragon's Keep", 90),
    ("Elvenwood", "Rivendell", 140),
    ("Rivendell", "Moonshade", 160),
    ("Blackrock", "Dragon's Keep", 200),
    ("Blackrock", "Stromgarde", 170),
    ("Blackrock", "Elvenwood", 110)
]

G = nx.Graph()
G.add_nodes_from(cities)

for source, dest, frequency in connections:
    G.add_edge(source, dest, weight=frequency)

message_frequencies = {city: sum(d['weight'] for u, v, d in G.edges(city, data=True)) for city in cities}
node_sizes = [500 + message_frequencies[city] * 2 for city in cities]

pos = nx.spring_layout(G, k=0.5, seed=42)
edge_labels = {(u, v): f'{d["weight"]} msgs' for u, v, d in G.edges(data=True)}
edge_widths = [1 + G[u][v]['weight'] / 50 for u, v in G.edges()]

# Apply a single color to all nodes
node_color = 'skyblue'

plt.figure(figsize=(12, 10))
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_color, alpha=0.9, edgecolors='black')
nx.draw_networkx_edges(G, pos, edgelist=G.edges, edge_color='black', width=edge_widths)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, label_pos=0.3, bbox=dict(facecolor='white', alpha=0.7))

plt.title("Communication Network in the Fantasy Kingdom:\nMessage Frequencies Between Key Cities", fontsize=16, fontweight='bold')
plt.axis('off')
plt.tight_layout()

# Update the legend to reflect the single color choice
plt.legend([plt.Line2D([0], [0], color=node_color, lw=4)], ["Cities"], title="Cities", loc='upper right', bbox_to_anchor=(1.1, 1))

plt.show()