import matplotlib.pyplot as plt
import networkx as nx

# Create an undirected graph (default in nx.Graph)
G = nx.Graph()

# Define collaborations as an undirected series of edges
collaborations = {
    'Leonardo': ['Galileo', 'Titian', 'Michelangelo'],
    'Michelangelo': ['Leonardo', 'Donatello'],
    'Raphael': ['Donatello', 'Caravaggio', 'Leonardo'],
    'Donatello': ['Raphael'],
    'Titian': ['Brunelleschi'],
    'Brunelleschi': ['Raphael'],
    'Caravaggio': ['Michelangelo'],
    'Galileo': ['Brunelleschi'],
}

# Add edges to the graph
for artist, collaborators in collaborations.items():
    for collaborator in collaborators:
        G.add_edge(artist, collaborator)

# Define node colors
node_colors = {
    'Leonardo': 'skyblue',
    'Michelangelo': 'lightcoral',
    'Raphael': 'turquoise',
    'Donatello': 'limegreen',
    'Titian': 'coral',
    'Brunelleschi': 'goldenrod',
    'Caravaggio': 'lightblue',
    'Galileo': 'violet',
}

node_color_list = [node_colors[node] for node in G.nodes]

# Set up the plot with a fixed size
fig, ax = plt.subplots(figsize=(9, 9))

# Calculate layout positions
pos = nx.spring_layout(G, seed=42)

# Draw the nodes, edges, and labels on the graph
nx.draw_networkx_nodes(G, pos, ax=ax, node_size=1200, node_color=node_color_list, edgecolors='black', linewidths=1.5)
nx.draw_networkx_edges(G, pos, ax=ax, width=2, edge_color='gray', style='solid', alpha=0.6)
nx.draw_networkx_labels(G, pos, ax=ax, font_size=10, font_weight='bold', verticalalignment='center')
ax.set_title("Artisans' Network", fontsize=16, fontweight='bold', pad=20)
ax.axis('off')

# Create a legend for node colors
legend_labels = {
    'lightblue': 'Invention',
    'goldenrod': 'Sculpture',
    'violet': 'Painting',
    'coral': 'Sculpture',
    'limegreen': 'Painting',
    'skyblue': 'Architecture',
    'turquoise': 'Painting',
    'lightcoral': 'Science',
}
handles = [plt.Line2D([0], [0], marker='o', color='w', label=label, markerfacecolor=color, markersize=10) for color, label in legend_labels.items()]
ax.legend(handles=handles, loc='upper right', title="Disciplines", fontsize=9, bbox_to_anchor=(1.3, 1))

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()