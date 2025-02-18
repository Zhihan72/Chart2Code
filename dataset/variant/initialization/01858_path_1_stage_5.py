import matplotlib.pyplot as plt
import networkx as nx

# Create an undirected graph
G = nx.Graph()

# Add nodes to the graph excluding "Mars Colony Delta"
nodes = ["Earth", "Mars Colony Alpha", "Mars Colony Beta", "Mars Colony Gamma"]
G.add_nodes_from(nodes)

# Add undirected edges to the graph excluding any connected to "Mars Colony Delta"
edges = [
    ("Earth", "Mars Colony Alpha", "Water"),
    ("Earth", "Mars Colony Beta", "Food"),
    ("Earth", "Mars Colony Gamma", "Tech"),
    ("Mars Colony Alpha", "Mars Colony Beta", "Data"),
    ("Mars Colony Gamma", "Mars Colony Alpha", "Food")
]

for source, target, resource in edges:
    G.add_edge(source, target, resource=resource)

# Generate positions for the nodes
pos = nx.spring_layout(G, seed=42)

# Plot the graph
plt.figure(figsize=(10, 8))
nx.draw_networkx_nodes(G, pos, node_size=3500, node_color='lightcoral', edgecolors='black')

# Draw the undirected edges
nx.draw_networkx_edges(G, pos, edge_color='lightcoral', connectionstyle='arc3,rad=0.2')

# Turn off the axis and display the plot
plt.axis('off')
plt.tight_layout()
plt.show()