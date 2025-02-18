import matplotlib.pyplot as plt
import networkx as nx

# Define the players in the ecosystem
nodes = {
    "Sun": "Energy Source",
    "Grass": "Producer",
    "Shrubbery": "Producer",
    "Insects": "Primary Consumer",
    "Rabbits": "Primary Consumer",
    "Birds": "Secondary Consumer",
    "Foxes": "Tertiary Consumer",
    "Eagles": "Tertiary Consumer",
}

# Define the directed edges to show energy flow
edges = [
    ("Sun", "Grass"),
    ("Sun", "Shrubbery"),
    ("Grass", "Insects"),
    ("Shrubbery", "Insects"),
    ("Grass", "Rabbits"),
    ("Shrubbery", "Rabbits"),
    ("Insects", "Birds"),
    ("Rabbits", "Birds"),
    ("Rabbits", "Foxes"),
    ("Birds", "Eagles"),
    ("Foxes", "Eagles"),
]

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Node positions using spring layout
pos = nx.spring_layout(G, k=0.5, iterations=50)

# Plot the directed graph
plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, node_color='lightgreen', node_size=2500)
nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, arrowsize=20, width=2)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', font_color='black', labels={node: node for node in G.nodes()})

# Turn off axes
plt.axis('off')

# Optimize layout
plt.tight_layout()

# Show plot
plt.show()