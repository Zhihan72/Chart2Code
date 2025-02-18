import matplotlib.pyplot as plt
import networkx as nx

governance_bodies = [
    "Majestic Court", "Defense Council", "Commerce Guild", "Peasants' League", "Sorcery Council",
    "Valorous Knights", "Guild of Shadows", "Creative Guild", "Woodland Watchers", "Ocean Merchants", "Temple Assembly"
]

interactions = [
    ("Majestic Court", "Defense Council"),
    ("Majestic Court", "Commerce Guild"),
    ("Defense Council", "Valorous Knights"),
    ("Defense Council", "Guild of Shadows"),
    ("Commerce Guild", "Ocean Merchants"),
    ("Commerce Guild", "Creative Guild"),
    ("Peasants' League", "Creative Guild"),
    ("Sorcery Council", "Valorous Knights"),
    ("Woodland Watchers", "Peasants' League"),
    ("Guild of Shadows", "Creative Guild"),
    ("Temple Assembly", "Majestic Court"),
    ("Ocean Merchants", "Majestic Court"),
]

colors = {
    "Leaders": 'forestgreen',
    "Commerce & Artisans": 'royalblue',
    "Protection & Order": 'darkorange',
    "Citizens": 'darkred'
}

node_categories = {
    "Leaders": ["Sorcery Council", "Defense Council", "Majestic Court"],
    "Commerce & Artisans": ["Creative Guild", "Commerce Guild", "Ocean Merchants"],
    "Protection & Order": ["Guild of Shadows", "Woodland Watchers", "Valorous Knights"],
    "Citizens": ["Temple Assembly", "Peasants' League"]
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

nx.draw_networkx_labels(
    kingdom_graph, pos, font_size=12, font_weight='bold', font_color='white'
)

plt.title("Kingdom Hierarchy of Fantasy Realm", fontsize=20, fontweight='bold', pad=20)

plt.axis('off')

plt.tight_layout()
plt.show()