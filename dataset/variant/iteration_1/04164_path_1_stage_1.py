import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import matplotlib.patches as mpatches

# Define the departments
departments = [
    'Biomass Production', 'Astrophysics', 'Energy Systems',
    'Habitats', 'Geology', 'Robotics', 'Communications'
]

# Define collaborations as edges
collaborations = [
    ('Biomass Production', 'Astrophysics'),
    ('Biomass Production', 'Energy Systems'),
    ('Biomass Production', 'Habitats'),
    ('Astrophysics', 'Geology'),
    ('Energy Systems', 'Habitats'),
    ('Geology', 'Robotics'),
    ('Geology', 'Habitats'),
    ('Communications', 'Robotics'),
    ('Energy Systems', 'Communications')
]

# Create graph and add nodes and edges
G = nx.Graph()
G.add_nodes_from(departments)
G.add_edges_from(collaborations)

# Assign positions to nodes
pos = nx.spring_layout(G, seed=42)

# Define node colors and sizes
node_colors = {
    'Biomass Production': '#FF6347',  # Changed color
    'Astrophysics': '#4682B4',        # Changed color
    'Energy Systems': '#9ACD32',      # Changed color
    'Habitats': '#DA70D6',            # Changed color
    'Geology': '#FF4500',             # Changed color
    'Robotics': '#32CD32',            # Changed color
    'Communications': '#FFD700'       # Changed color
}
node_sizes = {
    'Biomass Production': 2500,       # Changed size
    'Astrophysics': 1300,             # Changed size
    'Energy Systems': 2000,           # Changed size
    'Habitats': 1800,                 # Changed size
    'Geology': 1600,                  # Changed size
    'Robotics': 1700,                 # Changed size
    'Communications': 1500            # Changed size
}
node_shapes = {
    'Biomass Production': 'd',        # Changed shape
    'Astrophysics': 'o',              # Changed shape
    'Energy Systems': 's',            # Changed shape
    'Habitats': '^',                  # Changed shape
    'Geology': 'p',                   # Changed shape
    'Robotics': 'H',                  # Changed shape
    'Communications': '*'             # Changed shape
}

# Draw nodes
for node in G.nodes():
    nx.draw_networkx_nodes(
        G, pos,
        nodelist=[node],
        node_size=node_sizes[node],
        node_color=node_colors[node],
        edgecolors='black',
        node_shape=node_shapes[node]
    )

# Define edge styles
edge_styles = {
    ('Biomass Production', 'Astrophysics'): 'solid',   # Changed style
    ('Biomass Production', 'Energy Systems'): 'dashed', # Changed style
    ('Biomass Production', 'Habitats'): 'solid',       # Changed style
    ('Astrophysics', 'Geology'): 'dotted',             # Changed style
    ('Energy Systems', 'Habitats'): 'solid',           # Changed style
    ('Geology', 'Robotics'): 'dashed',                 # Changed style
    ('Geology', 'Habitats'): 'dotted',                 # Changed style
    ('Communications', 'Robotics'): 'solid',           # Changed style
    ('Energy Systems', 'Communications'): 'dashed'     # Changed style
}

# Draw edges
for edge in G.edges():
    if edge not in edge_styles.keys():
        continue
    nx.draw_networkx_edges(
        G, pos,
        edgelist=[edge],
        style=edge_styles[edge],
        width=2.5,                     # Changed width
        edge_color='dimgray'           # Changed color
    )

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=12, font_family='serif')  # Changed font

# Add a title
plt.title(
    "Space Colony Department Collaborations\nExploring Project Connections",
    fontsize=16, fontweight='bold'
)

# Add legend for node colors
handles = [mpatches.Patch(color=node_colors[node], label=node) for node in node_colors]
plt.legend(handles=handles, loc='upper right', bbox_to_anchor=(1.2, 1.1))  # Changed position

# Customize the layout
plt.grid(True)  # Added grid
plt.axis('on')  # Displayed axis
plt.tick_params(left=False, labelleft=False, bottom=False, labelbottom=False)  # Removed ticks
plt.tight_layout()

# Show plot
plt.show()