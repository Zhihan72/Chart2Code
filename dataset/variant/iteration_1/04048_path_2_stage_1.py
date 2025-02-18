import matplotlib.pyplot as plt
import networkx as nx

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

G = nx.DiGraph()
G.add_nodes_from(nodes.keys())
for (start, end), weight in edges.items():
    G.add_edge(start, end, weight=weight)

pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(14, 10))

# Nodes: Size and color based on importance
node_sizes = [nodes[node] * 500 for node in G.nodes]
node_colors = [plt.cm.plasma(nodes[node] / max(nodes.values())) for node in G.nodes]

nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, edgecolors='black', alpha=0.9)
nx.draw_networkx_edges(G, pos, edgelist=edges.keys(), arrowstyle='-|>', arrowsize=15,
                       width=[w for w in edges.values()], edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', verticalalignment='center')
nx.draw_networkx_edge_labels(G, pos, edge_labels={edge: f"{weight}" for edge, weight in edges.items()}, font_size=8)

# Add a color bar for node significance
sm = plt.cm.ScalarMappable(cmap=plt.cm.plasma, norm=plt.Normalize(vmin=min(nodes.values()), vmax=max(nodes.values())))
sm._A = []
cbar = plt.colorbar(sm, ax=plt.gca(), shrink=0.8)
cbar.set_label('Node Importance', rotation=270, labelpad=20)

plt.title("Interconnections Among Renewable Energy Sources\nand the Role of Critical Components and Technologies", fontsize=16, fontweight='bold')
plt.axis('off')
plt.tight_layout()
plt.show()