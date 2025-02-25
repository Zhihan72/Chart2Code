import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define authors as nodes
authors = [
    "Isaac Asimov", "Arthur C. Clarke", "Philip K. Dick", "H.G. Wells",
    "Jules Verne", "Frank Herbert", "Ursula K. Le Guin", "Ray Bradbury",
    "William Gibson", "Neal Stephenson", "Robert A. Heinlein", "Orson Scott Card"
]

# Define influences as edges
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

# Create an undirected graph
G = nx.Graph()
G.add_edges_from(influences)

# Set positions using spring layout for clarity
pos = nx.spring_layout(G, seed=23)

# Define node influence level for node color
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

# Node colors based on influence level
node_colors = np.array([influence_levels[author] for author in authors])
node_colors = node_colors / max(node_colors)  # Normalize to range [0, 1] for colormap
colormap = plt.cm.plasma

# Edge widths based on strength of influence
edge_widths = [2 * influence_levels[u] / 10 for u, v in influences]

# Plot the graph
plt.figure(figsize=(15, 12))
nodes = nx.draw_networkx_nodes(G, pos, node_color=node_colors, cmap=colormap, node_size=5000, edgecolors='black')
edges = nx.draw_networkx_edges(G, pos, width=edge_widths, edge_color='lightgrey')
labels = nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', font_color='black')

# Create legend for node colors
for level, author in influence_levels.items():
    plt.plot([], [], color=colormap(author/max(influence_levels.values())), marker='o', markersize=15, linestyle='',
             label=level)
plt.legend(loc='upper left', title='Influence Level', fontsize=10, frameon=False)

# Title and axis off
plt.title("Influence Network Among Science Fiction Authors", fontsize=18, fontweight='bold', pad=20)
plt.axis('off')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()