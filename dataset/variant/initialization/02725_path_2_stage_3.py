import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

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

for artist, collaborators in collaborations.items():
    for collaborator in collaborators:
        G.add_edge(artist, collaborator)

node_colors = {
    'Leonardo': 'lightblue',
    'Michelangelo': 'goldenrod',
    'Raphael': 'violet',
    'Donatello': 'coral',
    'Titian': 'limegreen',
    'Brunelleschi': 'skyblue',
    'Caravaggio': 'turquoise',
    'Galileo': 'lightcoral',
}

node_color_list = [node_colors[node] for node in G.nodes]

fig, ax = plt.subplots(figsize=(9, 9))

pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, ax=ax, node_size=1200, node_color=node_color_list, edgecolors='black', linewidths=1.5)
nx.draw_networkx_edges(G, pos, ax=ax, width=2, edge_color='gray', style='solid', alpha=0.6)
nx.draw_networkx_labels(G, pos, ax=ax, font_size=10, font_weight='bold', verticalalignment='center')
ax.set_title("Artisans' Network", fontsize=16, fontweight='bold', pad=20)
ax.axis('off')

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