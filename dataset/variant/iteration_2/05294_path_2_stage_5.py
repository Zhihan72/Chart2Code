import matplotlib.pyplot as plt
import networkx as nx

hubs = {
    'Central Base': 'train',
    'Western Hub': 'metro',
    'Southern Checkpoint': 'metro',
    'Western Terminal': 'train',
    'Eastern Node': 'metro',
    'Northern Outpost': 'train',
}

connections = [
    ('Central Base', 'Western Hub'),
    ('Western Hub', 'Western Terminal'),
    ('Southern Checkpoint', 'Central Base'),
    ('Western Terminal', 'Central Base'),
    ('Eastern Node', 'Southern Checkpoint'),
    ('Northern Outpost', 'Central Base'),
]

# Use an undirected graph
G = nx.Graph()
G.add_nodes_from(hubs)
G.add_edges_from(connections)

pos = nx.kamada_kawai_layout(G)

colors = {'train': '#FF4500', 'metro': '#2E8B57'}
node_colors = [colors[hubs[node]] for node in G.nodes()]
node_shapes = {'train': 's', 'metro': 'd'}
node_sizes = {'train': 1600, 'metro': 1100}

node_shape_map = {node: node_shapes[hubs[node]] for node in G.nodes()}

fig, ax = plt.subplots(figsize=(12, 10))
fig.patch.set_facecolor('lightyellow')

for shape in set(node_shapes.values()):
    nx.draw_networkx_nodes(
        G, pos, ax=ax,
        node_size=[node_sizes[hubs[node]] for node in G.nodes() if node_shape_map[node] == shape],
        node_color=[node_colors[idx] for idx, node in enumerate(G.nodes()) if node_shape_map[node] == shape],
        nodelist=[node for node in G.nodes() if node_shape_map[node] == shape],
        node_shape=shape,
        edgecolors='brown'
    )

nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.7, edge_color='purple', style='dotted')
nx.draw_networkx_labels(G, pos, font_size=10, font_color='darkblue', font_weight='light')

ax.set_title(
    'Web of Transport Bases in Geographica\nTrain Points and Metro Nodes',
    fontsize=16, fontweight='normal', ha='right', pad=15
)

ax.axis('equal')

train_patch = plt.Line2D([0], [0], marker='s', color='w', markersize=10, markerfacecolor=colors['train'], label='Train Points')
metro_patch = plt.Line2D([0], [0], marker='d', color='w', markersize=10, markerfacecolor=colors['metro'], label='Metro Nodes')
ax.legend(handles=[train_patch, metro_patch], loc='lower right', fontsize=10, title='Transport Locations', title_fontsize=12)

plt.tight_layout()
plt.show()