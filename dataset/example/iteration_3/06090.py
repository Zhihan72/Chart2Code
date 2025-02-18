import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Backstory:
# This graph represents the information network of global space agencies and key astronomical discoveries.
# It portrays how various agencies are connected through collaborative missions and shared data, showcasing
# the journey of humanity beyond the stars.

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

# Colors for different types of nodes
node_colors = {
    'NASA': '#1f78b4', 'ESA': '#33a02c', 'JAXA': '#e31a1c', 'Roscosmos': '#ff7f00', 
    'CNSA': '#6a3d9a', 'ISRO': '#b15928', 'New Horizons': '#a6cee3', 'Mars Rover': '#b2df8a', 
    'James Webb Telescope': '#fb9a99', 'Hubble': '#fdbf6f', 'Voyager': '#cab2d6', 
    'ISS': '#ffff99', 'Venus Missions': '#ff88aa'
}

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
    node_color=[node_colors[node] for node in G.nodes], edgecolors='black'
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

# Create legend manually
for label, color in node_colors.items():
    plt.scatter([], [], c=color, label=label, s=100)
plt.legend(loc='upper right', title='Space Agencies & Missions', fontsize=9)

# Remove axis
plt.axis('off')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()