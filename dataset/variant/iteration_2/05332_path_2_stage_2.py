import matplotlib.pyplot as plt
import networkx as nx

nodes = {
    "Sun": "Energy Source",
    "Grass": "Producer",
    "Shrubbery": "Producer",
    "Trees": "Producer",  # New Producer
    "Insects": "Primary Consumer",
    "Rabbits": "Primary Consumer",
    "Squirrels": "Primary Consumer",  # New Primary Consumer
    "Birds": "Secondary Consumer",
    "Snakes": "Secondary Consumer",  # New Secondary Consumer
    "Foxes": "Tertiary Consumer",
    "Wolves": "Tertiary Consumer",  # New Tertiary Consumer
    "Eagles": "Tertiary Consumer",
}

edges = [
    ("Sun", "Grass"),
    ("Sun", "Shrubbery"),
    ("Sun", "Trees"),  # New edge
    ("Grass", "Insects"),
    ("Shrubbery", "Insects"),
    ("Trees", "Squirrels"),  # New edge
    ("Grass", "Rabbits"),
    ("Shrubbery", "Rabbits"),
    ("Insects", "Birds"),
    ("Squirrels", "Snakes"),  # New edge
    ("Rabbits", "Birds"),
    ("Rabbits", "Foxes"),
    ("Snakes", "Wolves"),  # New edge
    ("Birds", "Eagles"),
    ("Foxes", "Eagles"),
]

G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

pos = nx.spring_layout(G, k=0.5, iterations=50)

color_map = {
    "Energy Source": "orange",
    "Producer": "#FF6347",
    "Primary Consumer": "#4682B4",
    "Secondary Consumer": "#9ACD32",
    "Tertiary Consumer": "#FFD700",
}

node_colors = [color_map[nodes[node]] for node in G.nodes()]

plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=2500)
nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, arrowsize=20, width=2)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', font_color='black')

plt.title("Energy Flow in EcoWorld:\nFrom Sun to Apex Predators", fontsize=16, fontweight='bold')

labels_legend = {node: role for node, role in nodes.items()}
for node, (x, y) in pos.items():
    plt.text(x, y - 0.1, labels_legend[node], fontsize=9, ha='center', va='center', bbox=dict(facecolor='white', alpha=0.8))

plt.axis('off')
plt.tight_layout()
plt.show()