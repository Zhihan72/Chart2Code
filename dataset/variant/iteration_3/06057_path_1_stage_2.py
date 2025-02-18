import matplotlib.pyplot as plt
import networkx as nx

nodes = [
    "Health Checkup", "Art Exhibition", "Food Stall",
    "Storytelling Corner", "Eco Workshop", "Games Stall",
    "Info Booth", "Crafts Stall", "Music Stage"
]

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

G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

pos = nx.spring_layout(G, seed=42)
node_colors = ['lightblue', 'peachpuff', 'lightgreen', 'aquamarine', 'khaki', 'salmon', 'orchid', 'lightgrey', 'plum']
node_sizes = [700 + 150 * G.degree(node) for node in G.nodes]

nx.draw_networkx_nodes(
    G, pos, node_size=node_sizes, node_color=node_colors,
    edgecolors='darkblue', linewidths=2, alpha=0.7
)
nx.draw_networkx_edges(
    G, pos, edgelist=edges, arrowstyle='-|>', arrowsize=20,
    edge_color='darkgrey', style='dotted', alpha=0.8
)
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif', font_color='navy')
edge_labels = {(u, v): f"{w} visits" for u, v, w in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, label_pos=0.5)

plt.title("Greenfield Community Festival:\nVisitor Interactions Between Stalls", fontsize=16, fontweight='bold', color='darkgreen')
plt.tight_layout()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()