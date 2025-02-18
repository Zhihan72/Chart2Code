import matplotlib.pyplot as plt
import networkx as nx

nodes = {
    "Sun": "Source",
    "Grass": "Prod.",
    "Shrubbery": "Prod.",
    "Flowers": "Prod.",  # New Producer
    "Insects": "Prim. Cons.",
    "Rabbits": "Prim. Cons.",
    "Birds": "Sec. Cons.",
    "Bees": "Prim. Cons.",  # New Primary Consumer
    "Foxes": "Tert. Cons.",
    "Eagles": "Tert. Cons.",
    "Bears": "Tert. Cons.",  # New Tertiary Consumer
}

edges = [
    ("Sun", "Grass"),
    ("Sun", "Shrubbery"),
    ("Sun", "Flowers"),  # New Edge
    ("Grass", "Insects"),
    ("Shrubbery", "Insects"),
    ("Flowers", "Insects"),  # New Edge
    ("Grass", "Rabbits"),
    ("Shrubbery", "Rabbits"),
    ("Insects", "Birds"),
    ("Rabbits", "Birds"),
    ("Rabbits", "Foxes"),
    ("Birds", "Eagles"),
    ("Foxes", "Eagles"),
    ("Flowers", "Bees"),   # New Edge
    ("Bees", "Bears"),     # New Edge
]

G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

pos = nx.spring_layout(G, k=0.5, iterations=50)

plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, node_color='cornflowerblue', node_size=2500)
nx.draw_networkx_edges(G, pos, edge_color='teal', arrows=True, arrowsize=20, width=2)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', font_color='black')

plt.axis('off')
plt.tight_layout()
plt.show()