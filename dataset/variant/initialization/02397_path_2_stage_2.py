import matplotlib.pyplot as plt
import networkx as nx

features = [
    "Playground", "Picnic Area", "Fountain", "Walking Path", 
    "Dog Park", "Garden", "Amphitheater", "Restrooms", "Food Stall"
]

# Altered connections by manually permuting them to simulate randomness
connections = [
    ("Fountain", "Garden"),
    ("Playground", "Restrooms"),
    ("Garden", "Walking Path"),
    ("Picnic Area", "Dog Park"),
    ("Walking Path", "Food Stall"),
    ("Dog Park", "Playground"),
    ("Restrooms", "Amphitheater"),
    ("Food Stall", "Fountain"),
    ("Amphitheater", "Picnic Area")
]

G = nx.DiGraph()
G.add_nodes_from(features)
G.add_edges_from(connections)

pos = nx.spring_layout(G, seed=42)

node_colors = ['#9acd32', '#ff6347', '#1e90ff', '#ffeb3b', '#f4a460', '#adff2f', '#dda0dd', '#8b4513', '#ff69b4']
node_sizes = [1200, 1000, 800, 1100, 900, 950, 1050, 850, 800]

plt.figure(figsize=(12, 10))
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes)
nx.draw_networkx_edges(G, pos, connectionstyle='arc3,rad=0.1', arrowstyle='-|>', arrowsize=15)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

plt.title(
    'Directed Interaction Network of Urban Park Features', 
    fontsize=16, fontweight='bold', pad=20
)

plt.axis('off')
plt.tight_layout()
plt.show()