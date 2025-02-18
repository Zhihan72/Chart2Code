import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.patches as mpatches

# Departments
departments = [
    'Biomass Production', 'Astrophysics', 'Energy Systems',
    'Habitats', 'Geology', 'Robotics', 'Communications'
]

# Collaborations
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

# Graph and layout
G = nx.Graph()
G.add_nodes_from(departments)
G.add_edges_from(collaborations)
pos = nx.spring_layout(G, seed=42)

# Node colors and sizes
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

# Draw nodes and edges
for node in G.nodes():
    nx.draw_networkx_nodes(
        G, pos,
        nodelist=[node],
        node_size=node_sizes[node],
        node_color=node_colors[node],
        edgecolors='black',
        node_shape='s'  # Changed node shape from default 'o' to 's'
    )
nx.draw_networkx_edges(
    G, pos, edgelist=collaborations, 
    width=2, edge_color='gray', style='dotted'  # Changed edge style to 'dotted'
)
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

# Title
plt.title(
    "Inter-Departmental Collaborations in Space Colony",
    fontsize=14, fontweight='bold'
)

# Legend
handles = [mpatches.Patch(color=node_colors[node], label=node) for node in node_colors]
plt.legend(handles=handles, loc='lower right', bbox_to_anchor=(1, 0)) # Changed legend position

# Grid (Added)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Layout
plt.axis('off')
plt.tight_layout()

# Show
plt.show()