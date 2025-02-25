import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define nodes with their positions
nodes = {
    'Zorgon': (1, 3), 
    'Xandar': (0, 1), 
    'Pluton': (2, 4), 
    'Vega': (1, 0), 
    'Titan': (3, 1), 
    'Ganymede': (4, 3), 
    'Zebes': (5, 1), 
    'Krypton': (3, 4), 
    'Helios': (0, 3)
}

# Define the edges along with weights
edges = [
    ('Zorgon', 'Xandar', 300), 
    ('Zorgon', 'Pluton', 500), 
    ('Zorgon', 'Vega', 200), 
    ('Xandar', 'Pluton', 150), 
    ('Pluton', 'Titan', 400),
    ('Titan', 'Ganymede', 600), 
    ('Ganymede', 'Zebes', 100),
    ('Krypton', 'Ganymede', 250), 
    ('Zebes', 'Pluton', 180), 
    ('Vega', 'Titan', 300),
    ('Helios', 'Vega', 160), 
    ('Helios', 'Zorgon', 140)
]

# Create an undirected graph
G = nx.Graph()
G.add_nodes_from(nodes.keys())
G.add_weighted_edges_from(edges)

# Compute positions for visualization using spring layout
pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(14, 10))

# Determine node colors based on name content
node_color_map = ['limegreen' if 'o' in planet.lower() else 'mediumorchid' for planet in G.nodes]
nx.draw_networkx_nodes(G, pos, node_size=1200, node_color=node_color_map, alpha=0.9, edgecolors='black')

# Set edge widths proportional to weights
edge_width = [0.05 * G[u][v]['weight'] for u, v in G.edges]
nx.draw_networkx_edges(G, pos, width=edge_width, edge_color='gray', alpha=0.8)

# Add labels to nodes
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif", font_weight='bold')

# Display edge weights
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_color='blue')

# Legend for node types
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='limegreen', markersize=10, label='Contains "o" in Name'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='mediumorchid', markersize=10, label='No "o" in Name')
]
plt.legend(handles=legend_elements, title='Cosmic Entities', loc='upper left')

# Plot nodes significance
economic_significance = [120, 50, 180, 70, 130, 110, 60, 90, 100]
scatter_x = np.array([pos[node][0] for node in G.nodes])
scatter_y = np.array([pos[node][1] for node in G.nodes])
plt.scatter(scatter_x, scatter_y, s=economic_significance, c='gold', alpha=0.6, label='Significance Rating')

plt.title("Galactic Connectivity of Cosmic Entities\nTrade Pathways and Significance", fontsize=16, fontweight='bold')
plt.axis('off')
plt.tight_layout()

plt.show()