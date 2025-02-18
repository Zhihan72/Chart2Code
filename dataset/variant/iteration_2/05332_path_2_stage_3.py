import matplotlib.pyplot as plt
import networkx as nx

nodes = {
    "Sun": "Source",
    "Grass": "Prod",
    "Shrubbery": "Prod",
    "Trees": "Prod",
    "Insects": "Prim Cons",
    "Rabbits": "Prim Cons",
    "Squirrels": "Prim Cons",
    "Birds": "Sec Cons",
    "Snakes": "Sec Cons",
    "Foxes": "Ter Cons",
    "Wolves": "Ter Cons",
    "Eagles": "Ter Cons",
}

edges = [
    ("Sun", "Grass"),
    ("Sun", "Shrubbery"),
    ("Sun", "Trees"),
    ("Grass", "Insects"),
    ("Shrubbery", "Insects"),
    ("Trees", "Squirrels"),
    ("Grass", "Rabbits"),
    ("Shrubbery", "Rabbits"),
    ("Insects", "Birds"),
    ("Squirrels", "Snakes"),
    ("Rabbits", "Birds"),
    ("Rabbits", "Foxes"),
    ("Snakes", "Wolves"),
    ("Birds", "Eagles"),
    ("Foxes", "Eagles"),
]

G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

pos = nx.spring_layout(G, k=0.5, iterations=50)

color_map = {
    "Source": "orange",
    "Prod": "#FF6347",
    "Prim Cons": "#4682B4",
    "Sec Cons": "#9ACD32",
    "Ter Cons": "#FFD700",
}

node_colors = [color_map[nodes[node]] for node in G.nodes()]

plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=2500)
nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, arrowsize=20, width=2)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', font_color='black')

plt.title("EcoWorld: Sun to Apex", fontsize=16, fontweight='bold')

labels_legend = {node: role for node, role in nodes.items()}
for node, (x, y) in pos.items():
    plt.text(x, y - 0.1, labels_legend[node], fontsize=9, ha='center', va='center', bbox=dict(facecolor='white', alpha=0.8))

plt.axis('off')
plt.tight_layout()
plt.show()