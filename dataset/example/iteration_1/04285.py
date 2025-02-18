import matplotlib.pyplot as plt
import networkx as nx

# Title and Backstory:
# The Fantasy Land Kingdom Governance Hierarchy
# This network graph shows the structure of a fantasy kingdom's governing bodies and their interactions. The kingdom consists of various councils, guilds, and factions that manage different aspects of the land. Each node represents a governing body, and the edges represent the interactions or influence among them.

# Define nodes representing governance bodies in the kingdom
governance_bodies = [
    "Royal Court", "Military Council", "Merchant Guild", "Farmers' Union", "Mages' Council",
    "Knights of Valor", "Thieves' Guild", "Artisan Guild", "Forest Rangers", "Sea Traders", "Clerics' Conclave"
]

# Define relationships (edges) among the governance bodies
interactions = [
    ("Royal Court", "Military Council"),     # Influence
    ("Royal Court", "Merchant Guild"),       # Economic Regulation
    ("Military Council", "Knights of Valor"),# Command
    ("Military Council", "Thieves' Guild"),  # Suppression
    ("Merchant Guild", "Sea Traders"),       # Trade Regulation
    ("Merchant Guild", "Artisan Guild"),     # Support
    ("Farmers' Union", "Artisan Guild"),     # Resource Supply
    ("Mages' Council", "Knights of Valor"),  # Enchantment
    ("Forest Rangers", "Farmers' Union"),    # Protection
    ("Thieves' Guild", "Artisan Guild"),     # Covert Operations 
    ("Clerics' Conclave", "Royal Court"),    # Advising /
    ("Sea Traders", "Royal Court"),          # Trade Influence
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

# Create the graph
kingdom_graph = nx.Graph()
kingdom_graph.add_nodes_from(governance_bodies)
kingdom_graph.add_edges_from(interactions)

# Define positions for nodes using the spring layout for aesthetic balance
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