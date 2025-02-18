import matplotlib.pyplot as plt
import networkx as nx

nodes = [
    'NASA', 'ESA', 'JAXA', 'Roscosmos', 'CNSA', 'ISRO',
    'New Horizons', 'Mars Rover', 'James Webb Telescope', 'Hubble',
    'Voyager', 'ISS', 'Venus Missions'
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
]

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

pos = nx.shell_layout(G)

node_color = '#1f78b4'

node_sizes = {
    'NASA': 2500, 'ESA': 2300, 'JAXA': 2100, 'Roscosmos': 2000, 
    'CNSA': 1900, 'ISRO': 1800, 'New Horizons': 1200, 'Mars Rover': 1600, 
    'James Webb Telescope': 1400, 'Hubble': 1500, 'Voyager': 1300, 
    'ISS': 2200, 'Venus Missions': 1100
}

nx.draw_networkx_nodes(
    G, pos, node_size=[node_sizes[node] for node in G.nodes], 
    node_color=node_color, edgecolors='black'
)

nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='gray', style='solid')

nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold')

plt.title(
    "Interstellar Alliance: Networking the Cosmos\nExploring Infinite Horizons",
    fontsize=16, fontweight='bold', pad=20
)
plt.xlabel("Entities: Cosmic Organizations & Explorations | Connections: Joint Ventures", fontsize=12)

plt.axis('off')
plt.tight_layout()
plt.show()