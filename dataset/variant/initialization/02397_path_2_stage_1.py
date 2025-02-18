import matplotlib.pyplot as plt
import networkx as nx

# Define park features as nodes
features = [
    "Playground", "Picnic Area", "Fountain", "Walking Path", 
    "Dog Park", "Garden", "Amphitheater", "Restrooms", "Food Stall"
]

# Define connections between features as directed edges
connections = [
    ("Playground", "Picnic Area"),
    ("Picnic Area", "Garden"),
    ("Garden", "Fountain"),
    ("Fountain", "Walking Path"),
    ("Walking Path", "Amphitheater"),
    ("Amphitheater", "Restrooms"),
    ("Restrooms", "Food Stall"),
    ("Food Stall", "Dog Park"),
    ("Dog Park", "Playground")
]

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges
G.add_nodes_from(features)
G.add_edges_from(connections)

# Position nodes using spring layout
pos = nx.spring_layout(G, seed=42)

# Define node colors and sizes
node_colors = ['#9acd32', '#ff6347', '#1e90ff', '#ffeb3b', '#f4a460', '#adff2f', '#dda0dd', '#8b4513', '#ff69b4']
node_sizes = [1200, 1000, 800, 1100, 900, 950, 1050, 850, 800]

# Plot the directed graph
plt.figure(figsize=(12, 10))
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes)
nx.draw_networkx_edges(G, pos, connectionstyle='arc3,rad=0.1', arrowstyle='-|>', arrowsize=15)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

# Add a title
plt.title(
    'Directed Interaction Network of Urban Park Features', 
    fontsize=16, fontweight='bold', pad=20
)

# Hide axes for a clean visualization
plt.axis('off')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()