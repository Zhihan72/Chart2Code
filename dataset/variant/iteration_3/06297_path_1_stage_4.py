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

influence_levels = {
    "Jules Verne": 3,
    "H.G. Wells": 10,
    "Isaac Asimov": 6,
    "Arthur C. Clarke": 4,
    "Philip K. Dick": 7,
    "Frank Herbert": 5,
    "Ursula K. Le Guin": 5,
    "Ray Bradbury": 6,
    "William Gibson": 4,
    "Neal Stephenson": 8,
    "Robert A. Heinlein": 10,
    "Orson Scott Card": 2
}

node_colors = np.array([influence_levels[author] for author in authors])
node_colors = node_colors / max(node_colors)
colormap = plt.cm.viridis

edge_widths = [1.5 * influence_levels[u] / 10 for u, v in influences]

plt.figure(figsize=(15, 12))
nx.draw_networkx_nodes(G, pos, node_color=node_colors, cmap=colormap, node_size=4000, node_shape='s')
nx.draw_networkx_edges(G, pos, width=edge_widths, style='dashed')

plt.axis('on')
plt.grid(True)
plt.legend(['Influence Network'], loc='upper right')

plt.tight_layout()
plt.show()