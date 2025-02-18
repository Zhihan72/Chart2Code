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
node_sizes = [1000 + 2000 * betweenness_centrality[node] for node in G.nodes()]

single_color = "#4682B4"
node_colors = [single_color for _ in G.nodes()]

fig, ax = plt.subplots(2, 1, figsize=(8, 16))

pos = nx.spring_layout(G, seed=24)
nx.draw_networkx_nodes(G, pos, ax=ax[0], node_size=node_sizes, node_color=node_colors, edgecolors='black')
nx.draw_networkx_edges(G, pos, ax=ax[0], width=2, alpha=0.6, edge_color='gray')
ax[0].axis('off')

writer_names = list(betweenness_centrality.keys())
centrality_values = list(betweenness_centrality.values())

sorted_indices = np.argsort(centrality_values)[::-1]
sorted_centrality_values = [centrality_values[i] for i in sorted_indices]

y_positions = np.arange(len(writer_names))
ax[1].barh(y_positions, sorted_centrality_values, color=single_color)
ax[1].invert_yaxis()

plt.tight_layout()
plt.show()