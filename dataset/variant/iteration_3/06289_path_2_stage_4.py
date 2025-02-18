import matplotlib.pyplot as plt
import networkx as nx

# Nodes and their sizes
departments = [
    "SecOps", "Threat Intel", "IR", 
    "VulMgmt", "Pentest", "Gov", 
    "Comp", "Forensics", "DataAnal", "RiskMgmt"
]
data_capacity = [200, 150, 180, 90, 80, 70, 60, 100, 130, 110]

# Edges representing data transfers
data_transfer = [
    ("SecOps", "Threat Intel", 120),
    ("SecOps", "IR", 100),
    ("Threat Intel", "VulMgmt", 80),
    ("IR", "Forensics", 70),
    ("IR", "Pentest", 65),
    ("VulMgmt", "Pentest", 50),
    ("Gov", "Comp", 75),
    ("Comp", "Forensics", 40),
    ("Forensics", "Gov", 55),
    ("DataAnal", "RiskMgmt", 95),
    ("RiskMgmt", "SecOps", 85),
    ("DataAnal", "IR", 60)
]

# Create an undirected graph
G = nx.Graph()
G.add_nodes_from(departments)
G.add_weighted_edges_from(data_transfer)

# Define positions for visualization
pos = nx.kamada_kawai_layout(G)

# Colors and sizes for the nodes
node_colors = ['#388E3C', '#D32F2F', '#8E24AA', '#1976D2', '#FF5722', '#FBC02D',
               '#009688', '#0288D1', '#7B1FA2', '#C2185B']
node_sizes = [size * 12 for size in data_capacity]

# Set up the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Draw the nodes, edges, and labels
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes, alpha=0.7, edgecolors='gray',)
edge_weights = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edges(G, pos, width=[0.03 * weight for weight in edge_weights.values()], alpha=0.9, style='dotted')
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='light', font_color='purple')

# Custom edge labels
edge_labels = {(u, v): f"{d['weight']} TB" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='orange', font_size=9)

# Title and axis management
plt.title("CyberGuard Network - Data Flow\nMonthly Transfers", fontsize=16, fontweight='regular', color='darkslategray', pad=15)
ax.axis('on')
ax.grid(True)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()