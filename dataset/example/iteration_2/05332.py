import matplotlib.pyplot as plt
import networkx as nx

# Backstory:
# The chart illustrates the flow of energy within a fictional ecosystem called "EcoWorld". The ecosystem consists 
# of both producers (plants) and consumers (animals). This flow of energy through various trophic levels is key to 
# maintaining balance within the ecosystem.

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

# Define the directed edges to show energy flow from producers to consumers
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

# Add title and supplementary labels
plt.title("Energy Flow in EcoWorld:\nFrom Sun to Apex Predators", fontsize=16, fontweight='bold')

# Additional labels for node roles
labels_legend = {node: role for node, role in nodes.items()}

# Display legend annotations beneath each node
for node, (x, y) in pos.items():
    plt.text(x, y - 0.1, labels_legend[node], fontsize=9, ha='center', va='center', bbox=dict(facecolor='white', alpha=0.8))

# Turn off axes
plt.axis('off')

# Optimize layout
plt.tight_layout()

# Show plot
plt.show()