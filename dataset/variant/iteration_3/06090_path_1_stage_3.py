import matplotlib.pyplot as plt
import networkx as nx

nodes = [
    'NASA', 'ESA', 'JAXA', 'Roscosmos', 'CNSA', 'ISRO',
    'New Horizons', 'Mars Rover', 'James Webb Telescope', 'Hubble',
    'Voyager', 'ISS', 'Venus Missions', 'SpaceX', 'Blue Origin', 'Artemis Program'
]

edges = [
    ('NASA', 'ESA'),
    ('NASA', 'JAXA'),
    ('NASA', 'Roscosmos'),
    ('ESA', 'Hubble'),
    ('JAXA', 'CNSA'),
    ('Roscosmos', 'ISS'),
    ('NASA', 'ISS'),
    ('NASA', 'Mars Rover'),
    ('NASA', 'James Webb Telescope'),
    ('ESA', 'James Webb Telescope'),
    ('NASA', 'Voyager'),
    ('ISRO', 'NASA'),
    ('ISRO', 'Venus Missions'),
    ('CNSA', 'Mars Rover'),
    ('JAXA', 'Venus Missions'),
    ('NASA', 'SpaceX'),
    ('NASA', 'Artemis Program'),
    ('SpaceX', 'Blue Origin'),
    ('Blue Origin', 'Artemis Program')
]

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

pos = nx.shell_layout(G)

node_colors = [
    '#1f78b4', '#33a02c', '#e31a1c', '#ff7f00', 
    '#6a3d9a', '#b15928', '#a6cee3', '#b2df8a', 
    '#fb9a99', '#fdbf6f', '#cab2d6', '#ffff99', 
    '#ff88aa', '#7fc97f', '#beaed4', '#fdc086'
]

node_sizes = [
    2500, 2300, 2100, 2000, 
    1900, 1800, 1200, 1600, 
    1400, 1500, 1300, 2200, 
    1100, 1700, 1450, 1250
]

nx.draw_networkx_nodes(
    G, pos, node_size=node_sizes, 
    node_color=node_colors, edgecolors='black'
)

nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='gray', style='solid')

nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold')

plt.axis('off')

plt.tight_layout()

plt.show()