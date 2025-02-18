import matplotlib.pyplot as plt
import networkx as nx

features = [
    "Playg.", "Picnic", "Fount.", "Path", 
    "Dog PK", "Garden", "Amphi.", "Rest.", "Food"
]

connections = [
    ("Playg.", "Picnic"),
    ("Picnic", "Garden"),
    ("Garden", "Fount."),
    ("Fount.", "Path"),
    ("Path", "Amphi."),
    ("Amphi.", "Rest."),
    ("Rest.", "Food"),
    ("Food", "Dog PK"),
    ("Dog PK", "Playg.")
]

# Change graph type to DiGraph for directed edges
G = nx.DiGraph()
G.add_nodes_from(features)
G.add_edges_from(connections)

pos = nx.spring_layout(G, seed=42)

# Colors and sizes for nodes
node_colors = ['#ff4500', '#4169e1', '#32cd32', '#ff1493', '#ffd700', '#20b2aa', '#ff00ff', '#00ced1', '#ff6347']
node_sizes = [1200, 1000, 800, 1100, 900, 950, 1050, 850, 800]

plt.figure(figsize=(12, 10))
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=node_sizes,
        font_size=10, font_weight='bold', edge_color='gray', width=2.0, alpha=0.7, arrows=True)

plt.title(
    'Park Features Network (Directed)', 
    fontsize=16, fontweight='bold', pad=20
)

plt.axis('off')
plt.tight_layout()
plt.show()