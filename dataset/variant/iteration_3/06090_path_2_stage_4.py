import matplotlib.pyplot as plt
import networkx as nx

# Adding new nodes and a new agency
nodes = [
    'NASA', 'ESA', 'JAXA', 'Roscosmos', 'CNSA', 'ISRO',
    'New Horizons', 'Mars Rover', 'James Webb Telescope', 'Hubble',
    'Voyager', 'ISS', 'Venus Missions', 'SpaceIL', 'Lunar Mission', 'Comet Probe'
]

# Adding edges that include the new nodes
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
    ('SpaceIL', 'Lunar Mission'),
    ('SpaceIL', 'Comet Probe'), 
    ('NASA', 'Lunar Mission'), 
    ('ESA', 'Comet Probe')
]

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

pos = nx.shell_layout(G)

node_color = '#1f78b4'

# Updated node sizes with new nodes
node_sizes = {
    'NASA': 2500, 'ESA': 2300, 'JAXA': 2100, 'Roscosmos': 2000, 
    'CNSA': 1900, 'ISRO': 1800, 'New Horizons': 1200, 'Mars Rover': 1600, 
    'James Webb Telescope': 1400, 'Hubble': 1500, 'Voyager': 1300, 
    'ISS': 2200, 'Venus Missions': 1100, 'SpaceIL': 1700, 
    'Lunar Mission': 1400, 'Comet Probe': 1300
}

nx.draw_networkx_nodes(
    G, pos, node_size=[node_sizes[node] for node in G.nodes], 
    node_color=node_color, edgecolors='black'
)

nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='gray', style='solid')

nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold')

plt.axis('off')  # Remove axes, including the borders

plt.show()