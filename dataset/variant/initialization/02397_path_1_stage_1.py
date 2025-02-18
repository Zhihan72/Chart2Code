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

G = nx.Graph()
G.add_nodes_from(features)
G.add_edges_from(connections)

pos = nx.spring_layout(G, seed=42)

node_colors = ['#9acd32', '#ff6347', '#1e90ff', '#ffeb3b', '#f4a460', '#adff2f', '#dda0dd', '#8b4513', '#ff69b4']
node_sizes = [1200, 1000, 800, 1100, 900, 950, 1050, 850, 800]

plt.figure(figsize=(12, 10))
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=node_sizes,
        font_size=10, font_weight='bold', edge_color='gray', width=2.0, alpha=0.7)

plt.title(
    'Park Features Network', 
    fontsize=16, fontweight='bold', pad=20
)

plt.axis('off')
plt.tight_layout()
plt.show()