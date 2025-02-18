import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define science fiction writers and their collaborations
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

# Create the graph
G = nx.Graph(writers_connections)

# Calculate node sizes and colors based on betweenness centrality
betweenness_centrality = nx.betweenness_centrality(G)
node_sizes = [1000 + 2000 * betweenness_centrality[node] for node in G.nodes()]

# Shuffle the colors assigned to the nodes
# Original color code: "#FFA07A" if centrality > 0.1 else "#20B2AA"
node_colors = ["#20B2AA" if betweenness_centrality[node] > 0.1 else "#FFA07A" for node in G.nodes()]

# Create a subplot layout
fig, ax = plt.subplots(1, 2, figsize=(16, 8))

# First subplot: Network Graph
pos = nx.spring_layout(G, seed=24)
nx.draw_networkx_nodes(G, pos, ax=ax[0], node_size=node_sizes, node_color=node_colors, edgecolors='black')
nx.draw_networkx_edges(G, pos, ax=ax[0], width=2, alpha=0.6, edge_color='gray')
nx.draw_networkx_labels(G, pos, ax=ax[0], font_size=10, font_family='serif')
ax[0].set_title("Interconnections of Sci-Fi Writers:\nCollaborative and Influential Ties", fontsize=14, fontweight='bold')
ax[0].axis('off')

# Second subplot: Bar Chart of Betweenness Centrality
writer_names = list(betweenness_centrality.keys())
centrality_values = list(betweenness_centrality.values())
y_positions = np.arange(len(writer_names))
ax[1].barh(y_positions, centrality_values, color=plt.cm.viridis(np.linspace(0.1, 0.9, len(writer_names))))
ax[1].set_yticks(y_positions)
ax[1].set_yticklabels(writer_names, fontsize=10)
ax[1].invert_yaxis()  # Highest centrality on top
ax[1].set_xlabel('Betweenness Centrality', fontsize=12)
ax[1].set_title("Writer Centrality Ranking", fontsize=14, fontweight='bold')

# Adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()