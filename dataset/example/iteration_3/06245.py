import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Backstory:
# The graph represents the influences and technology exchange pathways between various ancient civilizations.
# The goal is to visualize how different civilizations interacted and influenced each other through trade, wars, cultural exchange, etc.

# Define ancient civilizations as nodes
civilizations = ["Ancient Egypt", "Mesopotamia", "Indus Valley", "Ancient China", "Ancient Greece", "Ancient Rome", "Maya", "Inca"]

# Define connections between civilizations
# Edges will represent different types of influences (e.g., trade, war, cultural exchange) with weights representing influence strength
connections = [
    ("Ancient Egypt", "Mesopotamia", "Trade", 20),
    ("Mesopotamia", "Indus Valley", "Cultural Exchange", 15),
    ("Ancient China", "Indus Valley", "War", 10),
    ("Ancient Greece", "Ancient Rome", "Trade", 25),
    ("Ancient Greece", "Mesopotamia", "Cultural Exchange", 18),
    ("Ancient Rome", "Ancient Egypt", "War", 22),
    ("Maya", "Inca", "Trade", 19),
    ("Inca", "Ancient China", "Cultural Exchange", 14),
    ("Maya", "Indus Valley", "Trade", 12),
    ("Ancient China", "Mesopotamia", "Trade", 17)
]

# Create graph
G = nx.DiGraph()

# Add nodes and edges to the graph
G.add_nodes_from(civilizations)
for src, dst, influence, weight in connections:
    G.add_edge(src, dst, influence=influence, weight=weight)

# Determine positions using spring layout for better visualization
pos = nx.spring_layout(G, seed=2023)

# Extract edges and labels
edges = G.edges(data=True)
edge_colors = ["blue" if data['influence'] == "Trade" else "green" if data['influence'] == "Cultural Exchange" else "red" for _, _, data in edges]
edge_weights = [data['weight'] for _, _, data in edges]

# Draw the nodes with custom sizes and colors
node_size = [1000 * (G.degree(civilization) + 1) for civilization in civilizations]
nx.draw_networkx_nodes(G, pos, node_color="#FFD700", node_size=node_size, edgecolors='black', linewidths=1.5)

# Draw the edges with custom styles and thickness
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color=edge_colors, width=[weight / 5 for weight in edge_weights], arrowstyle='-|>', arrowsize=15)

# Draw the labels for nodes
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', font_color='darkgreen')

# Draw labels for edges with influence type and weight
edge_labels = {(u, v): f"{data['influence']} ({data['weight']})" for u, v, data in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_color='black', font_weight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.6))

# Title and layout adjustments
plt.title("Influences and Technology Exchange among Ancient Civilizations", fontsize=16, fontweight='bold', color='navy', pad=20)
plt.axis('off')
plt.tight_layout()

# Show plot
plt.show()