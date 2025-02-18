import matplotlib.pyplot as plt
import networkx as nx

# Nodes and their sizes representing departmental data processing capacity in TB
departments = [
    "Security Operations", "Threat Intelligence", "Incident Response", 
    "Vulnerability Management", "Penetration Testing", "Governance", 
    "Compliance", "Forensics", "Data Analytics", "Risk Management"
]
data_capacity = [200, 150, 180, 90, 80, 70, 60, 100, 130, 110]

# Edges representing data transfers in terabytes (TB)
data_transfer = [
    ("Security Operations", "Threat Intelligence", 120),
    ("Security Operations", "Incident Response", 100),
    ("Threat Intelligence", "Vulnerability Management", 80),
    ("Incident Response", "Forensics", 70),
    ("Incident Response", "Penetration Testing", 65),
    ("Vulnerability Management", "Penetration Testing", 50),
    ("Governance", "Compliance", 75),
    ("Compliance", "Forensics", 40),
    ("Forensics", "Governance", 55),
    ("Data Analytics", "Risk Management", 95),
    ("Risk Management", "Security Operations", 85),
    ("Data Analytics", "Incident Response", 60)
]

# Create an undirected graph
G = nx.Graph()
G.add_nodes_from(departments)
G.add_weighted_edges_from(data_transfer)

# Define the positions for better visualization using the spring layout
pos = nx.spring_layout(G, seed=42)

# Different colors for different types of departments
node_colors = ['#D32F2F', '#1976D2', '#388E3C', '#FBC02D', '#8E24AA', '#0288D1', 
               '#C2185B', '#7B1FA2', '#FF5722', '#009688']
node_sizes = [size * 10 for size in data_capacity]

# Set up the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Draw the nodes with their corresponding sizes and colors
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes, alpha=0.8, edgecolors='black')
edge_weights = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edges(G, pos, width=[0.05 * weight for weight in edge_weights.values()], alpha=0.7)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', font_color='darkblue')

# Custom edge labels for data transfer
edge_labels = {(u, v): f"{d['weight']} TB" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='green', font_size=9)

# Title and axis management
plt.title("CyberGuard Pro - Departmental Data Flow Network\nMonthly Data Transfers", fontsize=16, fontweight='bold', color='darkblue', pad=20)
ax.axis('off')

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()