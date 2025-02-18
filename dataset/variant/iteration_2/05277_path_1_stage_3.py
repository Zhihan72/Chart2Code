import matplotlib.pyplot as plt
import networkx as nx

cities = ["Stonehaven", "Moonshade", "Dragon's Keep", "Stromgarde"]

# Removed ("Elvenwood", "Stromgarde", 120) and ("Elvenwood", "Moonshade", 180) connections
connections = [
    ("Stonehaven", "Moonshade", 100),
    ("Moonshade", "Dragon's Keep", 90),
    ("Dragon's Keep", "Stonehaven", 150),
    ("Stromgarde", "Stonehaven", 130),
    ("Stromgarde", "Dragon's Keep", 110)
]

G = nx.Graph()
G.add_edges_from((source, dest, {'weight': frequency}) for source, dest, frequency in connections)

message_frequencies = {city: sum(d['weight'] for _, _, d in G.edges(city, data=True)) for city in cities}
node_sizes = [500 + message_frequencies[city] * 2 for city in cities]
pos = nx.spring_layout(G, k=0.5, seed=42)
edge_labels = {(u, v): f'{d["weight"]} msgs' for u, v, d in G.edges(data=True)}
edge_widths = [1 + G[u][v]['weight'] / 50 for u, v in G.edges()]

node_colors = ['#FF6347', '#1E90FF', '#32CD32', '#FF69B4'] # Removed Elvenwood's color

plt.figure(figsize=(12, 10))
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, edgecolors='black')
nx.draw_networkx_edges(G, pos, width=edge_widths, edge_color='black')
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, label_pos=0.3, bbox=dict(facecolor='white', alpha=0.7))

plt.title("Mystic Realm Network:\nInter-city Message Paths", fontsize=16, fontweight='bold')
plt.axis('off')
plt.tight_layout()

legend_lines = [plt.Line2D([0], [0], color=node_colors[i], lw=4) for i in range(len(cities))]
plt.legend(legend_lines, cities, title="Metropoles", loc='upper right', bbox_to_anchor=(1.1, 1))

plt.show()