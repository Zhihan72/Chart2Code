import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

kingdoms = [
    "Northland", "Riverland", "Highland", "Woodland",
    "Desertland", "Coastland", "Isleland", "Midland"
]

relationships = [
    ("Northland", "Riverland", 8),
    ("Riverland", "Highland", 5),
    ("Highland", "Woodland", -7),
    ("Woodland", "Desertland", -5),
    ("Desertland", "Coastland", 7),
    ("Coastland", "Isleland", 6),
    ("Isleland", "Midland", -6),
    ("Midland", "Northland", 4),
    ("Riverland", "Coastland", 9),
    ("Highland", "Desertland", 5),
    ("Northland", "Highland", -8)
]

G = nx.DiGraph()
G.add_nodes_from(kingdoms)
G.add_weighted_edges_from(relationships)

pos = nx.spring_layout(G, seed=42)

fig, ax = plt.subplots(figsize=(14, 10))

# Updated node color scheme
node_colors = ['palegreen', 'lightcoral', 'lightskyblue', 'thistle', 
               'khaki', 'lightpink', 'peachpuff', 'lightcyan']
nx.draw_networkx_nodes(
    G, pos, node_size=1600, node_color=node_colors, edgecolors='black', ax=ax
)

# Updated edge color scheme
edge_colors = ['darkolivegreen' if weight > 0 else 'firebrick' for u, v, weight in relationships]
weights = np.abs([weight for u, v, weight in relationships])
nx.draw_networkx_edges(
    G, pos, edgelist=relationships, arrowstyle='-|>', arrowsize=15,
    edge_color=edge_colors, width=weights, ax=ax, connectionstyle="arc3,rad=0.2"
)

nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', verticalalignment='center', ax=ax)

edge_labels = {(u, v): f"{'Alliance' if weight > 0 else 'Conflict'}\n({abs(weight)})" for u, v, weight in relationships}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='purple', font_size=9, ax=ax)

annotations = {
    "Northland-Riverland": (7.5, -0.5, 'Strongest Alliance'),
    "Northland-Highland": (3.5, 0.7, 'Deep-Seated Conflict'),
    "Riverland-Coastland": (8.5, 7.5, 'Strongest Alliance'),
    "Highland-Woodland": (7.5, 2.5, 'Active War Zone')
}
for key, (x, y, text) in annotations.items():
    ax.annotate(text, xy=pos[key.split('-')[0]], xytext=(x, y), textcoords="offset points",
                arrowprops=dict(arrowstyle="->", color='black', lw=1.5),
                bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='lightyellow'))

plt.title("The Web of Kingdoms:\nA Network of Alliances and Conflicts in the Seven Kingdoms", fontsize=16, fontweight='bold', pad=20)
plt.axis('off')

plt.tight_layout()
plt.show()