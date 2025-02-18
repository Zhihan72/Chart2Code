import matplotlib.pyplot as plt
import networkx as nx

nodes = [
    "Checkup", "Art", "Food",
    "Story", "Eco", "Games",
    "Info", "Crafts", "Music"
]

edges = [
    ("Music", "Eco", 10),
    ("Games", "Art", 22),
    ("Crafts", "Games", 15),
    ("Info", "Eco", 20),
    ("Checkup", "Crafts", 5),
    ("Story", "Food", 50),
    ("Art", "Music", 18),
    ("Food", "Games", 8),
    ("Food", "Crafts", 30),
    ("Eco", "Story", 25),
    ("Checkup", "Music", 40),
    ("Games", "Info", 12),
    ("Info", "Art", 14)
]

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

pos = nx.spring_layout(G, seed=42)
node_color = 'lightblue'  # Changed to a single color
node_sizes = [700 + 150 * G.degree(node) for node in G.nodes]

nx.draw_networkx_nodes(
    G, pos, node_size=node_sizes, node_color=node_color,
    edgecolors='darkblue', linewidths=2, alpha=0.7
)
nx.draw_networkx_edges(
    G, pos, edgelist=edges,
    edge_color='darkgrey', style='dotted', alpha=0.8
)
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif', font_color='navy')
edge_labels = {(u, v): f"{w}" for u, v, w in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, label_pos=0.5)

plt.title("Visitor Interactions", fontsize=16, fontweight='bold', color='darkgreen')
plt.tight_layout()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()