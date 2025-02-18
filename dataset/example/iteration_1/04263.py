import matplotlib.pyplot as plt
import networkx as nx

# Title and Backstory
# In a sprawling megacity, traffic management becomes increasingly complex. The transportation department is 
# analyzing the flow of traffic between major intersections to devise a better traffic regulation system.

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

# Create a manual layout for the nodes to improve readability
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

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=2500, edgecolors='k')

# Draw edges with varying widths
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, edge_color='black', width=edge_widths)

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=14, font_weight='bold')

# Add edge labels for traffic volumes
edge_labels = {(u, v): f"{G[u][v]['weight']} cars/h" for u, v in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12, font_color='red')

# Add title and labels
plt.title('Traffic Flow Analysis: Major Intersections in Megacity', fontsize=16, weight='bold')
plt.axis('off')

# Automatically adjust the layout to prevent text overlap
plt.tight_layout()

# Show the plot
plt.show()