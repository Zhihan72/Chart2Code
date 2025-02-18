import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

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
    ("Empire of the Nile", "Tigris-Euphrates Culture", "Merchandise", 20),
    ("Tigris-Euphrates Culture", "Indus Realm", "Art Exchange", 15),
    ("Middle Kingdom", "Indus Realm", "Conflict", 10),
    ("Hellenic States", "Roman Empire", "Commerce", 25),
    ("Hellenic States", "Tigris-Euphrates Culture", "Knowledge Transfer", 18),
    ("Roman Empire", "Empire of the Nile", "Hostility", 22),
    ("Yucatan Society", "Cusco Domain", "Barter", 19),
    ("Cusco Domain", "Middle Kingdom", "Culture Swap", 14),
    ("Yucatan Society", "Indus Realm", "Commerce", 12),
    ("Middle Kingdom", "Tigris-Euphrates Culture", "Merchandise", 17),
    ("Atlantic Confederation", "Saharan League", "Pact", 13),
    ("Saharan League", "Tigris-Euphrates Culture", "Trade", 11),
    ("Atlantic Confederation", "Empire of the Nile", "Alliance", 16)
]

G = nx.DiGraph()
G.add_nodes_from(civilizations)
for src, dst, influence, weight in connections:
    G.add_edge(src, dst, influence=influence, weight=weight)

pos = nx.spring_layout(G, seed=2023)

edges = G.edges(data=True)
edge_colors = [
    "red" if data['influence'] == "Merchandise" 
    else "blue" if data['influence'] == "Art Exchange"
    else "green" if data['influence'] == "Conflict" 
    else "purple" if data['influence'] == "Pact"
    else "orange"
    for _, _, data in edges
]
edge_weights = [data['weight'] for _, _, data in edges]

node_size = [1000 * (G.degree(civilization) + 1) for civilization in civilizations]
nx.draw_networkx_nodes(G, pos, node_color="#FFD700", node_size=node_size, edgecolors='black', linewidths=1.5)

nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color=edge_colors, width=[weight / 5 for weight in edge_weights], arrowstyle='-|>', arrowsize=15)

nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', font_color='darkgreen')

edge_labels = {(u, v): f"{data['influence']} ({data['weight']})" for u, v, data in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_color='black', font_weight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.6))

plt.title("Ancestral Networks of Exchange and Interaction", fontsize=16, fontweight='bold', color='navy', pad=20)
plt.axis('off')
plt.tight_layout()

plt.show()