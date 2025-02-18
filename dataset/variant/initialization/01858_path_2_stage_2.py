import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes
nodes = ["Earth", "Mars Colony Alpha", "Mars Colony Beta", "Mars Colony Gamma", "Mars Colony Delta"]
G.add_nodes_from(nodes)

# Define directed edges with altered resource types
edges = [
    ("Earth", "Mars Colony Alpha", "Tech"),
    ("Earth", "Mars Colony Beta", "Water"),
    ("Earth", "Mars Colony Gamma", "Food"),
    ("Mars Colony Alpha", "Mars Colony Beta", "Water"),
    ("Mars Colony Beta", "Mars Colony Delta", "Data"),
    ("Mars Colony Delta", "Mars Colony Gamma", "Tech"),
    ("Mars Colony Gamma", "Mars Colony Alpha", "Food")
]

# Add edges to the graph
for source, target, resource in edges:
    G.add_edge(source, target, resource=resource)

# Define a spring layout for the graph
pos = nx.spring_layout(G, seed=42)

# Draw the nodes
plt.figure(figsize=(10, 8))
nx.draw_networkx_nodes(G, pos, node_size=3500, node_color='lightcoral', edgecolors='black')

# Draw the node labels
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

# Draw the edges with directional arrows
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), arrowstyle='-|>', arrowsize=20, edge_color='gray', connectionstyle='arc3,rad=0.2')

# Draw edge labels for resources
edge_labels = nx.get_edge_attributes(G, 'resource')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, font_color='lightcoral')

# Add a title to the plot
plt.title("Interplanetary Supply Chain of Mars Colonization\nResource and Communication Flows", fontsize=14, fontweight='bold')

# Remove axes
plt.axis('off')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()