import matplotlib.pyplot as plt
import networkx as nx

# Define nodes representing governance bodies in the kingdom
governance_bodies = [
    "Royal Court", "Military Council", "Merchant Guild", "Farmers' Union", "Mages' Council",
    "Knights of Valor", "Thieves' Guild", "Artisan Guild", "Forest Rangers", "Sea Traders", "Clerics' Conclave"
]

# Define relationships (edges) among the governance bodies as undirected
interactions = [
    ("Royal Court", "Military Council"),
    ("Royal Court", "Merchant Guild"),
    ("Military Council", "Knights of Valor"),
    ("Military Council", "Thieves' Guild"),
    ("Merchant Guild", "Sea Traders"),
    ("Merchant Guild", "Artisan Guild"),
    ("Farmers' Union", "Artisan Guild"),
    ("Mages' Council", "Knights of Valor"),
    ("Forest Rangers", "Farmers' Union"),
    ("Thieves' Guild", "Artisan Guild"),
    ("Clerics' Conclave", "Royal Court"),
    ("Sea Traders", "Royal Court"),
]

# Classify nodes by categories for visualization
node_categories = {
    "Leadership": ["Royal Court", "Military Council", "Mages' Council"],
    "Trade & Craftsmanship": ["Merchant Guild", "Sea Traders", "Artisan Guild"],
    "Defense & Law": ["Knights of Valor", "Thieves' Guild", "Forest Rangers"],
    "Civilians": ["Farmers' Union", "Clerics' Conclave"]
}

# Assign colors to nodes based on their categories
colors = {
    "Leadership": 'royalblue',
    "Trade & Craftsmanship": 'darkorange',
    "Defense & Law": 'darkred',
    "Civilians": 'forestgreen'
}

# Map colors to nodes
color_map = []
for body in governance_bodies:
    for category in node_categories:
        if body in node_categories[category]:
            color_map.append(colors[category])

# Create undirected graph
kingdom_graph = nx.Graph()
kingdom_graph.add_nodes_from(governance_bodies)
kingdom_graph.add_edges_from(interactions)

# Define positions for nodes using spring layout
pos = nx.spring_layout(kingdom_graph, seed=21)

# Initialize plot
plt.figure(figsize=(15, 12))

# Draw nodes with specified size and color
nx.draw_networkx_nodes(
    kingdom_graph, pos, node_size=2000, node_color=color_map, edgecolors='black', linewidths=1.5, alpha=0.9
)

# Draw edges
nx.draw_networkx_edges(
    kingdom_graph, pos, width=2, alpha=0.7, edge_color='grey'
)

# Draw labels for the nodes
nx.draw_networkx_labels(
    kingdom_graph, pos, font_size=12, font_weight='bold', font_color='white'
)

# Create a custom legend
legend_handles = [
    plt.Line2D([0], [0], marker='o', color='w', label='Leadership', markersize=10, markerfacecolor='royalblue'),
    plt.Line2D([0], [0], marker='o', color='w', label='Trade & Craftsmanship', markersize=10, markerfacecolor='darkorange'),
    plt.Line2D([0], [0], marker='o', color='w', label='Defense & Law', markersize=10, markerfacecolor='darkred'),
    plt.Line2D([0], [0], marker='o', color='w', label='Civilians', markersize=10, markerfacecolor='forestgreen')
]

# Add the legend to the plot
plt.legend(handles=legend_handles, loc='upper right', fontsize=12, frameon=True, shadow=True)

# Set the title of the plot
plt.title("Fantasy Land Kingdom Governance Hierarchy", fontsize=20, fontweight='bold', pad=20)

# Hide axes for a cleaner look
plt.axis('off')

# Display the plot
plt.tight_layout()
plt.show()