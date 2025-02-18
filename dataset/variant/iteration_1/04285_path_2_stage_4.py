import matplotlib.pyplot as plt
import networkx as nx

governance_bodies = [
    "Royal Court", "Military Council", "Farmers' Union", "Mages' Council",
    "Knights of Valor", "Thieves' Guild", "Forest Rangers", "Clerics' Conclave"
]

interactions = [
    ("Royal Court", "Military Council"),
    ("Farmers' Union", "Knights of Valor"),
    ("Military Council", "Knights of Valor"),
    ("Military Council", "Thieves' Guild"),
    ("Mages' Council", "Knights of Valor"),
    ("Forest Rangers", "Farmers' Union"),
    ("Clerics' Conclave", "Royal Court"),
]

node_categories = {
    "Leadership": ["Royal Court", "Military Council", "Mages' Council"],
    "Defense & Law": ["Knights of Valor", "Thieves' Guild", "Forest Rangers"],
    "Civilians": ["Farmers' Union", "Clerics' Conclave"]
}

colors = {
    "Leadership": 'mediumturquoise',
    "Defense & Law": 'crimson',
    "Civilians": 'darkolivegreen'
}

color_map = []
for body in governance_bodies:
    for category in node_categories:
        if body in node_categories[category]:
            color_map.append(colors[category])

kingdom_graph = nx.Graph()
kingdom_graph.add_nodes_from(governance_bodies)
kingdom_graph.add_edges_from(interactions)

pos = nx.spring_layout(kingdom_graph, seed=21)

plt.figure(figsize=(15, 12))

nx.draw_networkx_nodes(
    kingdom_graph, pos, node_size=2000, node_color=color_map, edgecolors='black', linewidths=1.5, alpha=0.9
)

nx.draw_networkx_edges(
    kingdom_graph, pos, width=2, alpha=0.7, edge_color='grey'
)

plt.axis('off')
plt.tight_layout()
plt.show()