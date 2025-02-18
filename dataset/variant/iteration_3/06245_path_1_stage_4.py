import matplotlib.pyplot as plt
import networkx as nx

civilizations = ["Indus Valley", "Ancient Greece", "Ancient Rome", "Inca", "Ancient China", "Mesopotamia", "Ancient Egypt"]

connections = [
    ("Ancient Greece", "Ancient Rome", "Barter", 25),
    ("Ancient Rome", "Ancient Egypt", "Combat", 22),
    ("Indus Valley", "Mesopotamia", "Historical Exchange", 15),
    ("Ancient China", "Indus Valley", "Conflict", 10),
    ("Mesopotamia", "Inca", "Cultural Exchange", 14),
    ("Inca", "Ancient China", "Trade", 17),
    ("Indus Valley", "Mesopotamia", "Cultural Exchange", 18),
    ("Mesopotamia", "Ancient Egypt", "Trade", 20)
]

G = nx.DiGraph()
G.add_nodes_from(civilizations)
for src, dst, influence, weight in connections:
    G.add_edge(src, dst, influence=influence, weight=weight)

pos = nx.spring_layout(G, seed=2023)

edges = G.edges(data=True)
edge_weights = [data['weight'] for _, _, data in edges]

node_size = [1000 * (G.degree(civilization) + 1) for civilization in civilizations]
nx.draw_networkx_nodes(G, pos, node_color="#FFD700", node_size=node_size, edgecolors='black', linewidths=1.5)

nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='blue', width=[weight / 5 for weight in edge_weights], arrowstyle='-|>', arrowsize=15)

nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', font_color='darkgreen')

plt.axis('off')
plt.show()