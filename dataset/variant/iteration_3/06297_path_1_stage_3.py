import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

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

G = nx.Graph()
G.add_edges_from(influences)

pos = nx.spring_layout(G, seed=23)

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
colormap = plt.cm.viridis  # Changed colormap from plasma to viridis

edge_widths = [1.5 * influence_levels[u] / 10 for u, v in influences]  # Reduced edge width slightly

plt.figure(figsize=(15, 12))
nx.draw_networkx_nodes(G, pos, node_color=node_colors, cmap=colormap, node_size=4000, node_shape='s')  # Changed node shape to square
nx.draw_networkx_edges(G, pos, width=edge_widths, style='dashed')  # Changed edge style to dashed

plt.axis('on')
plt.grid(True)  # Added grid
plt.legend(['Influence Network'], loc='upper right')  # Added legend

plt.tight_layout()
plt.show()