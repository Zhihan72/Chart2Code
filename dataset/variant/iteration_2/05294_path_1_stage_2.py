import matplotlib.pyplot as plt
import networkx as nx

hubs = {
    'Central Station': 'train',
    'East Bus Terminal': 'bus',
    'West Metro Stop': 'metro',
    'North Bus Terminal': 'bus',
    'South Metro Stop': 'metro',
    'West Train Depot': 'train',
    'East Metro Hub': 'metro',
    'North Train Depot': 'train',
}

connections = [
    ('Central Station', 'East Bus Terminal'),
    ('Central Station', 'West Metro Stop'),
    ('East Bus Terminal', 'East Metro Hub'),
    ('West Metro Stop', 'West Train Depot'),
    ('North Bus Terminal', 'North Train Depot'),
    ('South Metro Stop', 'Central Station'),
    ('West Train Depot', 'Central Station'),
    ('East Metro Hub', 'South Metro Stop'),
    ('North Train Depot', 'Central Station'),
]

G = nx.Graph()
G.add_nodes_from(hubs)
G.add_edges_from(connections)

pos = nx.circular_layout(G)

node_color = 'steelblue'  # Single consistent color
node_shapes = {'train': 'v', 'bus': 'D', 'metro': 'h'}
node_sizes = {'train': 1800, 'bus': 1300, 'metro': 1400}

node_shape_map = {node: node_shapes[hubs[node]] for node in G.nodes()}

fig, ax = plt.subplots(figsize=(14, 12))
fig.patch.set_facecolor('whitesmoke')

# Draw nodes with the single consistent color, maintaining shapes and sizes
for shape in set(node_shapes.values()):
    nx.draw_networkx_nodes(
        G, pos, ax=ax,
        node_size=[node_sizes[hubs[node]] for node in G.nodes() if node_shape_map[node] == shape],
        node_color=node_color,  # Use consistent color
        nodelist=[node for node in G.nodes() if node_shape_map[node] == shape],
        node_shape=shape,
        edgecolors='purple'
    )

nx.draw_networkx_edges(G, pos, width=3.0, alpha=0.7, edge_color='darkred', style='dashed')

nx.draw_networkx_labels(G, pos, font_size=13, font_weight='normal', font_color='darkblue')

ax.set_title(
    'Transport Hub Connectivity in Technopolis\nTrain, Bus, and Metro Networks',
    fontsize=20, fontweight='normal', ha='center', pad=25
)

ax.grid(visible=True, linestyle='--', linewidth=0.5)

# Legend removed, since nodes share the same color now

plt.tight_layout()
plt.show()