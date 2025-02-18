import matplotlib.pyplot as plt
import networkx as nx

scientists = ['Newton', 'Einstein', 'Curie', 'Hawking', 'Tesla', 'Darwin', 'Galileo', 'Edison', 'Bohr', 'Turing']
collaborations = [
    ('Newton', 'Hawking', 70),
    ('Einstein', 'Galileo', 60),
    ('Curie', 'Turing', 55),
    ('Hawking', 'Curie', 85),
    ('Tesla', 'Newton', 95),
    ('Darwin', 'Einstein', 65),
    ('Edison', 'Bohr', 80),
    ('Galileo', 'Tesla', 60),
    ('Bohr', 'Edison', 90),
    ('Turing', 'Darwin', 75),
]

contribution_scores = {
    'Newton': 86,
    'Einstein': 89,
    'Curie': 80,
    'Hawking': 82,
    'Tesla': 87,
    'Darwin': 92,
    'Galileo': 78,
    'Edison': 85,
    'Bohr': 90,
    'Turing': 88
}

G = nx.DiGraph()
G.add_nodes_from(scientists)

for source, target, impact in collaborations:
    G.add_edge(source, target, weight=impact)

node_sizes = [1500 + contribution_scores[scientist]*10 for scientist in scientists]

pos = nx.spring_layout(G, seed=42)

edge_labels = {(u, v): f'{d["weight"]} pts' for u, v, d in G.edges(data=True)}
edge_widths = [2 + G[u][v]['weight'] / 25 for u, v in G.edges()]

node_colors = ['#8A2BE2', '#FF6347', '#FFE4C4', '#D3D3D3', '#FFB6C1', '#D8BFD8', '#00FF7F', '#E6E6FA', '#FFF0F5', '#FAFAD2']

fig, axs = plt.subplots(1, 2, figsize=(18, 8))
fig.suptitle('Scientific Network & Contributions', fontsize=18, fontweight='bold')

axs[1].set_title('Collaboration Graph', fontsize=16)
nx.draw_networkx_nodes(G, pos, ax=axs[1], node_size=node_sizes, node_color=node_colors, alpha=0.85, edgecolors='#4682B4', linewidths=1.5)
nx.draw_networkx_edges(G, pos, ax=axs[1], edgelist=G.edges, edge_color='black', arrows=True, arrowsize=12, width=edge_widths, style='dashed')
nx.draw_networkx_labels(G, pos, ax=axs[1], font_size=11, font_weight='normal')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, label_pos=0.5, bbox=dict(facecolor='lavender', alpha=0.75))
axs[1].grid(True, color='lightgray', linestyle='--', linewidth=0.5)

scientists_labels = list(contribution_scores.keys())
contributions_values = list(contribution_scores.values())
colors = [node_colors[scientists.index(name)] for name in scientists_labels]

axs[0].set_title('Contribution Scores', fontsize=16)
axs[0].bar(scientists_labels, contributions_values, color=colors, edgecolor='black', linestyle='-', linewidth=1)
axs[0].set_ylabel('Score', fontsize=12)
axs[0].set_xticklabels(scientists_labels, rotation=45, ha='right', fontsize=10)
axs[0].grid(True, axis='y', color='gray', linestyle=':', linewidth=0.7)

legend_lines = [plt.Line2D([0], [0], marker='s', color='w', markersize=9, markerfacecolor=node_colors[i], linestyle='--') for i in range(len(scientists))]
plt.legend(legend_lines, scientists, title="Scientists", loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()