import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

collaborations = {
    'Leonardo da Vinci': ['Michelangelo', 'Donatello', 'Raphael'],
    'Michelangelo': ['Raphael', 'Titian'],
    'Raphael': ['Titian', 'Donatello', 'Brunelleschi'],
    'Donatello': ['Brunelleschi'],
    'Titian': [],  # Removed 'Caravaggio'
    'Brunelleschi': ['Leonardo da Vinci'],
    # Removed 'Caravaggio': ['Galileo'],
    'Galileo': ['Michelangelo'],
}

for artist, collaborators in collaborations.items():
    for collaborator in collaborators:
        G.add_edge(artist, collaborator)

node_colors = {
    'Leonardo da Vinci': 'turquoise',
    'Michelangelo': 'limegreen',
    'Raphael': 'goldenrod',
    'Donatello': 'lightblue',
    'Titian': 'lightcoral',
    'Brunelleschi': 'violet',
    # Removed 'Caravaggio': 'coral',
    'Galileo': 'skyblue',
}

node_color_list = [node_colors[node] for node in G.nodes]
collaboration_count = {artist: len(collaborators) for artist, collaborators in collaborations.items()}

fig, axes = plt.subplots(1, 2, figsize=(18, 9))

pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, ax=axes[0], node_size=1200, node_color=node_color_list, edgecolors='black', linewidths=1.5)
nx.draw_networkx_edges(G, pos, ax=axes[0], width=2, edge_color='gray', style='solid', alpha=0.6)
nx.draw_networkx_labels(G, pos, ax=axes[0], font_size=10, font_weight='bold', verticalalignment='center')
axes[0].set_title("Creative Constellations:\nRenaissance Artisans' Network", fontsize=16, fontweight='bold', pad=20)
axes[0].axis('off')

legend_labels = {
    'turquoise': 'Invention',
    'limegreen': 'Sculpture',
    'goldenrod': 'Painting',
    'lightblue': 'Sculpture',
    'lightcoral': 'Painting',
    'violet': 'Architecture',
    # Removed 'coral': 'Painting',
    'skyblue': 'Science',
}
handles = [plt.Line2D([0], [0], marker='o', color='w', label=label, markerfacecolor=color, markersize=10)
           for color, label in legend_labels.items()]
axes[0].legend(handles=handles, loc='upper right', title="Disciplines", fontsize=9, bbox_to_anchor=(1.3, 1))

axes[1].bar(collaboration_count.keys(), collaboration_count.values(), color=node_color_list, edgecolor='black')
axes[1].set_title("Collaboration Frequency\nAmong Renaissance Artisans", fontsize=16, fontweight='bold', pad=20)
axes[1].set_ylabel("Number of Collaborations", fontsize=12)
axes[1].set_xticklabels(collaboration_count.keys(), rotation=45, ha='right')

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()