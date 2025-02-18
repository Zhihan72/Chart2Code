import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Title and Backstory:
# The chart is about "The Interstellar Trade Routes of the Galactic Federation"
# It visualizes key trade routes between major planets and the volume of goods traded annually.

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

# Create Graph
G = nx.Graph()
G.add_nodes_from(nodes.keys())
G.add_weighted_edges_from(edges)

# Extracting positions for plotting
pos = nx.spring_layout(G, seed=42)  # Using spring layout for better visualization

# Plotting the graph
plt.figure(figsize=(14, 10))

# Draw nodes
node_color_map = ['skyblue' if 'a' in planet.lower() else 'lightcoral' for planet in G.nodes]
nx.draw_networkx_nodes(G, pos, node_size=1200, node_color=node_color_map, alpha=0.9, edgecolors='black')

# Draw edges
edge_width = [0.05 * G[u][v]['weight'] for u, v in G.edges]
nx.draw_networkx_edges(G, pos, width=edge_width, edge_color='gray', alpha=0.8)

# Adding labels to nodes
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif", font_weight='bold')

# Adding edge labels (trade volume)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_color='blue')

# Adding a legend
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='skyblue', markersize=10, label='Contains "a" in Name'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='lightcoral', markersize=10, label='No "a" in Name')
]
plt.legend(handles=legend_elements, title='Planetary Classification', loc='upper left')

# Scatter plot overlay: Economic significance (based on some arbitrary data)
economic_significance = [120, 50, 180, 70, 130, 110, 60, 90, 100]
scatter_x = np.array([pos[node][0] for node in G.nodes])
scatter_y = np.array([pos[node][1] for node in G.nodes])
plt.scatter(scatter_x, scatter_y, s=economic_significance, c='gold', alpha=0.6, label='Economic Significance')

# Adding title and removing axes
plt.title("Interstellar Trade Routes of the Galactic Federation\nAnnual Trade Volumes and Economic Significance", fontsize=16, fontweight='bold')
plt.axis('off')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()