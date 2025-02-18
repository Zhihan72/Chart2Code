import matplotlib.pyplot as plt
import networkx as nx

nodes = [
    'Moon Mission', 'Planetary Explorers', 'Galactic Observers', 'Astro Agencies', 'Space Union', 'Satellite Squad',
    'Deep Space Probe', 'Martian Crawler', 'Cosmic Eye', 'Past Explorer',
    'Interstellar Voyager', 'Orbiting Lab', 'Venus Expeditors', 'Private Pioneers', 'Suborbital Shifters', 'Lunar Quest'
]

edges = [
    ('Moon Mission', 'Planetary Explorers'),
    ('Moon Mission', 'Galactic Observers'),
    ('Moon Mission', 'Astro Agencies'),
    ('Planetary Explorers', 'Past Explorer'),
    ('Galactic Observers', 'Space Union'),
    ('Astro Agencies', 'Orbiting Lab'),
    ('Moon Mission', 'Orbiting Lab'),
    ('Moon Mission', 'Martian Crawler'),
    ('Moon Mission', 'Cosmic Eye'),
    ('Planetary Explorers', 'Cosmic Eye'),
    ('Moon Mission', 'Interstellar Voyager'),
    ('Satellite Squad', 'Moon Mission'),
    ('Satellite Squad', 'Venus Expeditors'),
    ('Space Union', 'Martian Crawler'),
    ('Galactic Observers', 'Venus Expeditors'),
    ('Moon Mission', 'Private Pioneers'),
    ('Moon Mission', 'Lunar Quest'),
    ('Private Pioneers', 'Suborbital Shifters'),
    ('Suborbital Shifters', 'Lunar Quest')
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