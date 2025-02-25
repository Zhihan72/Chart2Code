import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Nodes (Authors) and edges (Influences)
authors = [
    "Isaac Asimov", "Arthur C. Clarke", "Philip K. Dick", "H.G. Wells",
    "Jules Verne", "Frank Herbert", "Ursula K. Le Guin", "Ray Bradbury",
    "William Gibson", "Neal Stephenson", "Robert A. Heinlein", "Orson Scott Card"
]

influences = [
    ("Jules Verne", "H.G. Wells"),
    ("H.G. Wells", "Isaac Asimov"),
    ("Isaac Asimov", "Arthur C. Clarke"),
    ("Isaac Asimov", "Philip K. Dick"),
    ("Arthur C. Clarke", "Frank Herbert"),
    ("Philip K. Dick", "William Gibson"),
    ("Frank Herbert", "Ursula K. Le Guin"),
    ("Ray Bradbury", "William Gibson"),
    ("William Gibson", "Neal Stephenson"),
    ("Ursula K. Le Guin", "Orson Scott Card"),
    ("Robert A. Heinlein", "Orson Scott Card"),
    ("Arthur C. Clarke", "Neal Stephenson")
]

G = nx.DiGraph()
G.add_edges_from(influences)
pos = nx.spring_layout(G, seed=23)

# Influence level for node colors
influence_levels = {
    "Jules Verne": 10, 
    "H.G. Wells": 8,
    "Isaac Asimov": 7,
    "Arthur C. Clarke": 6,
    "Philip K. Dick": 6,
    "Frank Herbert": 5,
    "Ursula K. Le Guin": 4,
    "Ray Bradbury": 4,
    "William Gibson": 3,
    "Neal Stephenson": 2,
    "Robert A. Heinlein": 6,
    "Orson Scott Card": 3
}

node_colors = np.array([influence_levels[author] for author in authors])
node_colors = node_colors / max(node_colors)
colormap = plt.cm.plasma

edge_widths = [(G[u][v]['weight'] if 'weight' in G[u][v] else 2 * influence_levels[u] / 10) for u, v in influences]

plt.figure(figsize=(15, 12))
nodes = nx.draw_networkx_nodes(G, pos, node_color=node_colors, cmap=colormap, node_size=5000, edgecolors='grey', 
                               node_shape='h')
edges = nx.draw_networkx_edges(G, pos, width=edge_widths, arrowsize=15, edge_color='dimgray', style='dotted')
labels = nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', font_color='navy')

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend(loc='lower right', title='Impact Score', fontsize=8, frameon=True, framealpha=0.8, edgecolor='black')

plt.title("Sci-Fi Writer Impact Web", fontsize=16, fontweight='heavy', color='purple')  # Title changed
plt.axis('on')

plt.tight_layout()
plt.show()