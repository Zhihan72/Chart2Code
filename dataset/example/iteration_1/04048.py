import matplotlib.pyplot as plt
import networkx as nx

# Backstory: Exploring the Network of Renewable Energy Sources
# This graph visualizes the network of interconnections among various renewable energy sources and the essential components and technologies that facilitate their generation and distribution.

# Define nodes (Renewable Energy Sources and Components)
nodes = {
    'Solar Panels': 5,
    'Wind Turbines': 4,
    'Hydropower': 3,
    'Geothermal': 2,
    'Biomass': 4,
    'Energy Storage': 6,
    'Grid Distribution': 7,
    'Smart Grids': 5
}

# Define directed edges capturing the flow and connections
edges = {
    ('Solar Panels', 'Energy Storage'): 5,
    ('Wind Turbines', 'Energy Storage'): 4,
    ('Hydropower', 'Grid Distribution'): 6,
    ('Geothermal', 'Grid Distribution'): 4,
    ('Biomass', 'Energy Storage'): 3,
    ('Energy Storage', 'Smart Grids'): 4,
    ('Smart Grids', 'Grid Distribution'): 5,
    ('Solar Panels', 'Grid Distribution'): 2,
    ('Wind Turbines', 'Grid Distribution'): 3,
    ('Biomass', 'Grid Distribution'): 2
}

# Create a directed graph using NetworkX
G = nx.DiGraph()

# Add nodes and edges to the graph
G.add_nodes_from(nodes.keys())
for (start, end), weight in edges.items():
    G.add_edge(start, end, weight=weight)

# Position the nodes using a spring layout for better readability
pos = nx.spring_layout(G, seed=42)

# Create the plot
plt.figure(figsize=(14, 10))

# Nodes: Size and color based on importance
node_sizes = [nodes[node] * 500 for node in G.nodes]
node_colors = [plt.cm.viridis(nodes[node] / max(nodes.values())) for node in G.nodes]

# Draw nodes and edges
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, edgecolors='black', alpha=0.9)
nx.draw_networkx_edges(G, pos, edgelist=edges.keys(), arrowstyle='-|>', arrowsize=15, 
                       width=[w for w in edges.values()], edge_color='gray')

# Draw labels for nodes
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', verticalalignment='center')
nx.draw_networkx_edge_labels(G, pos, edge_labels={edge: f"{weight}" for edge, weight in edges.items()}, font_size=8)

# Add a color bar for node significance
sm = plt.cm.ScalarMappable(cmap=plt.cm.viridis, norm=plt.Normalize(vmin=min(nodes.values()), vmax=max(nodes.values())))
sm._A = []
cbar = plt.colorbar(sm, ax=plt.gca(), shrink=0.8)  # Specify the current axes for the color bar
cbar.set_label('Node Importance', rotation=270, labelpad=20)

# Add a concise, multi-line title
plt.title("Interconnections Among Renewable Energy Sources\nand the Role of Critical Components and Technologies", fontsize=16, fontweight='bold')

# Adjust layout
plt.axis('off')
plt.tight_layout()

# Show the plot
plt.show()