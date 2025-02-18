import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Backstory and Context:
# In the world of fantasy, the Seven Kingdoms are interconnected by various alliances and conflicts. Each kingdom has connections of friendship, trade, or enmity with others. This network helps visualize the complex relationships that keep the Seven Kingdoms in constant flux.

# Define the kingdoms as nodes and their relationships as edges
kingdoms = [
    "Northland", "Riverland", "Highland", "Woodland",
    "Desertland", "Coastland", "Isleland", "Midland"
]

# Define edges with weights indicating the type of relationship; positive for alliances, negative for enmity
relationships = [
    ("Northland", "Riverland", 8),   # Strong Alliance
    ("Riverland", "Highland", 5),    # Moderate Alliance
    ("Highland", "Woodland", -7),    # Conflict
    ("Woodland", "Desertland", -5),  # Conflict
    ("Desertland", "Coastland", 7),  # Alliance
    ("Coastland", "Isleland", 6),    # Alliance
    ("Isleland", "Midland", -6),     # Conflict
    ("Midland", "Northland", 4),     # Trade Agreement
    ("Riverland", "Coastland", 9),   # Strong Alliance
    ("Highland", "Desertland", 5),   # Trade Agreement
    ("Northland", "Highland", -8)    # Significant Conflict
]

# Create a directed graph
G = nx.DiGraph()
G.add_nodes_from(kingdoms)
G.add_weighted_edges_from(relationships)

# Set the layout using spring layout
pos = nx.spring_layout(G, seed=42)

# Create a figure and axis
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
edge_labels = {(u, v): f"{'Alliance' if weight > 0 else 'Conflict'}\n({abs(weight)})" for u, v, weight in relationships}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='purple', font_size=9, ax=ax)

# Add annotations for key relationships
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

# Set the title and remove the axis
plt.title("The Web of Kingdoms:\nA Network of Alliances and Conflicts in the Seven Kingdoms", fontsize=16, fontweight='bold', pad=20)
plt.axis('off')

# Adjust layout to prevent overlap and ensure clarity
plt.tight_layout()
plt.show()