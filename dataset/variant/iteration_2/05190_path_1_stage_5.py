import matplotlib.pyplot as plt
import networkx as nx

regions = ['North', 'South', 'East', 'West', 'Cntrl', 'High', 'Low']

regional_connections = [
    ('North', 'South'),
    ('South', 'East'),
    ('East', 'West'),
    ('West', 'Cntrl'),
    ('Cntrl', 'High'),
    ('High', 'Low'),
    ('Low', 'North')
]

G = nx.Graph()

G.add_nodes_from(regions)
G.add_edges_from(regional_connections)

fig, ax = plt.subplots(1, 2, figsize=(14, 8))

pos = nx.spring_layout(G, seed=42)

nx.draw(G, pos, ax=ax[0], with_labels=True, node_color='lightblue', edge_color='grey', node_size=2000, font_weight='bold')
ax[0].set_title('Region Graph', fontsize=14, fontweight='bold')

nx.draw(G, pos, ax=ax[1], with_labels=True, node_color='lightgreen', edge_color='grey', node_size=2000, font_weight='bold')
ax[1].set_title('Connections', fontsize=14, fontweight='bold')

fig.suptitle('Region & Demographics', fontsize=18, fontweight='bold', y=0.98)
plt.tight_layout()
plt.show()