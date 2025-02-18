import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Nodes and their relationships with weights
kingdoms = [
    "North", "River", "High", "Wood",
    "Desert", "Coast", "Isle", "Mid"
]

relationships = [
    ("North", "River", 8),
    ("River", "High", 5),
    ("High", "Wood", -7),
    ("Wood", "Desert", -5),
    ("Desert", "Coast", 7),
    ("Coast", "Isle", 6),
    ("Isle", "Mid", -6),
    ("Mid", "North", 4),
    ("River", "Coast", 9),
    ("High", "Desert", 5),
    ("North", "High", -8)
]

# Create a directed graph
G = nx.DiGraph()
G.add_nodes_from(kingdoms)
G.add_weighted_edges_from(relationships)

# Set layout
pos = nx.spring_layout(G, seed=42)

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 10))

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=1600, node_color='lightblue', edgecolors='black', ax=ax)

# Draw edges with weights
edge_colors = ['green' if weight > 0 else 'red' for u, v, weight in relationships]
weights = np.abs([weight for u, v, weight in relationships])
nx.draw_networkx_edges(
    G, pos, edgelist=relationships, arrowstyle='-|>', arrowsize=15, 
    edge_color=edge_colors, width=weights, ax=ax, connectionstyle="arc3,rad=0.2"
)

# Draw labels for nodes
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', verticalalignment='center', ax=ax)

# Add edge labels for weights
edge_labels = {(u, v): f"{'Ally' if weight > 0 else 'Conflict'}\n({abs(weight)})" for u, v, weight in relationships}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='purple', font_size=9, ax=ax)

# Add annotations for key relationships
annotations = {
    "North-River": (7.5, -0.5, 'Strongest Ally'),
    "North-High": (3.5, 0.7, 'Deep Conflict'),
    "River-Coast": (8.5, 7.5, 'Strongest Ally'),
    "High-Wood": (7.5, 2.5, 'War Zone')
}
for key, (x, y, text) in annotations.items():
    ax.annotate(text, xy=pos[key.split('-')[0]], xytext=(x, y), textcoords="offset points",
                arrowprops=dict(arrowstyle="->", color='black', lw=1.5),
                bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='lightyellow'))

# Set the title and remove the axis
plt.title("Kingdoms Network", fontsize=16, fontweight='bold', pad=20)
plt.axis('off')

# Adjust layout
plt.tight_layout()
plt.show()