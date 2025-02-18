import matplotlib.pyplot as plt
import networkx as nx

# Define planets (nodes) in the coalition
planets = ['Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']

# Define travel routes (directed edges) with travel and trade volumes
travel_routes = [
    ('Earth', 'Mars', 700),
    ('Earth', 'Jupiter', 450),
    ('Mars', 'Saturn', 300),
    ('Saturn', 'Neptune', 550),
    ('Neptune', 'Earth', 600),
    ('Jupiter', 'Saturn', 350),
    ('Mars', 'Neptune', 500)
]

# Create a directed graph
G = nx.DiGraph()
G.add_nodes_from(planets)

# Add edges with weights
for source, dest, volume in travel_routes:
    G.add_edge(source, dest, weight=volume)

# Calculate total travel volume per planet
travel_volumes = {planet: sum(d['weight'] for u, v, d in G.edges(planet, data=True)) + 
                              sum(d['weight'] for u, v, d in G.in_edges(planet, data=True)) for planet in planets}

# Assign node sizes based on total travel volume
node_sizes = [1500 + travel_volumes[planet] for planet in planets]

# Define positions using a spring layout
pos = nx.spring_layout(G)

# Extract weights for edge labels and widths
edge_labels = {(u, v): f'{d["weight"]} passengers' for u, v, d in G.edges(data=True)}
edge_widths = [1 + G[u][v]['weight'] / 150 for u, v in G.edges()]

# Define color maps for nodes and edges
node_colors = ['#1f78b4', '#33a02c', '#e31a1c', '#ff7f00', '#6a3d9a']

# Plotting the graph
plt.figure(figsize=(12, 10))
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.9, edgecolors='black')
nx.draw_networkx_edges(G, pos, edgelist=G.edges, edge_color='gray', arrows=True, arrowsize=15, width=edge_widths)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', font_color="white")

# Add edge labels with an offset
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, label_pos=0.3, bbox=dict(facecolor='white', alpha=0.7))

# Title and layout adjustments
plt.title('Galactic Passageways:\nTrade and Travel in the Cosmos', fontsize=16, fontweight='bold')
plt.axis('off')
plt.tight_layout()

# Create a custom legend
legend_lines = [plt.Line2D([0], [0], color=node_colors[i], lw=4) for i in range(len(planets))]
plt.legend(legend_lines, ['Gaia', 'Ares', 'Zeus', 'Kronos', 'Poseidon'], title="Celestial Bodies", loc='upper right', bbox_to_anchor=(1.2, 1))

# Display the plot
plt.show()