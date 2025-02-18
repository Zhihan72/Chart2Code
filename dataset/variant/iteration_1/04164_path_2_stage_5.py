import matplotlib.pyplot as plt
import networkx as nx

departments = [
    'Habitats', 'Astrophysics', 'Energy Systems',
    'Biomass Production', 'Geology', 'Robotics', 'Communications'
]

collaborations = [
    ('Habitats', 'Astrophysics'), ('Biomass Production', 'Astrophysics'),
    ('Energy Systems', 'Habitats'), ('Geology', 'Biomass Production'),
    ('Astrophysics', 'Robotics'), ('Geology', 'Habitats'),
    ('Robotics', 'Energy Systems'), ('Communications', 'Astrophysics'),
    ('Energy Systems', 'Communications')
]

G = nx.Graph()
G.add_nodes_from(departments)
G.add_edges_from(collaborations)
pos = nx.spring_layout(G, seed=42)

node_colors = {
    'Habitats': '#FF5733', 'Astrophysics': '#33FFBD',
    'Energy Systems': '#3380FF', 'Biomass Production': '#D433FF',
    'Geology': '#FF33F6', 'Robotics': '#33FF57',
    'Communications': '#FFBD33'
}
node_sizes = {
    'Habitats': 1800, 'Astrophysics': 1500,
    'Energy Systems': 2000, 'Biomass Production': 1600,
    'Geology': 1400, 'Robotics': 1700, 'Communications': 1500
}

for node in G.nodes():
    nx.draw_networkx_nodes(
        G, pos,
        nodelist=[node],
        node_size=node_sizes[node],
        node_color=node_colors[node],
        edgecolors='black',
        node_shape='s'
    )
nx.draw_networkx_edges(
    G, pos, edgelist=collaborations,
    width=2, edge_color='gray', style='dotted'
)

plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.axis('off')
plt.tight_layout()

plt.show()