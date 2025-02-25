import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

authors = [
    "Ray Bradbury", "Philip K. Dick", "Ursula K. Le Guin", "Arthur C. Clarke",
    "Isaac Asimov", "Frank Herbert", "H.G. Wells", "Neal Stephenson",
    "William Gibson", "Jules Verne", "Orson Scott Card", "Robert A. Heinlein"
]

# Alter existing influences while retaining structure
influences = [
    ("Ray Bradbury", "Philip K. Dick"),
    ("Philip K. Dick", "Isaac Asimov"),
    ("Isaac Asimov", "Arthur C. Clarke"),
    ("Ursula K. Le Guin", "H.G. Wells"),
    ("Arthur C. Clarke", "Frank Herbert"),
    ("Ray Bradbury", "William Gibson"),
    ("William Gibson", "Neal Stephenson"),
    ("H.G. Wells", "Jules Verne"),
    ("Frank Herbert", "Robert A. Heinlein"),
    ("Neal Stephenson", "Orson Scott Card"),
    ("Jules Verne", "Robert A. Heinlein"),
    ("Orson Scott Card", "Ursula K. Le Guin")
]

G = nx.DiGraph()
G.add_edges_from(influences)
pos = nx.spring_layout(G, seed=23)

influence_levels = {
    "Ray Bradbury": 8, 
    "Philip K. Dick": 7,
    "Ursula K. Le Guin": 6,
    "Arthur C. Clarke": 5,
    "Isaac Asimov": 8,
    "Frank Herbert": 4,
    "H.G. Wells": 6,
    "Neal Stephenson": 3,
    "William Gibson": 10,
    "Jules Verne": 3,
    "Orson Scott Card": 4,
    "Robert A. Heinlein": 5
}

# Node colors are shuffled manually
node_colors = np.array([8, 3, 3, 4, 10, 7, 5, 6, 8, 6, 4, 5])
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

plt.title("Sci-Fi Writer Impact Web", fontsize=16, fontweight='heavy', color='purple')
plt.axis('on')

plt.tight_layout()
plt.show()