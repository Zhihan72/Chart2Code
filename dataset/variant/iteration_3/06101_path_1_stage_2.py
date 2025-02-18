import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

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

G = nx.DiGraph()
G.add_nodes_from(kingdoms)
G.add_weighted_edges_from(relationships)

pos = nx.spring_layout(G, seed=42)

fig, ax = plt.subplots(figsize=(14, 10))

node_colors = ['palegreen', 'lightcoral', 'lightskyblue', 'thistle', 
               'khaki', 'lightpink', 'peachpuff', 'lightcyan']
nx.draw_networkx_nodes(
    G, pos, node_size=1600, node_color=node_colors, edgecolors='black', ax=ax
)

edge_colors = ['darkolivegreen' if weight > 0 else 'firebrick' for u, v, weight in relationships]
weights = np.abs([weight for u, v, weight in relationships])
nx.draw_networkx_edges(
    G, pos, edgelist=relationships, arrowstyle='-|>', arrowsize=15,
    edge_color=edge_colors, width=weights, ax=ax, connectionstyle="arc3,rad=0.2"
)

nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', verticalalignment='center', ax=ax)

edge_labels = {(u, v): f"{'Alli' if weight > 0 else 'Confl'}\n({abs(weight)})" for u, v, weight in relationships}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='purple', font_size=9, ax=ax)

annotations = {
    "North-River": (7.5, -0.5, 'Strong Alli'),
    "North-High": (3.5, 0.7, 'Deep Confl'),
    "River-Coast": (8.5, 7.5, 'Strong Alli'),
    "High-Wood": (7.5, 2.5, 'War Zone')
}
for key, (x, y, text) in annotations.items():
    ax.annotate(text, xy=pos[key.split('-')[0]], xytext=(x, y), textcoords="offset points",
                arrowprops=dict(arrowstyle="->", color='black', lw=1.5),
                bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='lightyellow'))

plt.title("Web of Kingdoms:\nNetwork of Alliances and Conflicts", fontsize=16, fontweight='bold', pad=20)
plt.axis('off')

plt.tight_layout()
plt.show()