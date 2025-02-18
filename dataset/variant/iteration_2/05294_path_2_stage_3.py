import matplotlib.pyplot as plt
import networkx as nx

hubs = {
    'Central Station': 'train',
    'West Metro Stop': 'metro',
    'South Metro Stop': 'metro',
    'West Train Depot': 'train',
    'East Metro Hub': 'metro',
    'North Train Depot': 'train',
}

connections = [
    ('Central Station', 'West Metro Stop'),
    ('West Metro Stop', 'West Train Depot'),
    ('South Metro Stop', 'Central Station'),
    ('West Train Depot', 'Central Station'),
    ('East Metro Hub', 'South Metro Stop'),
    ('North Train Depot', 'Central Station'),
]

G = nx.Graph()
G.add_nodes_from(hubs)
G.add_edges_from(connections)

pos = nx.kamada_kawai_layout(G)

colors = {'train': '#FF4500', 'metro': '#2E8B57'}
node_colors = [colors[hubs[node]] for node in G.nodes()]
node_shapes = {'train': 's', 'metro': 'd'}  # Changed shapes: square and diamond
node_sizes = {'train': 1600, 'metro': 1100}

node_shape_map = {node: node_shapes[hubs[node]] for node in G.nodes()}

fig, ax = plt.subplots(figsize=(12, 10))
fig.patch.set_facecolor('ivory')

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
    'Connectivity of Transportation Hubs in Technopolis\nTrain Stations and Metro Stops',
    fontsize=16, fontweight='normal', ha='right', pad=15
)

ax.axis(True)

train_patch = plt.Line2D([0], [0], marker='s', color='w', markersize=10, markerfacecolor=colors['train'], label='Train Stations')
metro_patch = plt.Line2D([0], [0], marker='d', color='w', markersize=10, markerfacecolor=colors['metro'], label='Metro Stops')
ax.legend(handles=[train_patch, metro_patch], loc='lower right', fontsize=10, title='Transportation Hubs', title_fontsize=12)

plt.tight_layout()
plt.show()