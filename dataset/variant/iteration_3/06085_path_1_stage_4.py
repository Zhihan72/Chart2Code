import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

writers_connections = {
    "Isaac Asimov": ["Arthur C. Clarke", "Robert Heinlein", "Ray Bradbury"],
    "Arthur C. Clarke": ["Isaac Asimov", "Robert Heinlein", "Philip K. Dick"],
    "Robert Heinlein": ["Isaac Asimov", "Arthur C. Clarke", "Frank Herbert"],
    "Ray Bradbury": ["Isaac Asimov", "Philip K. Dick", "Ursula K. Le Guin"],
    "Philip K. Dick": ["Arthur C. Clarke", "Ray Bradbury", "J.G. Ballard"],
    "Frank Herbert": ["Robert Heinlein", "Ursula K. Le Guin"],
    "Ursula K. Le Guin": ["Ray Bradbury", "Frank Herbert", "H.G. Wells"],
    "J.G. Ballard": ["Philip K. Dick", "H.G. Wells"],
    "H.G. Wells": ["Ursula K. Le Guin", "J.G. Ballard"]
}

G = nx.Graph(writers_connections)
betweenness_centrality = nx.betweenness_centrality(G)
node_sizes = [1100 + 1800 * betweenness_centrality[node] for node in G.nodes()]
node_colors = ["#FF6347" if betweenness_centrality[node] > 0.1 else "#4682B4" for node in G.nodes()]

fig, ax = plt.subplots(2, 1, figsize=(8, 16))

pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, ax=ax[0], node_size=node_sizes, node_color=node_colors, edgecolors='grey', linewidths=2)
nx.draw_networkx_edges(G, pos, ax=ax[0], width=3, alpha=0.7, edge_color='purple', style='dashed')
nx.draw_networkx_labels(G, pos, ax=ax[0], font_size=9, font_family='sans-serif', font_weight='light')
ax[0].set_title("Sci-Fi Writers Network", fontsize=13, fontweight='normal')
ax[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.3, color='black')
ax[0].axis('on')

writer_names = list(betweenness_centrality.keys())
centrality_values = list(betweenness_centrality.values())
y_positions = np.arange(len(writer_names))
ax[1].barh(y_positions, centrality_values, color=plt.cm.plasma(np.linspace(0, 1, len(writer_names))), edgecolor='darkorange', linewidth=1.5)
ax[1].set_yticks(y_positions)
ax[1].set_yticklabels(writer_names, fontsize=9, style='italic')
ax[1].invert_yaxis()
ax[1].set_xlabel('Betweenness Centrality Score', fontsize=11, fontweight='medium')
ax[1].set_title("Centrality Analysis", fontsize=13, fontweight='medium')

plt.tight_layout()
plt.show()