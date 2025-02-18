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

pos = nx.shell_layout(G)

colors = {'train': '#4682B4', 'metro': '#FF6347'}
node_colors = [colors[hubs[node]] for node in G.nodes()]
node_shapes = {'train': 'o', 'metro': '^'}
node_sizes = {'train': 1500, 'metro': 1200}

node_shape_map = {node: node_shapes[hubs[node]] for node in G.nodes()}

fig, ax = plt.subplots(figsize=(14, 12))
fig.patch.set_facecolor('linen')

for shape in set(node_shapes.values()):
    nx.draw_networkx_nodes(
        G, pos, ax=ax,
        node_size=[node_sizes[hubs[node]] for node in G.nodes() if node_shape_map[node] == shape],
        node_color=[node_colors[idx] for idx, node in enumerate(G.nodes()) if node_shape_map[node] == shape],
        nodelist=[node for node in G.nodes() if node_shape_map[node] == shape],
        node_shape=shape,
        edgecolors='black'
    )

nx.draw_networkx_edges(G, pos, width=2.0, alpha=0.5, edge_color='grey')
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

ax.set_title(
    'Connectivity of Transportation Hubs in Technopolis\nTrain Stations and Metro Stops',
    fontsize=18, fontweight='bold', ha='center', pad=20
)

ax.axis('off')

train_patch = plt.Line2D([0], [0], marker='o', color='w', markersize=10, markerfacecolor=colors['train'],  label='Train Stations')
metro_patch = plt.Line2D([0], [0], marker='^', color='w', markersize=10, markerfacecolor=colors['metro'],  label='Metro Stops')
ax.legend(handles=[train_patch, metro_patch], loc='upper left', fontsize=12, title='Hubs', title_fontsize=14)

plt.tight_layout()
plt.show()