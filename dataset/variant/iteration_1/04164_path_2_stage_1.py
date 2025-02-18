import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.patches as mpatches

# Define the departments
departments = [
    'Biomass Production', 'Astrophysics', 'Energy Systems',
    'Habitats', 'Geology', 'Robotics', 'Communications'
]

# Define collaborations as edges between departments
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

# Create an undirected graph and add nodes and edges
G = nx.Graph()
G.add_nodes_from(departments)
G.add_edges_from(collaborations)

# Assign positions for visualization
pos = nx.spring_layout(G, seed=42)

# Define node colors and sizes
node_colors = {
    'Biomass Production': '#5B9BD5',
    'Astrophysics': '#ED7D31',
    'Energy Systems': '#A5A5A5',
    'Habitats': '#FFC000',
    'Geology': '#4472C4',
    'Robotics': '#70AD47',
    'Communications': '#255E91'
}
node_sizes = {
    'Biomass Production': 2000,
    'Astrophysics': 1500,
    'Energy Systems': 1800,
    'Habitats': 1600,
    'Geology': 1700,
    'Robotics': 1500,
    'Communications': 1400
}

# Draw the graph
for node in G.nodes():
    nx.draw_networkx_nodes(
        G, pos,
        nodelist=[node],
        node_size=node_sizes[node],
        node_color=node_colors[node],
        edgecolors='black'
    )
nx.draw_networkx_edges(G, pos, edgelist=collaborations, width=2, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

# Add a title
plt.title(
    "Inter-Departmental Collaborations in Space Colony",
    fontsize=14, fontweight='bold'
)

# Add legend for node colors
handles = [mpatches.Patch(color=node_colors[node], label=node) for node in node_colors]
plt.legend(handles=handles, loc='upper left', bbox_to_anchor=(1, 1))

# Customize the layout
plt.axis('off')
plt.tight_layout()

# Show plot
plt.show()