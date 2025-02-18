import matplotlib.pyplot as plt
import networkx as nx

# Define intersections
intersections = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G'
]

# Define traffic flow between intersections (cars per hour)
traffic_routes = [
    ('A', 'B', 50),
    ('A', 'C', 30),
    ('B', 'D', 20),
    ('C', 'D', 25),
    ('B', 'E', 40),
    ('D', 'F', 60),
    ('E', 'F', 30),
    ('E', 'G', 20),
    ('F', 'G', 10)
]

# Create a directed graph
G = nx.DiGraph()

# Add nodes
G.add_nodes_from(intersections)

# Add edges with traffic volumes as weights
for route in traffic_routes:
    G.add_edge(route[0], route[1], weight=route[2])

# Determine edge widths based on traffic volume
edge_widths = [G[u][v]['weight'] / 10 for u, v in G.edges()]

# Create a manual layout for the nodes
pos = {
    'A': (0, 3),
    'B': (2, 3),
    'C': (0, 1),
    'D': (2, 1),
    'E': (4, 3),
    'F': (4, 1),
    'G': (6, 2)
}

# Plot the directed graph
plt.figure(figsize=(12, 8))

# Draw nodes with different edge colors and shapes
nx.draw_networkx_nodes(G, pos, node_color='lightgreen', node_size=3000, edgecolors='brown')

# Draw edges with different styles and color
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=25, edge_color='grey', width=edge_widths, style='dashed')

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=14, font_family='serif')

# Add edge labels for traffic volumes
edge_labels = {(u, v): f"{G[u][v]['weight']} cars/h" for u, v in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12, font_color='blue')

# Add title
plt.title('Traffic Flow: Megacity Intersections', fontsize=16, family='serif')

# Hide axes
plt.axis('off')

# Automatically adjust the layout
plt.tight_layout()

# Show the plot
plt.show()