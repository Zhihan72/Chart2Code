import matplotlib.pyplot as plt
import networkx as nx

# Backstory:
# The city of Technopolis is known for its advanced interconnected public transportation system.
# We are visualizing the connectivity between different transportation hubs in Technopolis, including train stations, bus terminals, and metro stops.
# This graph will show the connections and how residents can travel from one hub to another seamlessly.

# Define the transportation hubs (nodes)
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

# Define the connections between hubs (edges)
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

# Create the graph
G = nx.Graph()
G.add_nodes_from(hubs)
G.add_edges_from(connections)

# Define positions using a shell layout
pos = nx.shell_layout(G)

# Node attributes
colors = {'train': '#FF6347', 'bus': '#4682B4', 'metro': '#32CD32'}
node_colors = [colors[hubs[node]] for node in G.nodes()]
node_shapes = {'train': 'o', 'bus': 's', 'metro': '^'}
node_sizes = {'train': 1500, 'bus': 1000, 'metro': 1200}

# Map shapes to node types
node_shape_map = {node: node_shapes[hubs[node]] for node in G.nodes()}

# Create figure and axes
fig, ax = plt.subplots(figsize=(14, 12))
fig.patch.set_facecolor('linen')

# Draw nodes with different shapes
for shape in set(node_shapes.values()):
    nx.draw_networkx_nodes(
        G, pos, ax=ax,
        node_size=[node_sizes[hubs[node]] for node in G.nodes() if node_shape_map[node] == shape],
        node_color=[node_colors[idx] for idx, node in enumerate(G.nodes()) if node_shape_map[node] == shape],
        nodelist=[node for node in G.nodes() if node_shape_map[node] == shape],
        node_shape=shape,
        edgecolors='black'
    )

# Draw edges
nx.draw_networkx_edges(G, pos, width=2.0, alpha=0.5, edge_color='grey')

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

# Set title with line breaks for clarity
ax.set_title(
    'Connectivity of Transportation Hubs in Technopolis\nTrain Stations, Bus Terminals, and Metro Stops',
    fontsize=18, fontweight='bold', ha='center', pad=20
)

# Remove axis
ax.axis('off')

# Add a legend manually
train_patch = plt.Line2D([0], [0], marker='o', color='w', markersize=10, markerfacecolor=colors['train'],  label='Train Stations')
bus_patch = plt.Line2D([0], [0], marker='s', color='w', markersize=10, markerfacecolor=colors['bus'],  label='Bus Terminals')
metro_patch = plt.Line2D([0], [0], marker='^', color='w', markersize=10, markerfacecolor=colors['metro'],  label='Metro Stops')
ax.legend(handles=[train_patch, bus_patch, metro_patch], loc='upper left', fontsize=12, title='Hubs', title_fontsize=14)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()