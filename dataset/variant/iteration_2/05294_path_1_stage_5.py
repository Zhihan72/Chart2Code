import matplotlib.pyplot as plt
import networkx as nx

hubs = {
    'Central': 'train',
    'East Bus': 'bus',
    'West Metro': 'metro',
    'North Bus': 'bus',
    'South Metro': 'metro',
    'West Train': 'train',
    'East Metro': 'metro',
    'North Train': 'train',
    'Tech Park': 'train',
    'City Center': 'bus',
    'Innovation': 'metro',
}

connections = [
    ('Central', 'East Bus'),
    ('Central', 'West Metro'),
    ('East Bus', 'East Metro'),
    ('West Metro', 'West Train'),
    ('North Bus', 'North Train'),
    ('South Metro', 'Central'),
    ('West Train', 'Central'),
    ('East Metro', 'South Metro'),
    ('North Train', 'Central'),
    ('Tech Park', 'Innovation'),
    ('City Center', 'Innovation'),
    ('City Center', 'North Bus'),
]

G = nx.Graph()
G.add_nodes_from(hubs)
G.add_edges_from(connections)

pos = nx.circular_layout(G)

node_color = 'steelblue'
node_shapes = {'train': 'v', 'bus': 'D', 'metro': 'h'}
node_sizes = {'train': 1800, 'bus': 1300, 'metro': 1400}

node_shape_map = {node: node_shapes[hubs[node]] for node in G.nodes()}

fig, ax = plt.subplots(figsize=(14, 12))
fig.patch.set_facecolor('whitesmoke')

for shape in set(node_shapes.values()):
    nx.draw_networkx_nodes(
        G, pos, ax=ax,
        node_size=[node_sizes[hubs[node]] for node in G.nodes() if node_shape_map[node] == shape],
        node_color=node_color,
        nodelist=[node for node in G.nodes() if node_shape_map[node] == shape],
        node_shape=shape,
        edgecolors='purple'
    )

nx.draw_networkx_edges(G, pos, width=3.0, alpha=0.7, edge_color='darkred', style='dashed')

nx.draw_networkx_labels(G, pos, font_size=13, font_weight='normal', font_color='darkblue')

ax.set_title(
    'Hub Connectivity in Technopolis\nTrain, Bus & Metro',
    fontsize=20, fontweight='normal', ha='center', pad=25
)

ax.grid(visible=True, linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.show()