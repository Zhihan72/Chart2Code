import matplotlib.pyplot as plt
import networkx as nx

# Define space agencies and key astronomical discoveries as nodes
nodes = [
    'NASA', 'ESA', 'JAXA', 'Roscosmos', 'CNSA', 'ISRO',
    'New Horizons', 'Mars Rover', 'James Webb Telescope', 'Hubble',
    'Voyager', 'ISS', 'Venus Missions'
]

# Define their relationships (edges) based on collaboration and shared missions
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

# Create the graph
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Position the nodes using a shell layout
pos = nx.shell_layout(G)

# Use a single consistent color for all nodes
node_color = '#1f78b4'

# Sizes for different nodes based on their significance in the space community
node_sizes = {
    'NASA': 2500, 'ESA': 2300, 'JAXA': 2100, 'Roscosmos': 2000, 
    'CNSA': 1900, 'ISRO': 1800, 'New Horizons': 1200, 'Mars Rover': 1600, 
    'James Webb Telescope': 1400, 'Hubble': 1500, 'Voyager': 1300, 
    'ISS': 2200, 'Venus Missions': 1100
}

# Draw nodes
nx.draw_networkx_nodes(
    G, pos, node_size=[node_sizes[node] for node in G.nodes], 
    node_color=node_color, edgecolors='black'
)

# Draw edges
nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='gray', style='solid')

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold')

# Title and labels
plt.title(
    "Global Space Agencies: Collaborative Network and Discoveries\nA Journey Beyond the Stars",
    fontsize=16, fontweight='bold', pad=20
)
plt.xlabel("Nodes: Space Agencies and Missions | Edges: Collaborations", fontsize=12)

# Remove axis
plt.axis('off')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()