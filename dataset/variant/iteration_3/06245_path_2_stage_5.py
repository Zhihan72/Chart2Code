import matplotlib.pyplot as plt
import networkx as nx

civilizations = [
    "Empire of the Nile", 
    "Tigris-Euphrates Culture", 
    "Indus Realm", 
    "Middle Kingdom", 
    "Hellenic States", 
    "Roman Empire", 
    "Yucatan Society", 
    "Cusco Domain",
    "Atlantic Confederation", 
    "Saharan League"
]

connections = [
    ("Empire of the Nile", "Tigris-Euphrates Culture", 20),
    ("Tigris-Euphrates Culture", "Indus Realm", 15),
    ("Middle Kingdom", "Indus Realm", 10),
    ("Hellenic States", "Roman Empire", 25),
    ("Hellenic States", "Tigris-Euphrates Culture", 18),
    ("Roman Empire", "Empire of the Nile", 22),
    ("Yucatan Society", "Cusco Domain", 19),
    ("Cusco Domain", "Middle Kingdom", 14),
    ("Yucatan Society", "Indus Realm", 12),
    ("Middle Kingdom", "Tigris-Euphrates Culture", 17),
    ("Atlantic Confederation", "Saharan League", 13),
    ("Saharan League", "Tigris-Euphrates Culture", 11),
    ("Atlantic Confederation", "Empire of the Nile", 16)
]

G = nx.Graph()
G.add_nodes_from(civilizations)
G.add_weighted_edges_from(connections)

pos = nx.spring_layout(G, seed=2023)

edges = G.edges(data=True)
edge_weights = [data['weight'] for _, _, data in edges]

node_size = [1000 * (G.degree(civilization) + 1) for civilization in civilizations]
nx.draw_networkx_nodes(G, pos, node_color="#FFD700", node_size=node_size, edgecolors='black', linewidths=1.5)

nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='black', width=[weight / 5 for weight in edge_weights])

nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', font_color='darkgreen')

plt.title("Ancestral Networks of Exchange and Interaction", fontsize=16, fontweight='bold', color='navy', pad=20)
plt.axis('off')
plt.tight_layout()

plt.show()