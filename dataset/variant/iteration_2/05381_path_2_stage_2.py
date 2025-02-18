import matplotlib.pyplot as plt
import networkx as nx

scientists = ['Newton', 'Einstein', 'Curie', 'Hawking', 'Tesla', 'Darwin', 'Galileo', 'Edison', 'Bohr', 'Turing']

collaborations = [
    ('Newton', 'Einstein', 85),
    ('Einstein', 'Curie', 70),
    ('Curie', 'Hawking', 65),
    ('Hawking', 'Tesla', 60),
    ('Tesla', 'Edison', 90),
    ('Darwin', 'Galileo', 75),
    ('Edison', 'Turing', 80),
    ('Galileo', 'Newton', 95),
    ('Bohr', 'Einstein', 55),
    ('Turing', 'Bohr', 60),
]

contribution_scores = {
    'Newton': 90,
    'Einstein': 92,
    'Curie': 88,
    'Hawking': 86,
    'Tesla': 87,
    'Darwin': 80,
    'Galileo': 89,
    'Edison': 85,
    'Bohr': 78,
    'Turing': 82
}

G = nx.Graph()
G.add_nodes_from(scientists)
for source, target, impact in collaborations:
    G.add_edge(source, target, weight=impact)

node_sizes = [1500 + contribution_scores[scientist] * 10 for scientist in scientists]
pos = nx.circular_layout(G)
edge_labels = {(u, v): f'{d["weight"]} pts' for u, v, d in G.edges(data=True)}
edge_widths = [0.5 + G[u][v]['weight'] / 20 for u, v in G.edges()]

node_colors = ['#FF5733', '#33FF57', '#3357FF', '#F33FFF', '#FFF333', '#33FFF3', '#F3FF33', '#7F33FF', '#FF3380', '#33FF80']

fig, axs = plt.subplots(1, 2, figsize=(20, 10))
fig.suptitle('Sci. Collabs & Scores', fontsize=16, fontweight='bold')

# Subplot 1: Network Graph
axs[0].set_title('Collab Network', fontsize=14)
nx.draw_networkx_nodes(G, pos, ax=axs[0], node_size=node_sizes, node_color=node_colors, alpha=0.9, edgecolors='black')
nx.draw_networkx_edges(G, pos, ax=axs[0], edgelist=G.edges, edge_color='gray', width=edge_widths)
nx.draw_networkx_labels(G, pos, ax=axs[0], font_size=12, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, label_pos=0.3, bbox=dict(facecolor='white', alpha=0.7))
axs[0].axis('off')

scientists_labels = list(contribution_scores.keys())
contributions_values = list(contribution_scores.values())
colors = [node_colors[scientists.index(name)] for name in scientists_labels]

axs[1].set_title('Contributions', fontsize=14)
axs[1].bar(scientists_labels, contributions_values, color=colors)
axs[1].set_ylabel('Score')
axs[1].set_xticklabels(scientists_labels, rotation=45, ha='right')

legend_lines = [plt.Line2D([0], [0], marker='o', color='w', markersize=10, markerfacecolor=node_colors[i]) for i in range(len(scientists))]
plt.legend(legend_lines, scientists, title="Sci.", loc='lower right', bbox_to_anchor=(1, 0))

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()