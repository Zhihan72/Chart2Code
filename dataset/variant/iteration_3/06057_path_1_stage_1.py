import matplotlib.pyplot as plt
import networkx as nx

# Nodes with activities
nodes = [
    "Health Checkup", "Art Exhibition", "Food Stall",
    "Storytelling Corner", "Eco Workshop", "Games Stall",
    "Info Booth", "Crafts Stall", "Music Stage"
]

# Randomly altered edges and their weights
edges = [
    ("Music Stage", "Eco Workshop", 10),
    ("Games Stall", "Art Exhibition", 22),
    ("Crafts Stall", "Games Stall", 15),
    ("Info Booth", "Eco Workshop", 20),
    ("Health Checkup", "Crafts Stall", 5),
    ("Storytelling Corner", "Food Stall", 50),
    ("Art Exhibition", "Music Stage", 18),
    ("Food Stall", "Games Stall", 8),
    ("Food Stall", "Crafts Stall", 30),
    ("Eco Workshop", "Storytelling Corner", 25),
    ("Health Checkup", "Music Stage", 40),
    ("Games Stall", "Info Booth", 12),
    ("Info Booth", "Art Exhibition", 14)
]

# Create graph
G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

# Layout and colors
pos = nx.spring_layout(G, seed=42)
node_colors = ['plum', 'peachpuff', 'salmon', 'orchid', 'aquamarine', 'lightblue', 'lightgrey', 'khaki', 'lightgreen']
node_sizes = [700 + 150 * G.degree(node) for node in G.nodes]

# Draw nodes, edges, labels
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, edgecolors='black')
nx.draw_networkx_edges(G, pos, edgelist=edges, arrowstyle='-|>', arrowsize=15, edge_color='grey')
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
edge_labels = {(u, v): f"{w} visitors" for u, v, w in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, label_pos=0.3)

# Title and display settings
plt.title("Greenfield Community Festival:\nVisitor Interactions Between Stalls", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.axis('off')
plt.show()