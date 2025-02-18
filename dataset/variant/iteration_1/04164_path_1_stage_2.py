import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import matplotlib.patches as mpatches

departments = [
    'Biomass Production', 'Astrophysics', 'Energy Systems',
    'Habitats', 'Geology', 'Robotics', 'Communications'
]

collaborations = [
    ('Biomass Production', 'Geology'),
    ('Habitats', 'Robotics'),
    ('Astrophysics', 'Communications'),
    ('Habitats', 'Geology'),
    ('Energy Systems', 'Robotics')
]

G = nx.Graph()
G.add_nodes_from(departments)
G.add_edges_from(collaborations)

pos = nx.spring_layout(G, seed=42)

node_colors = {
    'Biomass Production': '#DA70D6',
    'Astrophysics': '#4682B4',
    'Energy Systems': '#32CD32',
    'Habitats': '#FF6347',
    'Geology': '#9ACD32',
    'Robotics': '#FFD700',
    'Communications': '#FF4500'
}
node_sizes = {
    'Biomass Production': 1700,
    'Astrophysics': 2500,
    'Energy Systems': 1500,
    'Habitats': 2000,
    'Geology': 1300,
    'Robotics': 1800,
    'Communications': 1600
}
node_shapes = {
    'Biomass Production': 'o',
    'Astrophysics': 'p',
    'Energy Systems': '*',
    'Habitats': 's',
    'Geology': '^',
    'Robotics': 'd',
    'Communications': 'H'
}

for node in G.nodes():
    nx.draw_networkx_nodes(
        G, pos,
        nodelist=[node],
        node_size=node_sizes[node],
        node_color=node_colors[node],
        edgecolors='black',
        node_shape=node_shapes[node]
    )

edge_styles = {
    ('Biomass Production', 'Geology'): 'solid',
    ('Habitats', 'Robotics'): 'dashed',
    ('Astrophysics', 'Communications'): 'dotted',
    ('Habitats', 'Geology'): 'dashed',
    ('Energy Systems', 'Robotics'): 'solid'
}

for edge in G.edges():
    if edge not in edge_styles.keys():
        continue
    nx.draw_networkx_edges(
        G, pos,
        edgelist=[edge],
        style=edge_styles[edge],
        width=2.5,
        edge_color='dimgray'
    )

nx.draw_networkx_labels(G, pos, font_size=12, font_family='serif')

plt.title(
    "Space Colony Department Collaborations\nExploring Project Connections",
    fontsize=16, fontweight='bold'
)

handles = [mpatches.Patch(color=node_colors[node], label=node) for node in node_colors]
plt.legend(handles=handles, loc='upper right', bbox_to_anchor=(1.2, 1.1))

plt.grid(True)
plt.axis('on')
plt.tick_params(left=False, labelleft=False, bottom=False, labelbottom=False)
plt.tight_layout()

plt.show()