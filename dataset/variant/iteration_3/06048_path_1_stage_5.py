import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

authors = [
    "Isaac Asimov", "Frank Herbert", "Arthur C. Clarke", "H.G. Wells",
    "Jules Verne", "Ursula K. Le Guin", "Ray Bradbury", "Philip K. Dick",
    "William Gibson", "Neal Stephenson", "Robert A. Heinlein", "Orson Scott Card"
]

influences = [
    ("Jules Verne", "Philip K. Dick"),
    ("H.G. Wells", "William Gibson"),
    ("Isaac Asimov", "Ray Bradbury"),
    ("Isaac Asimov", "Arthur C. Clarke"),
    ("Arthur C. Clarke", "Frank Herbert"),
    ("Frank Herbert", "Ursula K. Le Guin"),
    ("Ray Bradbury", "Neal Stephenson"),
    ("William Gibson", "Ursula K. Le Guin"),
    ("Robert A. Heinlein", "Neal Stephenson"),
    ("Philip K. Dick", "Arthur C. Clarke"),
    ("Arthur C. Clarke", "Orson Scott Card"),
    ("Isaac Asimov", "Robert A. Heinlein")
]

G = nx.Graph()
G.add_edges_from(influences)

pos = nx.spring_layout(G, seed=23)

# Manually shuffled influence levels for color mapping
shuffled_influence_levels = {
    "Jules Verne": 6,
    "H.G. Wells": 4,
    "Isaac Asimov": 7,
    "Arthur C. Clarke": 10,
    "Philip K. Dick": 5,
    "Frank Herbert": 10,
    "Ursula K. Le Guin": 3,
    "Ray Bradbury": 8,
    "William Gibson": 2,
    "Neal Stephenson": 5,
    "Robert A. Heinlein": 4,
    "Orson Scott Card": 6
}

node_colors = np.array([shuffled_influence_levels[author] for author in authors])
node_colors = node_colors / max(node_colors)
colormap = plt.cm.viridis

edge_widths = [1.5 * shuffled_influence_levels[u] / 10 for u, v in influences]

plt.figure(figsize=(15, 12))
nx.draw_networkx_nodes(G, pos, node_color=node_colors, cmap=colormap, node_size=4000, node_shape='s')
nx.draw_networkx_edges(G, pos, width=edge_widths, style='dashed')

plt.axis('on')
plt.grid(True)
plt.legend(['Influence Network'], loc='upper right')

plt.tight_layout()
plt.show()